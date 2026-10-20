# ¿Reúne Ellen G. White las credenciales necesarias para ser considerada una profeta auténtica?

Repositorio de investigación del libro cuya pregunta central es:

> **¿Reúne Elena G. de White las credenciales necesarias para ser considerada una profeta auténtica?**

La respuesta del capítulo 16 es personal y provisional: el autor no encuentra fundamentos suficientes para afirmar con seguridad que Elena G. de White haya sido una profeta auténtica, pero tampoco considera demostrado que definitivamente no lo fuera. La explicación que hoy le parece más probable es que ella creyera sinceramente recibir mensajes de Dios, aunque al menos algunos parecen haber tenido origen humano. La investigación se limita a los casos y documentos efectivamente examinados.

## ¿Cómo se organiza el repositorio?

- `capitulos/`: manuscrito del libro (edición condensada y en lenguaje sencillo, unas 23.200 palabras de cuerpo).
- `hallazgos/`: fichas de investigación, auditorías y cotejos, con todo el detalle que el manuscrito resume.
- `metodologia/`: criterios, orden del manuscrito y guía de estilo.
- `ediciones/libro-para-escuchar.md`: libro completo para escuchar, sin llamadas a notas ni bibliografía final, con citas bíblicas pronunciables. Se regenera con `python3 scripts/edicion_audio.py`. Para importarlo directamente en ElevenReader está también `ediciones/libro-para-escuchar.txt`.
- `scripts/manuscrito.py`: ensambla la edición de lectura y hace una validación estructural (notas, enlaces, títulos). No comprueba citas, fechas ni razonamientos: eso lo hacen los cotejos de `hallazgos/`.

## ¿Cómo se investiga?

Para cada cuestión importante:

1. identificar exactamente qué se afirma;
2. buscar fuentes primarias;
3. reconstruir fecha, contexto y destinatario;
4. buscar el mejor argumento a favor y la mejor objeción;
5. determinar qué queda demostrado;
6. distinguir entre probado, probable, posible y no se sabe.

Pregunta de control: **¿qué evidencia podría demostrar que esta conclusión está equivocada?**

## ¿Qué fuentes tienen prioridad?

1. Cartas, manuscritos, diarios, primeras ediciones y documentos contemporáneos.
2. Archivos y colecciones documentales.
3. Investigación académica.
4. Obras apologéticas y críticas: Walter Rea para localizar las críticas, Herbert E. Douglass para reconstruir la defensa adventista.

## ¿Cómo se escribe el libro?

Investigación profunda detrás de una lectura sencilla. Frases cortas, palabras de todos los días y cada término técnico explicado. Cada capítulo responde su pregunta en el primer párrafo, presenta sólo los casos que pesan y dice cada cautela una vez. Todos los títulos y subtítulos son preguntas. La regla de simetría exige la misma prueba a favor y en contra, también cuando el criterio se aplica a la Biblia.

## ¿Qué contiene cada capítulo?

| Capítulo | Respuesta breve |
|---|---|
| 1. Definiciones | Una visión o una impresión no prueban por sí solas una revelación; usar fuentes no refuta la inspiración. |
| 2. Credenciales | Criterios bíblicos: contenido, predicciones, condicionalidad, origen, frutos e interés. Valen también para la Biblia. |
| 3. Lo que ella decía | Que Dios le daba mensajes, que los contaba con sus palabras, que había que obedecerlos, que no era infalible y que la Biblia estaba primero. |
| 4. Primeras visiones | En público desde 1845; lo central se mantuvo, pero se borraron frases; hasta 1849 se usaron para sostener la puerta cerrada. |
| 5. Lo que pasaba en el cuerpo | Un trance es probable; no está probado que dejara de respirar por mucho tiempo ni que tuviera fuerza sobrehumana. |
| 6. Explicaciones | Un trance religioso explica cómo se veían; no quedan probados ni la epilepsia, ni el fraude, ni que vinieran de Dios. |
| 7. Predicciones | Dos advertencias a su favor; el anuncio de 1856 no se cumplió y es un problema serio, aunque no cerrado (caso de Ezequías). |
| 8. Cosas que no podía saber | Faulkhead y Salamanca siguen siendo interesantes; en ningún caso se descarta que alguien le contara. |
| 9. Libros de otros | Probado que los usó (Conybeare y Howson, Wylie, 31,4 % de las unidades en la muestra de Veltman). |
| 10. Libros de otros e inspiración | Usarlos para historia encaja con lo que ella dijo; en 1879 y 1890 es posible que presentara como de Dios palabras de un libro. |
| 11. Quién escribió | Los textos de base son suyos; la forma y el orden, con mucha ayuda; los libros de extractos posteriores a 1915 no los aprobó ella. |
| 12. Errores | Errores de historia corregidos, una explicación equivocada de los volcanes y un error médico de 1864 presentado como mostrado por Dios. |
| 13. Contradicciones | Cambió consejos; quedan cuatro choques sin resolver, pero no dos revelaciones contrarias. |
| 14. Su vida | No hay pruebas de que se hiciera rica; el problema es cómo usó su autoridad. |
| 15. Frutos | Salud, educación y misión reales; costaba mucho reconocer sus errores en público. |
| 16. Conclusión | En primera persona: la evidencia no permite afirmar con seguridad que fuera profeta, pero tampoco descarta definitivamente esa posibilidad. La explicación humana sincera tiene más apoyo y la conclusión sigue abierta a revisión. |

## ¿Cuál es el estado actual?

Véase [`ESTADO_ACTUAL.md`](ESTADO_ACTUAL.md). La última revisión, del 17 de octubre de 2026, condensó el manuscrito, cotejó 25 citas clave e incorporó cinco objeciones de fondo: [`hallazgos/auditoria-y-condensacion-2026-10-17.md`](hallazgos/auditoria-y-condensacion-2026-10-17.md). La versión extensa anterior se conserva en el commit `4217d00`.

## ¿Cuál es la regla maestra?

> **No investigar para demostrar que Ellen White fue profeta ni para demostrar que no lo fue. Investigar hasta descubrir qué conclusión explica mejor toda la evidencia disponible y detenerse donde se detenga la evidencia.**
