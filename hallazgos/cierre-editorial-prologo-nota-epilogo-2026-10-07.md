# ¿Qué se cerró en la etapa editorial posterior a P3?

**Fecha:** 7 de octubre de 2026  
**Base:** `main` después del PR #18.  
**Objetivo:** completar los elementos de apertura y cierre solicitados en la auditoría externa sin reabrir la conclusión documental.

## ¿Qué archivos nuevos se incorporaron?

- `capitulos/00-nota-al-lector.md`
- `capitulos/00-prologo.md`
- `capitulos/17-epilogo.md`
- `metodologia/ORDEN_MANUSCRITO.md`

## ¿Qué función cumple la Nota al lector?

Explica antes de comenzar:

- la diferencia entre establecido, probable, posible e indeterminado;
- hecho, interpretación e hipótesis;
- prioridad de fuentes primarias;
- regla de simetría;
- diferencias de peso entre evidencias;
- límites de alcance del libro;
- la regla de falsación: qué evidencia podría obligar a cambiar una conclusión.

No añade casos históricos ni argumentos nuevos.

## ¿Qué función cumple el Prólogo?

Plantea la pregunta humana e histórica: qué hacemos cuando alguien atribuye un mensaje a Dios. Evita dos extremos metodológicos —protección automática y acusación automática— y presenta las hipótesis de revelación, error sincero y fraude sin anticipar cuál terminará prefiriéndose.

No repite la reconstrucción documental de Atkinson del capítulo 1 ni adelanta la conclusión del capítulo 16.

## ¿Qué función cumple el Epílogo?

Trabaja las consecuencias intelectuales y personales del veredicto ya establecido en el capítulo 16. No agrega evidencia nueva. Distingue:

- utilidad de una idea y origen sobrenatural;
- sinceridad y autenticidad profética;
- error y fraude consciente;
- autoridad religiosa y criterio de prueba;
- incertidumbre razonada y ausencia de investigación.

La conclusión del capítulo 16 permanece intacta: pretensión profética no confirmada, preferencia moderada por una explicación humana sincera y falta de prueba suficiente para fraude consciente generalizado.

## ¿Por qué no se modificaron mecánicamente todos los títulos restantes?

P2 fijó `Elena G. de White` como grafía narrativa preferida. P3 aplicó esa convención en los capítulos que debían reescribirse de todos modos. Los capítulos C4–C8 y C15–C16 todavía contienen algunas grafías históricas de `Ellen G. White` en títulos o primeras menciones.

El conector disponible reemplaza archivos completos y no ofrece una operación segura de búsqueda/reemplazo parcial. Reescribir capítulos largos sólo para modificar una grafía aumentaría el riesgo editorial sin cambiar contenido. La normalización se reserva para la copia de producción, donde deberá ejecutarse con búsqueda/reemplazo controlado y revisión de diff, excluyendo citas, bibliografía, enlaces y nombres históricos.

## ¿Qué queda pendiente después de este cierre?

No queda pendiente investigación de los puntos P0–P3 como bloque de auditoría externa. Sí quedan tareas de **producción editorial**, distintas de la investigación:

1. normalización mecánica final de grafías, comillas y títulos en los capítulos no reescritos;
2. ensamblado del manuscrito completo según `ORDEN_MANUSCRITO.md`;
3. control automático de notas huérfanas, duplicadas y enlaces rotos sobre el manuscrito ensamblado;
4. maquetación de la edición de lectura y eventual creación de apéndices/bibliografía si se decide para publicación;
5. revisión final de estilo exclusivamente sobre la copia de producción, sin alterar grados de evidencia.

La investigación puede reabrirse si aparece nueva evidencia capaz de modificar materialmente un caso o la conclusión, pero ya no es necesario mantener el manuscrito en estado de revisión abierta para completar la estructura del libro.
