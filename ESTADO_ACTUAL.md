# ¿Cuál es el estado actual del libro?

**Actualizado:** 7 de octubre de 2026.

El proyecto ya completó la revisión externa organizada en prioridades **P0–P3**, incorporó la evidencia adicional verificada, realizó la pasada de estructura/estilo, limpió el aparato crítico de la edición de lectura y añadió los paratextos necesarios para cerrar el libro.

## ¿Qué está terminado?

- **Nota al lector** terminada.
- **Prólogo** terminado.
- **Capítulos 1–16** escritos y revisados.
- **Epílogo** terminado.
- **P0** integrado: alcance doctrinal/geocronológico, dicotomía de White, rendición frente a la matriz, Deuteronomio 18 y expansión de C16.
- **P1** integrado: puerta cerrada 1849, cuadro de 1843, patrón estudio→visión, Salamanca, predicciones abiertas, base bíblica adventista del don, autoridad institucional y casos adicionales verificados.
- **P2** integrado: arranque más rápido, reducción de C1/C2, mejora de prosa y guía de estilo.
- **P3** integrado: limpieza de notas en los capítulos revisados, eliminación de marcas internas de la edición de lectura y normalización del aparato.
- **Edición de lectura automática** disponible mediante GitHub Actions.
- **Validación automática** de notas, enlaces, encabezados y marcas internas.

## ¿Cuál es la conclusión vigente?

La conclusión del capítulo 16 no cambió durante la fase de producción:

> **Con la evidencia hoy disponible, no quedó suficientemente demostrado que Elena G. de White reuniera las credenciales necesarias para considerarla una profeta auténtica. La explicación mejor apoyada es, con confianza moderada, la de experiencias religiosas de origen humano interpretadas sinceramente como revelaciones.**

El origen profético sigue siendo posible, pero no es la explicación mejor respaldada por el expediente examinado. El fraude consciente generalizado recibe menos apoyo todavía.

El veredicto es explícitamente parcial respecto de la comparación doctrinal: no incluye una investigación exhaustiva de 1844, santuario y juicio investigador. También declara el costo de no desarrollar una evaluación completa de la geocronología.

## ¿Qué archivos forman el libro?

El orden editorial vigente está en [`metodologia/ORDEN_MANUSCRITO.md`](metodologia/ORDEN_MANUSCRITO.md):

**Nota al lector → Prólogo → C1–C16 → Epílogo.**

La estructura metodológica sigue siendo de **16 capítulos**. Nota, prólogo y epílogo son paratextos.

## ¿Qué diferencia hay entre edición de investigación y edición de lectura?

Los archivos dentro de `capitulos/` conservan parte de la trazabilidad necesaria para investigación: referencias internas, historial de verificaciones y algunas grafías históricas.

La **edición de lectura** se genera automáticamente con `scripts/manuscrito.py`. Durante ese proceso:

- se ensamblan los 19 archivos en orden;
- se vuelven únicos los identificadores de notas al pie;
- se eliminan enlaces internos del repositorio que no pertenecen al libro impreso;
- se normaliza `Elena G. de White` en encabezados;
- se reemplazan marcas editoriales internas conocidas por referencias legibles;
- se valida que no queden errores estructurales.

El workflow está en `.github/workflows/validar-manuscrito.yml`.

## ¿Qué resultado dio la validación final?

La edición de lectura pasó con **0 errores**.

Los dieciséis capítulos contienen aproximadamente **79.000 palabras de cuerpo**. Con Nota al lector, Prólogo y Epílogo, el cuerpo completo queda alrededor de **82.600 palabras**, sin contar las definiciones de notas. La auditoría de producción explica por qué no se recomienda otra reducción global por cuota de palabras.

Véase [`hallazgos/auditoria-produccion-final-2026-10-07.md`](hallazgos/auditoria-produccion-final-2026-10-07.md).

## ¿Qué queda por hacer?

La investigación principal y la revisión P0–P3 están cerradas. Lo que queda pertenece a **producción editorial**:

1. elegir el formato final de publicación;
2. generar la edición maquetada a partir del manuscrito validado;
3. revisar visualmente notas, saltos, tablas y jerarquía de títulos;
4. preparar los archivos finales de distribución/publicación;
5. reabrir investigación sólo si aparece nueva evidencia capaz de modificar materialmente un caso o la conclusión.

El manuscrito ya no necesita permanecer en estado de revisión estructural abierta para avanzar a producción.
