# ¿Qué muestra la auditoría final de producción del manuscrito?

**Fecha:** 7 de octubre de 2026  
**Base:** `main` después de los PR #18–#21.  
**Objeto:** medir la edición de lectura ensamblada y decidir si hace falta otra reducción sustantiva antes de maquetar.

## ¿Qué versión se midió?

Se midió `build/manuscrito-completo.md`, generado automáticamente por `scripts/manuscrito.py` en GitHub Actions.

El orden es:

1. Nota al lector;
2. Prólogo;
3. capítulos 1–16;
4. Epílogo.

La edición generada conserva el contenido documental de los capítulos, vuelve únicos los identificadores de notas, retira enlaces internos del repositorio y normaliza en los encabezados la forma narrativa `Elena G. de White`.

## ¿Cuántas palabras tiene la edición de lectura?

El recuento aproximado, separando las definiciones de notas al pie, es:

| Componente | Palabras aproximadas |
|---|---:|
| Capítulos 1–16, sin definiciones de notas | **79.027** |
| Nota al lector | 1.014 |
| Prólogo | 1.257 |
| Epílogo | 1.292 |
| Cuerpo completo con paratextos, sin definiciones de notas | **82.590** |
| Definiciones de notas | **23.610** |
| Archivo Markdown completo, incluidas notas | **106.200** |

El conteo usa tokenización por palabras y debe entenderse como métrica editorial, no como conteo contractual de una plataforma de impresión.

## ¿Cómo se compara con la auditoría externa?

La auditoría externa había estimado unas **96.000 palabras** para el manuscrito anterior y propuso como objetivo orientativo reducir el cuerpo a unas 70.000–75.000.

La edición actual de los dieciséis capítulos queda cerca de **79.000 palabras**, es decir, unas **17.000 menos** que aquella estimación, a pesar de haber incorporado después nueva evidencia P1: puerta cerrada de 1849, cuadro de 1843, patrón estudio→visión, autoridad institucional, casos de *The Living Temple* y «the daily», y bibliografía/contexto adicionales.

Por eso no se recomienda perseguir de manera mecánica el rango 70.000–75.000. Alcanzarlo exigiría retirar entre unas 4.000 y 9.000 palabras adicionales de capítulos donde buena parte de la extensión corresponde a reconstrucciones probatorias y límites documentales. El objetivo editorial era eliminar repetición y teoría innecesaria, no reducir evidencia.

## ¿Qué capítulos siguen siendo los más extensos?

Los mayores bloques de cuerpo son, aproximadamente:

| Capítulo | Palabras de cuerpo |
|---|---:|
| C4 — primeras visiones | 8.269 |
| C13 — contradicciones | 7.068 |
| C16 — síntesis final | 6.750 |
| C12 — historia, ciencia y salud | 6.546 |
| C5 — fenómenos físicos | 6.314 |

Su extensión responde principalmente a multiplicidad de documentos, variantes, testigos o casos. No se recomienda un nuevo recorte global sin identificar antes una repetición concreta que pueda eliminarse sin perder una distinción probatoria.

## ¿Qué pasó con las repeticiones señaladas por Claude?

En el **cuerpo** ensamblado, sin contar definiciones de notas, aparecen aproximadamente:

| Expresión | Auditoría externa anterior | Edición actual |
|---|---:|---:|
| `pendiente*` | 121 | **9** |
| `Tampoco` | 171 | **91** |
| `por sí solo/a` | 87 | **69** |
| `no demuestra` | 72 | **80** |
| `establecid*` | 82 | **86** |
| `indeterminad*` | 47 | **69** |
| `cotejad*` | ~35 | **5** |

Los descensos fuertes en `pendiente`, `Tampoco` y `cotejad*` muestran que se retiró buena parte del lenguaje de expediente interno. `No demuestra`, `establecido` e `indeterminado` no descendieron porque también se incorporaron nuevos casos y porque esas expresiones siguen cumpliendo una función metodológica real.

No se recomienda reducirlas por simple conteo. Sí deben revisarse en una futura corrección de estilo si aparecen varias veces dentro del mismo párrafo o sección sin añadir una distinción nueva.

## ¿Quedaron rastros internos en la edición de lectura?

La validación automática final pasó con **0 errores**.

En el archivo ensamblado no quedaron las cadenas controladas:

- `../hallazgos/`;
- `../metodologia/`;
- `PDF aportado`;
- `EPUB proporcionado`;
- `No inventar paginación`;
- nombres de ramas de revisión P1;
- `segunda ronda P1`.

Las advertencias que siguen apareciendo en el informe pertenecen a los **archivos fuente de investigación**, donde se conserva deliberadamente trazabilidad interna. La edición de lectura las normaliza al generarse.

## ¿Qué controla automáticamente el proceso de producción?

El script comprueba, entre otras cosas:

- que existan los 19 archivos que forman el manuscrito;
- que toda nota referenciada tenga definición;
- que no existan definiciones duplicadas;
- que los enlaces locales apunten a archivos existentes;
- que los encabezados sean preguntas;
- que la edición de lectura no conserve marcas internas controladas;
- que los encabezados de la edición de lectura no mantengan la grafía inglesa de White.

Además, al ensamblar, renombra internamente las notas de cada capítulo para evitar colisiones de identificadores entre archivos.

## ¿Cuál es la decisión editorial final sobre la extensión?

**No hacer otra reducción global por cuota de palabras.**

La siguiente intervención sobre el texto, si se realiza, debe ser una corrección de lectura frase por frase: eliminar sólo redundancias identificables, prosa rígida o una cautela repetida inmediatamente. No debe reabrir el alcance de los capítulos ni eliminar documentación para alcanzar un número arbitrario.

La edición está suficientemente estabilizada para pasar a una fase distinta: **maquetación y producción de archivos de lectura/publicación**, manteniendo la edición de investigación como fuente trazable.
