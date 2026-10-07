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
HEX_TOKEN_RE = re.compile(r"\b[0-9a-f]{12,40}\b")

# Marcadores de proceso que sí son inequívocamente internos. No se marca la
# palabra genérica "expediente" o "ficha" porque puede aparecer legítimamente
# en la prosa histórica.
INTERNAL_MARKERS = [
    re.compile(r"\.\./hallazgos/", re.I),
    re.compile(r"\.\./metodologia/", re.I),
    re.compile(r"\bexpediente\s+(?:P\d|C\d|[A-Z]/[A-Z]|espec[ií]fico)", re.I),
    re.compile(r"\bficha\s+(?:C\d|P\d|sanitaria|educativa|social|organizativa|de recepci[oó]n|de autoridad)", re.I),
    re.compile(r"\bmatriz vigente\b", re.I),
    re.compile(r"PDF aportado", re.I),
    re.compile(r"EPUB proporcionado", re.I),
    re.compile(r"no se cotej[oó] aqu[ií]", re.I),
    re.compile(r"no inventar paginaci[oó]n", re.I),
    re.compile(r"revision-p\d-[\w-]+", re.I),
    re.compile(r"segunda ronda P1", re.I),
]

# La edición de investigación conserva trazabilidad. La edición de lectura
# elimina marcas internas conocidas sin modificar hechos, fuentes ni grados de
# evidencia. Estas sustituciones se aplican únicamente al archivo generado.
READING_REPLACEMENTS = {
    "Inventario y matriz, auditoría y registro de fuentes: existencia, papel, certeza causal, valor y falsación.":
        "Véase el capítulo 2 para los criterios de existencia del efecto, papel de White, certeza causal, valor probatorio y falsación.",
    "Distinguir experiencia, comunicación y edición. Ficha sanitaria.":
        "La referencia permite distinguir experiencia, comunicación y edición.",
    "Métodos y discusión. La ficha identifica comparación, variables y selección; terapia hormonal es variable histórica, no consejo actual.":
        "Métodos y discusión. El estudio informa comparación, variables y selección; la terapia hormonal aparece como variable histórica, no como consejo actual.",
    "Ficha educativa distingue cartas de historia y aprendizaje no medido.":
        "Las cartas documentan decisiones educativas; no miden por sí solas el aprendizaje.",
    "La ficha registra inconsistencia aritmética en otra valuación y evita sumar dinero cobrado/prometido.":
        "Otra valuación presenta una inconsistencia aritmética, por lo que aquí no se suman dinero cobrado y prometido.",
    "Correlación y autorreporte. Ficha de recepción.":
        "Son correlaciones basadas en autorreporte.",
    "Ficha organizativa.": "",
    "Rea, *The White Lie* (1982), C2 pp. 39–43, PDF aportado; Douglass, *Messenger of the Lord* (1998/EPUB 2013), recepción y C38 sobre 1919. Mapas críticos/favorables; no encuestas independientes. No inventar paginación del EPUB.":
        "Walter T. Rea, *The White Lie* (1982), cap. 2, pp. 39–43; Herbert E. Douglass, *Messenger of the Lord* (1998; edición digital de 2013), especialmente el capítulo 38 sobre 1919. Se usan para reconstruir argumentos críticos y favorables, no como encuestas independientes.",
    "Ficha social.": "",
    "Ficha de autoridad.": "",
    "ficha C13.": "véase el capítulo 13.",
    "ficha Rochester/Daniels.": "véase el capítulo 8.",
    "Capítulo 15, inventario y matriz y auditoría.": "Capítulo 15.",
    " y ficha de masturbación y afirmaciones médicas.": ".",
    "Cotejos y límites en C10 §§8–10, fichas de juicio y March, diario y Krummacher y Queensland/Humphrey.":
        "Cotejos y límites en C10 §§8–10.",
    "Capítulos 4–6, 5 y 6; ficha de visiones tempranas.":
        "Capítulos 4–6.",
    "C9, C10, C11; declaraciones y cronología, atribución y prácticas editoriales y colaboradores.":
        "Capítulos 9–11.",
    "Capítulo 13, especialmente §28; inventario y protocolo.":
        "Capítulo 13, especialmente §28.",
    "Capítulo 14, especialmente §§2–3 y 12–13; expedientes sobre dinero, diezmo y autoridad, y auditoría documental.":
        "Capítulo 14, especialmente §§2–3 y 12–13.",
    "; análisis, fuentes y límites en C7 y expediente P1.":
        "; análisis, fuentes y límites en C7.",
    "; reconstrucción y problema del referente en C4, C13 y expediente P1.":
        "; reconstrucción y problema del referente en C4 y C13.",
    "Véanse C6 y expediente específico.": "Véase C6.",
    "; análisis de alcance en C14 y segunda ronda P1.": "; análisis de alcance en C14.",
    "; fuentes y cautelas en C15 y segunda ronda P1.": "; fuentes y cautelas en C15.",
}


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


