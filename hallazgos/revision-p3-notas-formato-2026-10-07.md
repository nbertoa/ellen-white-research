# ¿Cómo se aplicó la pasada P3 de notas y formato?

**Fecha:** 7 de octubre de 2026  
**Origen:** puntos 21–24 de la auditoría externa y tareas de cierre dejadas por P2.  
**Alcance:** limpiar el aparato del manuscrito sin modificar la tesis, los grados de evidencia ni las conclusiones históricas.

## ¿Qué problema apareció durante la pasada y cómo se evitó perder trabajo?

Mientras P3 se desarrollaba, `main` avanzó mediante el PR #17. Ese PR modificó los capítulos 9, 14, 15 y 16. La primera rama P3 quedó divergida y no se fusionó.

Se creó `revision/p3-notas-formato-v2-2026-10-07` desde el `main` actualizado. Los cambios ya limpios de C1, C2, C3 y C10 se rebasaron sobre ese nuevo punto. C9 y C14 se reconciliaron manualmente para conservar las adiciones de P1: la investigación sobre la supuesta amenaza legal a *Sketches from the Life of Paul*, el caso *The Living Temple* y el caso «the daily». C15 y C16 no fueron reemplazados.

## ¿Qué capítulos recibieron limpieza de aparato?

Se trabajó directamente en C1, C2, C3, C9, C10, C11, C12, C13 y C14.

- **C1–C2:** se retiraron secciones de «bibliografía pendiente de cotejo» y comentarios no paginados usados sólo como bibliografía orientativa. Se conservaron textos bíblicos, entradas léxicas y artículos o documentos que sostienen realmente el argumento.
- **C3:** se normalizaron nombre narrativo, comillas y títulos en el cuerpo; la sección de fuentes quedó numerada. Las notas conservan la edición o documento realmente utilizado.
- **C9–C10:** se eliminaron remisiones a fichas internas como sustituto de evidencia. Los casos de Conybeare/Howson, Hus/Wylie, Veltman, March, Krummacher y Queensland siguen apoyados por las fuentes documentales correspondientes.
- **C11:** todos los subtítulos del cuerpo quedaron numerados; se retiraron enlaces a expedientes internos y se conservaron las cartas, exhibiciones y documentos que permiten reconstruir el trabajo de Davis, Bolton y las revisiones editoriales.
- **C12:** se retiraron referencias a inventarios y fichas internas; la subpregunta sobre geocronología quedó identificada como §9.1 y la sección de fuentes como §28. No se redujo el peso adverso de *An Appeal to Mothers*, medicamentos ni volcanismo.
- **C13:** se conservaron los 28 pares y la conclusión; las 49 notas ya no dependen de enlaces a expedientes internos. Se añadió §29 para el aparato documental.
- **C14:** se retiraron remisiones a expedientes internos conservando las fuentes externas y las limitaciones de transmisión; se mantuvieron intactas las adiciones de P1 sobre *The Living Temple* y «the daily».

## ¿Qué criterio se usó para retirar una referencia interna?

Una ficha de `hallazgos/` puede ser útil para investigar, pero no debe funcionar como autoridad frente al lector. Cuando una nota citaba una ficha y una fuente primaria o secundaria verificable, se dejó la fuente y se trasladó al texto de la nota sólo la limitación que cambia la evaluación: original no inspeccionado, transcripción tardía, fuente institucional, recuerdo retrospectivo, fecha incierta o ausencia de una pieza documental.

Cuando una remisión interna sólo repetía un método ya explicado en C1–C2, se reemplazó por una referencia narrativa al capítulo correspondiente o por una formulación breve del criterio.

## ¿Se ocultaron documentos todavía no obtenidos?

No. P3 elimina la expresión editorial «pendiente de cotejo» cuando sólo funcionaba como diario de trabajo, pero conserva la incertidumbre cuando afecta una conclusión.

Ejemplos que siguen explícitos:

- no se inspeccionó el autógrafo de determinadas cartas o recuerdos;
- no se conoce el borrador que permitiría decidir ciertas intervenciones editoriales;
- la carta original sobre las habitaciones de Paradise Valley no está disponible en la cadena usada;
- los recuerdos de quinina y vacunación son posteriores;
- el alcance de la negación de junio de 1897 sigue ambiguo;
- las condiciones propuestas para 1856 no quedaron demostradas como parte del anuncio original.

La regla es: **quitar el rastro del proceso, no la incertidumbre probatoria**.

## ¿Qué pasó con los títulos y nombres de obras?

En los capítulos directamente editados se aplicó la guía P2: `Elena G. de White` en la primera mención narrativa relevante y títulos castellanos habituales en la primera mención cuando eso no altera la identificación de la edición. Las notas bibliográficas conservan los títulos de las ediciones realmente citadas.

No se hizo una sustitución masiva en C4–C8, C15 y C16 porque el conector disponible exige reemplazar archivos completos y una corrección puramente mecánica no justificaba el riesgo de sobrescribir contenido reciente. Esa normalización de grafía permanece como tarea editorial menor; no es un defecto documental ni metodológico.

## ¿Se modificaron las conclusiones del libro?

No. P3 no cambia el sentido de las evaluaciones.

Entre otras cosas, permanecen:

- la dependencia literaria como hecho separado de su implicación para inspiración;
- los casos de 1879 y 1890 como dificultades específicas de origen, no prueba global de fraude;
- la intervención real de asistentes sin demostrar una autoría fantasma sistemática;
- errores históricos y científicos con distinto peso según el origen reclamado;
- la afirmación médica de *An Appeal to Mothers* como dificultad seria;
- las posibles contradicciones de medicamentos, junio de 1897 y diezmo;
- la tensión de la puerta cerrada;
- el incumplimiento literal de 1856 con la condicionalidad aún no demostrada en el anuncio original.

## ¿Qué limpieza mecánica queda fuera de P3?

Queda una tarea editorial menor para una fase de producción: uniformar exclusivamente grafías y primeras menciones en C4–C8 y C15–C16 si se desea que cada capítulo use exactamente `Elena G. de White` en el título o primera mención. No debe mezclarse esa sustitución con nueva investigación ni con cambios de contenido.

Antes de publicación en otro formato conviene además ejecutar sobre una copia local del árbol completo un control automático de referencias de notas, enlaces rotos y recuento final de palabras. En esta pasada no se afirma haber ejecutado un script local que el entorno no permitió ejecutar.

## ¿Qué prueba mostraría que P3 eliminó algo necesario?

Si al comparar la rama con `main` aparece una fuente primaria retirada sin reemplazo, una limitación probatoria borrada, una conclusión sustantiva modificada o una adición de PR #17 perdida, P3 debe corregirse antes de fusionarse. La comparación de ramas es el control final, no la intención editorial.
