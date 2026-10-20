#!/usr/bin/env python3
"""Genera una edición completa en Markdown para escuchar en ElevenReader.

Incluye nota al lector, prólogo, capítulos 1–16 y epílogo.
No incluye marcas de notas ni bibliografía: ambas permanecen en el
manuscrito fuente, preparado para la futura edición de lectura.
Convierte citas bíblicas a una forma que suena natural al leerlas.
Uso: python3 scripts/edicion_audio.py
Salida: ediciones/libro-para-escuchar.md y su copia .txt
"""
from __future__ import annotations

import re
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
CAPITULOS = RAIZ / "capitulos"
SALIDA = RAIZ / "ediciones" / "libro-para-escuchar.md"
SALIDA_TXT = SALIDA.with_suffix(".txt")

TITULO = "¿Reúne Elena G. de White las credenciales necesarias para ser considerada una profeta auténtica?"
AUTOR = "Nicolás Bertoa"

LIBROS_NUMERADOS = {
    "1 Juan": "Primera de Juan", "2 Juan": "Segunda de Juan",
    "1 Corintios": "Primera de Corintios", "2 Corintios": "Segunda de Corintios",
    "1 Tesalonicenses": "Primera de Tesalonicenses",
    "2 Tesalonicenses": "Segunda de Tesalonicenses",
    "1 Timoteo": "Primera de Timoteo", "2 Timoteo": "Segunda de Timoteo",
    "1 Pedro": "Primera de Pedro", "2 Pedro": "Segunda de Pedro",
    "1 Samuel": "Primero de Samuel", "2 Samuel": "Segundo de Samuel",
    "1 Reyes": "Primero de Reyes", "2 Reyes": "Segundo de Reyes",
    "1 Crónicas": "Primero de Crónicas", "2 Crónicas": "Segundo de Crónicas",
    "2 Esdras": "Segundo de Esdras", "1 Enoc": "Primero de Enoc",
}


def limpiar_notas(texto: str) -> str:
    """Saca las definiciones de notas y sus llamadas del cuerpo de escucha."""
    sin_definiciones = [
        linea for linea in texto.splitlines()
        if not re.match(r"^\[\^\d+\]:", linea)
    ]
    return re.sub(r"\[\^\d+\]", "", "\n".join(sin_definiciones))


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
        if (lineas[i].startswith("|") and i + 1 < len(lineas)
                and re.match(r"^\|[-| :]+\|$", lineas[i + 1])):
            i += 2
            while i < len(lineas) and lineas[i].startswith("|"):
                celdas = [c.strip().replace("**", "")
                          for c in lineas[i].strip("|").split("|")]
                if len(celdas) >= 2:
                    valor = celdas[1].rstrip(".")
                    salida.append(f"- {celdas[0]}: {valor[:1].lower() + valor[1:]}.")
                i += 1
            continue
        salida.append(lineas[i])
        i += 1
    return "\n".join(salida)


def a_texto_plano(texto: str) -> str:
    """Quita la marca de Markdown para la copia .txt que importa ElevenReader."""
    texto = re.sub(r"^#+ ", "", texto, flags=re.M)
    texto = re.sub(r"^> ", "", texto, flags=re.M)
    return texto.replace("**", "").replace("*", "")


def main() -> None:
    archivos = sorted(CAPITULOS.glob("*.md"))
    assert len(archivos) == 19, f"Se esperaban 19 archivos: {len(archivos)}"
    partes = [f"# {TITULO}\n\n{AUTOR}"]
    for archivo in archivos:
        cuerpo = limpiar_notas(archivo.read_text(encoding="utf-8"))
        cuerpo = quitar_enlaces(cuerpo)
        cuerpo = tablas_a_frases(cuerpo)
        cuerpo = versiculos(cuerpo)
        partes.append(cuerpo.strip())
    texto = "\n\n".join(partes).rstrip() + "\n"
    texto = re.sub(r"\n{3,}", "\n\n", texto)
    assert "[^" not in texto, "Quedaron referencias a notas en la edición de audio"
    assert "# Notas" not in texto, "Quedó la bibliografía en la edición de audio"
    assert "Esta es mi conclusión hasta ahora." in texto, "Falta el cierre aprobado"
    SALIDA.parent.mkdir(exist_ok=True)
    SALIDA.write_text(texto, encoding="utf-8")
    SALIDA_TXT.write_text(a_texto_plano(texto), encoding="utf-8")
    print(f"Edición para escuchar: {SALIDA.relative_to(RAIZ)} ({len(texto.split())} palabras)")


if __name__ == "__main__":
    main()
