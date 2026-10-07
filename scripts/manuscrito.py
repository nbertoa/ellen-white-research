#!/usr/bin/env python3
"""Ensambla y valida el manuscrito de Ellen White Research.

Uso:
  python scripts/manuscrito.py
  python scripts/manuscrito.py --check-only
  python scripts/manuscrito.py --strict

El script no altera los capítulos fuente. Genera una copia de lectura en
build/manuscrito-completo.md y un informe en build/validacion-manuscrito.txt.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
BUILD_DIR = ROOT / "build"
OUTPUT = BUILD_DIR / "manuscrito-completo.md"
REPORT = BUILD_DIR / "validacion-manuscrito.txt"

MANUSCRIPT_FILES = [
    "capitulos/00-nota-al-lector.md",
    "capitulos/00-prologo.md",
    "capitulos/01-que-significa-inspiracion-iluminacion-revelacion-y-don-de-profecia.md",
    "capitulos/02-que-credenciales-debe-reunir-un-profeta-autentico.md",
    "capitulos/03-que-afirmo-ellen-white-sobre-su-propio-don-y-sobre-el-origen-y-la-autoridad-de-sus-mensajes.md",
    "capitulos/04-que-ocurrio-realmente-en-las-primeras-visiones-de-ellen-g-white.md",
    "capitulos/05-que-ocurria-fisicamente-durante-las-visiones-de-ellen-g-white.md",
    "capitulos/06-que-podria-explicar-las-visiones-de-ellen-g-white.md",
    "capitulos/07-predijo-ellen-white-acontecimientos-que-no-podia-conocer.md",
    "capitulos/08-conocio-ellen-white-cosas-que-no-podia-saber-por-medios-normales.md",
    "capitulos/09-utilizo-ellen-white-escritos-de-otros-autores.md",
    "capitulos/10-que-implica-dependencia-literaria-para-inspiracion.md",
    "capitulos/11-hasta-que-punto-podemos-atribuir-a-ellen-white-los-libros-publicados-bajo-su-nombre.md",
    "capitulos/12-cometio-ellen-white-errores-en-asuntos-de-historia-ciencia-y-salud.md",
    "capitulos/13-se-contradijo-ellen-white.md",
    "capitulos/14-que-revela-su-vida-y-conducta-sobre-su-pretension-profetica.md",
    "capitulos/15-que-frutos-produjo-el-ministerio-de-ellen-white.md",
    "capitulos/16-que-explicacion-encaja-mejor-con-toda-la-evidencia.md",
    "capitulos/17-epilogo.md",
]

FOOTNOTE_REF_RE = re.compile(r"\[\^([^\]]+)\]")
FOOTNOTE_DEF_RE = re.compile(r"(?m)^\[\^([^\]]+)\]:")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
HEADING_RE = re.compile(r"(?m)^(#{1,6})\s+(.+?)\s*$")
GIT_HASH_RE = re.compile(r"\b[0-9a-f]{12,40}\b")

INTERNAL_MARKERS = [
    re.compile(r"\.\./hallazgos/", re.I),
    re.compile(r"\.\./metodologia/", re.I),
    re.compile(r"\bexpediente\b", re.I),
    re.compile(r"\bficha\b", re.I),
    re.compile(r"\bmatriz vigente\b", re.I),
    re.compile(r"PDF aportado", re.I),
    re.compile(r"EPUB proporcionado", re.I),
    re.compile(r"no se cotej[oó] aqu[ií]", re.I),
    re.compile(r"no inventar paginaci[oó]n", re.I),
    re.compile(r"revision-[\w-]+", re.I),
]


@dataclass
class Finding:
    level: str  # ERROR | WARN
    file: str
    message: str

    def render(self) -> str:
        return f"{self.level}: {self.file}: {self.message}"


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def iter_local_links(text: str) -> Iterable[tuple[str, str, int]]:
    for match in MARKDOWN_LINK_RE.finditer(text):
        label, target = match.groups()
        target = target.strip()
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        yield label, target, match.start()


def validate_file(path: Path, findings: list[Finding]) -> None:
    name = rel(path)
    if not path.exists():
        findings.append(Finding("ERROR", name, "archivo requerido inexistente"))
        return

    text = path.read_text(encoding="utf-8")

    # Notas: una definición por identificador y toda referencia resuelta.
    refs = FOOTNOTE_REF_RE.findall(text)
    defs = FOOTNOTE_DEF_RE.findall(text)
    def_counts: dict[str, int] = {}
    for key in defs:
        def_counts[key] = def_counts.get(key, 0) + 1

    for key in sorted(set(refs)):
        if key not in def_counts:
            findings.append(Finding("ERROR", name, f"nota referenciada sin definición: [^{key}]"))
    for key, count in sorted(def_counts.items()):
        if count > 1:
            findings.append(Finding("ERROR", name, f"nota definida {count} veces: [^{key}]"))
        if key not in refs:
            findings.append(Finding("WARN", name, f"nota definida pero no usada: [^{key}]"))

    # Links locales.
    for label, target, offset in iter_local_links(text):
        pure_target = target.split("#", 1)[0].split("?", 1)[0]
        if not pure_target:
            continue
        linked = (path.parent / pure_target).resolve()
        if not linked.exists():
            findings.append(
                Finding(
                    "ERROR",
                    name,
                    f"enlace local roto en línea {line_number(text, offset)}: {label!r} -> {target}",
                )
            )

    # Encabezados: el libro se organiza por preguntas.
    for match in HEADING_RE.finditer(text):
        heading = match.group(2).strip()
        # Se permite un prefijo editorial, pero debe contener una pregunta real.
        if "¿" not in heading or "?" not in heading:
            findings.append(
                Finding(
                    "WARN",
                    name,
                    f"encabezado no formulado como pregunta en línea {line_number(text, match.start())}: {heading}",
                )
            )

    # Rastros internos: sólo se controlan en el manuscrito, no en hallazgos/metodología.
    for pattern in INTERNAL_MARKERS:
        for match in pattern.finditer(text):
            findings.append(
                Finding(
                    "WARN",
                    name,
                    f"posible rastro de edición interna en línea {line_number(text, match.start())}: {match.group(0)!r}",
                )
            )

    # Hashes de git dentro del manuscrito impreso.
    for match in GIT_HASH_RE.finditer(text):
        findings.append(
            Finding(
                "WARN",
                name,
                f"posible hash de git en línea {line_number(text, match.start())}: {match.group(0)}",
            )
        )

    # Normalización editorial pendiente: sólo se informa, no se sustituye automáticamente.
    for match in re.finditer(r"(?m)^#{1,6} .*\bEllen(?: G\.)? White\b", text):
        findings.append(
            Finding(
                "WARN",
                name,
                f"grafía inglesa en encabezado, revisar para edición castellana (línea {line_number(text, match.start())})",
            )
        )


def namespace_footnotes(text: str, prefix: str) -> str:
    """Hace únicos los identificadores de notas al concatenar capítulos."""
    keys = set(FOOTNOTE_REF_RE.findall(text)) | set(FOOTNOTE_DEF_RE.findall(text))
    # Reemplazar identificadores largos primero evita colisiones parciales teóricas.
    for key in sorted(keys, key=len, reverse=True):
        text = text.replace(f"[^{key}]", f"[^{prefix}-{key}]")
    return text


def strip_internal_md_links(text: str) -> str:
    """En la edición de lectura, deja el texto visible y quita links internos .md."""
    def repl(match: re.Match[str]) -> str:
        label, target = match.groups()
        target_no_anchor = target.split("#", 1)[0].split("?", 1)[0]
        if target_no_anchor.endswith(".md") or target_no_anchor.startswith(("../hallazgos/", "../metodologia/")):
            return label
        return match.group(0)

    return MARKDOWN_LINK_RE.sub(repl, text)


def build_manuscript(findings: list[Finding]) -> str:
    parts: list[str] = []
    for index, rel_path in enumerate(MANUSCRIPT_FILES):
        path = ROOT / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8").strip()
        prefix = f"m{index:02d}"
        text = namespace_footnotes(text, prefix)
        text = strip_internal_md_links(text)
        parts.append(text)
    return "\n\n---\n\n".join(parts).rstrip() + "\n"


def validate_order(findings: list[Finding]) -> None:
    seen: set[str] = set()
    for item in MANUSCRIPT_FILES:
        if item in seen:
            findings.append(Finding("ERROR", item, "archivo repetido en MANUSCRIPT_FILES"))
        seen.add(item)


def write_report(findings: list[Finding]) -> None:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    errors = [f for f in findings if f.level == "ERROR"]
    warnings = [f for f in findings if f.level == "WARN"]
    lines = [
        "VALIDACIÓN DEL MANUSCRITO",
        "=========================",
        f"Archivos esperados: {len(MANUSCRIPT_FILES)}",
        f"Errores: {len(errors)}",
        f"Advertencias: {len(warnings)}",
        "",
    ]
    if findings:
        lines.extend(f.render() for f in findings)
    else:
        lines.append("Sin hallazgos.")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check-only", action="store_true", help="valida sin generar manuscrito")
    parser.add_argument("--strict", action="store_true", help="trata advertencias como fallo")
    args = parser.parse_args()

    findings: list[Finding] = []
    validate_order(findings)
    for rel_path in MANUSCRIPT_FILES:
        validate_file(ROOT / rel_path, findings)

    if not args.check_only:
        BUILD_DIR.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(build_manuscript(findings), encoding="utf-8")

    write_report(findings)

    errors = sum(f.level == "ERROR" for f in findings)
    warnings = sum(f.level == "WARN" for f in findings)
    print(f"Validación terminada: {errors} error(es), {warnings} advertencia(s).")
    print(f"Informe: {REPORT.relative_to(ROOT)}")
    if not args.check_only:
        print(f"Manuscrito: {OUTPUT.relative_to(ROOT)}")

    if errors:
        return 1
    if args.strict and warnings:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
