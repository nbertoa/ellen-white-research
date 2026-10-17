#!/usr/bin/env python3
"""Genera una edición en Markdown pensada para escucharse (ElevenReader).

- Las llamadas a notas quedan como números volados (¹, ², ³) y las notas
  van todas juntas al final del libro, sin direcciones web.
- Las tablas se convierten en frases.
- Las citas bíblicas se escriben como se leen en voz alta.

Uso: python3 scripts/edicion_audio.py
Salida: ediciones/libro-para-escuchar.md
"""
from __future__ import annotations

import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CAPITULOS = RAIZ / "capitulos"
SALIDA = RAIZ / "ediciones" / "libro-para-escuchar.md"

TITULO = "¿Reúne Elena G. de White las credenciales necesarias para ser considerada una profeta auténtica?"
AUTOR = "Nicolás Bertoa"

VOLADOS = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")

LIBROS_NUMERADOS = {
    "1 Juan": "Primera de Juan",
    "2 Juan": "Segunda de Juan",
    "1 Corintios": "Primera de Corintios",
    "2 Corintios": "Segunda de Corintios",
    "1 Tesalonicenses": "Primera de Tesalonicenses",
    "2 Tesalonicenses": "Segunda de Tesalonicenses",
    "1 Timoteo": "Primera de Timoteo",
    "2 Timoteo": "Segunda de Timoteo",
    "1 Pedro": "Primera de Pedro",
    "2 Pedro": "Segunda de Pedro",
    "1 Samuel": "Primero de Samuel",
    "2 Samuel": "Segundo de Samuel",
    "1 Reyes": "Primero de Reyes",
    "2 Reyes": "Segundo de Reyes",
    "1 Crónicas": "Primero de Crónicas",
    "2 Crónicas": "Segundo de Crónicas",
    "2 Esdras": "Segundo de Esdras",
    "1 Enoc": "Primero de Enoc",
}


def separar(texto: str) -> tuple[str, dict[str, str]]:
    """Devuelve el cuerpo sin definiciones de notas y un diccionario de notas."""
    notas: dict[str, str] = {}
    cuerpo: list[str] = []
    for linea in texto.splitlines():
        m = re.match(r"\[\^(\d+)\]:\s*(.*)", linea)
        if m:
            notas[m.group(1)] = m.group(2)
        else:
            cuerpo.append(linea)
    return "\n".join(cuerpo).rstrip() + "\n", notas


def quitar_enlaces(texto: str) -> str:
    return re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", texto)


def versiculos(texto: str) -> str:
    def leer(m: re.Match) -> str:
        cap, v1, v2 = m.group(1), m.group(2), m.group(3)
        if v2:
            return f"capítulo {cap}, versículos {v1} al {v2}"
        return f"capítulo {cap}, versículo {v1}"

    texto = re.sub(r"\b(\d+):(\d+)(?:[-–](\d+))?\b", leer, texto)
    for corto, largo in LIBROS_NUMERADOS.items():
        texto = re.sub(rf"(?<![\w]){re.escape(corto)}\b", largo, texto)
    return texto


def tablas_a_frases(texto: str) -> str:
    salida: list[str] = []
    lineas = texto.splitlines()
    i = 0
    while i < len(lineas):
        if lineas[i].startswith("|") and i + 1 < len(lineas) and re.match(r"^\|[-| :]+\|$", lineas[i + 1]):
            i += 2  # se omiten encabezado y separador
            while i < len(lineas) and lineas[i].startswith("|"):
                celdas = [c.strip().replace("**", "") for c in lineas[i].strip("|").split("|")]
                if len(celdas) >= 2:
                    valor = celdas[1].rstrip(".")
                    salida.append(f"- {celdas[0]}: {valor[:1].lower() + valor[1:]}.")
                i += 1
            continue
        salida.append(lineas[i])
        i += 1
    return "\n".join(salida)


def llamadas(texto: str) -> str:
    return re.sub(r"\[\^(\d+)\]", lambda m: m.group(1).translate(VOLADOS), texto)


def titulo_capitulo(cuerpo: str) -> str:
    primera = cuerpo.splitlines()[0]
    return primera.lstrip("# ").strip()


def main() -> None:
    archivos = sorted(CAPITULOS.glob("*.md"))
    partes = [f"# {TITULO}\n\n{AUTOR}\n"]
    bloque_notas = ["# Notas", "Estas son las referencias de cada capítulo, para quien quiera consultar las fuentes. No hace falta escucharlas para seguir el libro."]
    for archivo in archivos:
        cuerpo, notas = separar(archivo.read_text(encoding="utf-8"))
        cuerpo = quitar_enlaces(cuerpo)
        cuerpo = tablas_a_frases(cuerpo)
        cuerpo = versiculos(cuerpo)
        cuerpo = llamadas(cuerpo)
        partes.append(cuerpo)
        if notas:
            bloque_notas.append(f"## {titulo_capitulo(cuerpo)}")
            for numero in sorted(notas, key=int):
                bloque_notas.append(f"{numero}. {quitar_enlaces(notas[numero])}")
            bloque_notas.append("")
    texto = "\n\n".join(p.strip() for p in partes) + "\n\n" + "\n\n".join(bloque_notas).strip() + "\n"
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    SALIDA.parent.mkdir(exist_ok=True)
    SALIDA.write_text(texto, encoding="utf-8")
    print(f"Edición para escuchar: {SALIDA.relative_to(RAIZ)} ({len(texto.split())} palabras)")


if __name__ == "__main__":
    main()
