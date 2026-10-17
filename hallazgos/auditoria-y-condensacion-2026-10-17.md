# ¿Qué cambió en la auditoría y condensación del 17 de octubre de 2026?

El manuscrito se reescribió completo para que fuera corto y claro, sin cambiar los hechos, los grados de certeza ni la conclusión. Pasó de unas 79.000 palabras de cuerpo y 407 notas a unas 19.700 palabras y 202 notas. Además se incorporaron cinco objeciones de fondo que la versión anterior no respondía.

## ¿Qué se auditó?

- Lectura íntegra de los 19 archivos del manuscrito, con sus notas.
- Cotejo de 25 citas clave contra transcripciones o reproducciones en línea de los originales: [registro de cotejos](cotejo-citas-clave-2026-10-17.md). Todas coinciden; hay dos precisiones menores.
- Revisión del argumento del capítulo 16 desde el punto de vista de un lector adventista y de un lector crítico.

## ¿Qué objeciones de fondo se incorporaron?

| Objeción | Dónde se responde |
|---|---|
| El criterio aplicado al anuncio de 1856 también afectaría anuncios del Nuevo Testamento sobre la cercanía del fin (Marcos 13:30, 9:1; 1 Tesalonicenses 4:15) | Capítulo 2, §3; capítulo 7, §10; capítulo 16, §6 |
| Los autores bíblicos también escribieron con la ciencia de su época; ¿por qué no excusar igual el error médico de 1864? | Capítulo 12, §8; capítulo 16, §6 |
| El criterio de «menos suposiciones» favorece de entrada la explicación humana | Capítulo 16, §7 |
| El veredicto deja fuera 1844, el santuario y el juicio investigador, por lo que no contesta del todo la pregunta del título | Nota al lector; capítulo 16, §12 |
| La sinceridad tiene poco sustento positivo y falta una posición intermedia: núcleo sincero con episodios de autodefensa interesada | Capítulo 14, §9; capítulo 16, §10 |

Ninguna de las cinco cambió la conclusión, pero dos explican mejor por qué la confianza es moderada y no alta.

## ¿Qué se quitó y dónde está?

Se quitaron las cautelas repetidas, las secciones de autodefensa metodológica de cada capítulo, las tablas de trabajo (cronologías de testigos, matrices H1–H3, inventarios de pares), los casos de menor peso y el historial de cotejo dentro de las notas. Se conservaron todos los casos que inclinan el balance y todos los casos favorables con algún peso probatorio; de los favorables sólo se omitió una observación menor sobre la estricnina, que no distingue entre explicaciones.

La versión extensa completa está en el historial del repositorio, en el commit `4217d00`, y las fichas de investigación de `hallazgos/` siguen intactas. Nada se borró del expediente; sólo de la edición de lectura.

## ¿Qué precisiones dejó el cotejo?

- La cifra de «unos seis mil años» de *Spiritual Gifts* 3 está en pp. 91–92 según la paginación consultada; el capítulo 12 remite a pp. 90–93.
- La carta 267 de 1905 habla de ministros desatendidos «blancos y negros»; el capítulo 13 lo recoge.

## ¿Qué resultado dio la validación?

`scripts/manuscrito.py` terminó con 0 errores y 0 advertencias. Todos los títulos y subtítulos son preguntas y usan «Elena G. de White».

## ¿Qué corrigió la segunda revisión del mismo día?

Se volvió a leer la edición completa y se compararon todos sus números y fechas con la versión extensa. No aparecieron datos nuevos sin respaldo. Se corrigió lo siguiente:

- **Capítulo 16, §6:** la diferencia entre 1856 y Marcos 9:1 no está en que el anuncio de White nombre a un grupo de presentes (Marcos 9:1 también lo hace), sino en que el acontecimiento de 1856 no admite otra lectura que la segunda venida.
- **Capítulo 16, §10:** la atribución a Dios está documentada desde sus primeros escritos de 1845, no «desde los diecisiete años».
- **Capítulo 15, §7:** se restituyó que Prescott admitió que el problema podía no ser intencional.
- **Capítulo 3, §2:** la frase de 1906 se traduce como «no pretendo ser profetisa», más cerca del original.
- **Capítulo 7, §8:** se restituyó el pronóstico de 1855 sobre el grupo del *Messenger of Truth*, un caso favorable menor que se había omitido.

## ¿Qué cambió la revisión de lenguaje simple?

Se reescribió el cuerpo de los 19 archivos para que lo entienda cualquier lector:

- frases cortas, de una idea cada una: las oraciones de más de 30 palabras bajaron a unas 40 en todo el libro;
- palabras de todos los días en lugar de términos técnicos («decir que venía de Dios» por «atribución», «maneras normales de enterarse» por «vías ordinarias»), y explicación de los que quedan (mesmerismo, apnea, diezmo, transfiguración, juicio investigador);
- los cuatro grados de certeza pasaron a llamarse **probado, probable, posible y no se sabe** en todo el libro, también en las tablas de los capítulos 5 y 16;
- los títulos de los capítulos 10 y 14 se simplificaron («¿Qué significa para su inspiración que usara libros de otros?» y «¿Qué muestra la vida de Elena G. de White sobre si fue profeta?»); los nombres de archivo no cambiaron.