def looks_like_git_hash(token: str) -> bool:
    # Evita marcar ISBN, DOI y otros identificadores numéricos como hashes.
    return any(c in "abcdef" for c in token.lower()) and any(c.isdigit() for c in token)


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
        if "¿" not in heading or "?" not in heading:
            findings.append(
                Finding(
                    "WARN",
                    name,
                    f"encabezado no formulado como pregunta en línea {line_number(text, match.start())}: {heading}",
                )
            )

    # Rastros internos inequívocos.
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
    for match in HEX_TOKEN_RE.finditer(text):
        token = match.group(0)
        if not looks_like_git_hash(token):
            continue
        findings.append(
            Finding(
                "WARN",
                name,
                f"posible hash de git en línea {line_number(text, match.start())}: {token}",
            )
        )

    # Normalización editorial pendiente en la edición de investigación.
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


def normalize_reading_copy(text: str) -> str:
    """Aplica sólo a la edición generada las decisiones editoriales P2–P3."""
    # En encabezados, usar la forma castellana sin tocar citas o bibliografía.
    def normalize_heading(match: re.Match[str]) -> str:
        hashes, heading = match.groups()
        heading = re.sub(r"\bEllen G\. White\b", "Elena G. de White", heading)
        heading = re.sub(r"\bEllen White\b", "Elena G. de White", heading)
        return f"{hashes} {heading}"

    text = HEADING_RE.sub(normalize_heading, text)
    for old, new in READING_REPLACEMENTS.items():
        text = text.replace(old, new)
    # Limpieza tipográfica mínima causada por sustituciones vacías.
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r" {2,}", " ", text)
    return text


def validate_reading_copy(text: str, findings: list[Finding]) -> None:
    # La edición de lectura no debe exponer rutas ni marcas de auditoría.
    reading_markers = [
        r"\.\./hallazgos/",
        r"\.\./metodologia/",
        r"PDF aportado",
        r"EPUB proporcionado",
        r"no inventar paginaci[oó]n",
        r"revision-p\d-[\w-]+",
        r"segunda ronda P1",
        r"\bficha\s+(?:C\d|P\d|sanitaria|educativa|social|organizativa|de recepci[oó]n|de autoridad)",
        r"\bexpediente\s+(?:P\d|C\d|espec[ií]fico)",
    ]
    for raw in reading_markers:
        pattern = re.compile(raw, re.I)
        for match in pattern.finditer(text):
            findings.append(
                Finding(
                    "ERROR",
                    "build/manuscrito-completo.md",
                    f"marca interna sobrevivió a la edición de lectura: {match.group(0)!r}",
                )
            )

    for match in re.finditer(r"(?m)^#{1,6} .*\bEllen(?: G\.)? White\b", text):
        findings.append(
            Finding(
                "ERROR",
                "build/manuscrito-completo.md",
                f"grafía inglesa sobrevivió en encabezado: línea {line_number(text, match.start())}",
            )
        )


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
        text = normalize_reading_copy(text)
        parts.append(text)
    manuscript = "\n\n---\n\n".join(parts).rstrip() + "\n"
    validate_reading_copy(manuscript, findings)
    return manuscript


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
        manuscript = build_manuscript(findings)
        OUTPUT.write_text(manuscript, encoding="utf-8")

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