No se cambió ningún hecho, fecha, número ni grado de certeza. Las notas al pie quedaron idénticas: se comprobó con un script que las definiciones de notas de cada archivo coinciden línea por línea con la versión anterior. El cuerpo creció de unas 19.700 a unas 22.500 palabras, porque explicar con palabras simples a veces lleva más palabras. La validación terminó con 0 errores y 0 advertencias.

## ¿Qué se tomó de la auditoría externa de ChatGPT?

Se revisó una auditoría externa del repositorio (commit `00eb25c`). Se aplicó lo que mejoraba la precisión o el alcance:

- **Conclusión más estrecha.** Ya no dice «experiencias de origen humano», que afirma más de lo que muestran los documentos sobre la causa de las visiones. Ahora dice que creyó sinceramente que sus mensajes venían de Dios, pero que, en los casos estudiados, lo que decían salió de fuentes humanas, y que la causa de las visiones mismas no se sabe. Cambio aplicado en la Nota, el capítulo 16, el epílogo, el README y `ESTADO_ACTUAL.md`.
- **Alcance provisional.** La Nota, el capítulo 16 y el README dicen que la respuesta evalúa lo que se puede comprobar con documentos históricos y que es provisional mientras falte el examen doctrinal.
- **Criterios de la propia iglesia.** Nueva sección 4 del capítulo 16: aplica las cuatro pruebas que presenta el White Estate (Isaías 8:20, Deuteronomio 18, 1 Juan 4, Mateo 7) y señala que una condicionalidad sin límite haría que la prueba de los anuncios no pudiera fallar.
- **Veltman.** «Eran propias» pasó a «no se encontró parecido con los libros revisados», con la aclaración de que eso no prueba originalidad.
- **Krummacher.** «Probado» queda limitado a la dependencia del texto; no hay constancia de lectura directa, como ya decía `capitulo-10-diario-1890-y-krummacher.md`.
- **Respiración.** Se distinguió a personas sin entrenamiento (decenas de segundos) de personas entrenadas (pocos minutos).
- **Prólogo.** Se resolvió la tensión con la Nota: la respuesta se adelanta, pero tiene que sostenerse capítulo a capítulo.
- **Validación.** El script y el workflow la llaman «estructural»; se quitó del workflow el paso que modificaba el capítulo 7 antes de validar.
- **Terminología.** `MATRIZ_CRITERIOS_BIBLICOS.md` usa probado, probable, posible y no se sabe; `ESTADO_ACTUAL.md` tiene el conteo de palabras actualizado.

No se aplicó:

- **Quitar la respuesta de la Nota al lector.** Fue una decisión editorial del autor («al grano»).
- **Afirmar que *Elijah the Tishbite* estaba en la biblioteca de White.** No se pudo verificar.
- **Investigar ahora la doctrina, la edad de la Tierra, el inventario completo de casos descartados y una auditoría nueva de las notas.** Quedan como trabajo pendiente para pasar de una respuesta provisional a una global.

## ¿Qué se tomó de la segunda auditoría externa?

Sobre el commit `8343886`:

- **1856 baja un escalón.** El caso de Ezequías (2 Reyes 20; Isaías 38) muestra que en la Biblia un anuncio sin condición escrita puede cambiar sin que el profeta quede como falso. Los capítulos 2, 7 y 16 dicen ahora que 1856 es un problema serio, pero no una refutación cerrada. La diferencia que se mantiene: en la Biblia el cambio se cuenta en el momento, con su razón, y en 1856 la explicación llegó años después.
- **1864 pasa a ser el caso más fuerte.** No admite la salida de la condicionalidad. Cambio aplicado en los capítulos 12 y 16.
- **La conclusión separa lo demostrado de lo que encaja mejor.** En varios casos se puede mostrar que el contenido salió de libros o de ideas de la época (March, Wylie, Krummacher, medicina de 1864). En otros, como Faulkhead, Salamanca o las primeras visiones, una explicación humana encaja mejor sin que se pueda reconstruir la fuente.
- **Criterios oficiales.** El capítulo 16, §4, usa ahora las cinco pruebas de la página oficial de Adventist.org, además de las del White Estate. Entre ellas está «si habla del futuro, no debe haber lugar para el error» (Jeremías 28:9).

No se aplicó:

- **La edad de la Tierra.** Su exclusión fue una decisión previa del autor («opción B»). La auditoría la critica como una asimetría que favorece a White; queda para que el autor la reconsidere.
- **El inventario completo de casos y el cotejo de las 204 notas.** Siguen pendientes en `ESTADO_ACTUAL.md`.
