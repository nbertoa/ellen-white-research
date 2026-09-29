# ¿Qué resiste una auditoría integral del libro sobre Ellen G. White?

Auditoría de investigación, 29 de septiembre de 2026. Repositorio: [nbertoa/ellen-white-research](https://github.com/nbertoa/ellen-white-research).

## ¿Qué se auditó y con qué límites?

Se inspeccionó el árbol completo de `main`, sus capítulos, las fichas de `hallazgos`, los documentos metodológicos, el README y los PR relacionados. La base de los capítulos 1–7 es el commit `1242677982dc3fe6b71095c65f6d4e5a95c5aff9`. El capítulo 8 y su ficha pertenecen al [PR 5](https://github.com/nbertoa/ellen-white-research/pull/5), cabeza `e0b10129cb379fa5b439946a7be1f20c5e72e35e`; todavía no forman parte de `main`. La auditoría incluye los ocho capítulos, pero no presenta ese borrador como texto integrado.

La metodología normativa es `metodologia/INSTRUCCIONES_PROYECTO.md`, junto con `MATRIZ_CRITERIOS_BIBLICOS.md` y la skill `ellen-white-investigacion-profetica`, incluida también entre los documentos del proyecto. El antiguo prompt de auditoría del capítulo 2 se examinó como antecedente de trabajo: su rama específica no se reutiliza para esta auditoría integral. No se tomó una revisión previa como prueba de exactitud.

**Resultado general:** el libro posee buenos controles conceptuales y varias reconstrucciones históricas cuidadosas. Todavía necesita correcciones documentales y argumentales antes de publicarse. Los problemas más materiales son la cronología incompleta del testimonio respiratorio, una inferencia fisiológica que excluye una alternativa antes de evaluarla, la insuficiente comparación entre la regla de condicionalidad del capítulo 2 y su aplicación en el capítulo 7, y la omisión de paralelos textuales que una fuente ya citada identifica. Nada de esto permite decidir aquí la autenticidad global de White.

**Límite importante:** leer y auditar todos los capítulos no equivale a autenticar todos los autógrafos ni a cotejar íntegramente cada monografía citada. Se cotejaron documentos externos concretos —incluidas reproducciones de primeras ediciones, periódicos y estudios— y se señala dónde sólo se obtuvo una transcripción, una reproducción posterior o una noticia bibliográfica. Los documentos cuyo original no pudo verificarse permanecen pendientes. La ausencia de una corrección en este informe no certifica una referencia no cotejada. Los apartados de fuentes y verificaciones pendientes permiten distinguir esos niveles.

Se emplean dos clasificaciones diferentes:

- **Hecho:** lo que el documento efectivamente registra. Que un testigo afirme una experiencia es un hecho documental; que la experiencia ocurriera exactamente así es otra proposición.
- **Interpretación:** lectura de hechos o documentos que requiere argumentación.
- **Hipótesis:** explicación causal posible, todavía no demostrada.

Y cuatro grados: **establecido, probable, posible e indeterminado**. “No establecido” no significa “falso”. “Indeterminado” tampoco significa que dos explicaciones tengan igual apoyo.

Las prioridades son **P0**, corrección indispensable antes de publicar; **P1**, investigación capaz de cambiar materialmente la evaluación; **P2**, mejora metodológica o argumental; **P3**, edición. Una misma cuestión puede exigir una corrección P0 ahora y conservar una investigación P1 después.

## ¿Qué archivos y antecedentes afectan la interpretación?

| Conjunto | Resultado de la inspección |
|---|---|
| Capítulos de `main` | 01 a 07, sin capítulos posteriores en ese árbol |
| Capítulo fuera de `main` | 08, sobre conocimientos privados, en PR 5 |
| Fichas bíblicas | 18 archivos en `hallazgos/criterios-biblicos/`: continuidad; Deut. 13; Deut. 18; medios de revelación; 1 Reyes 13; Isaías 8; Jeremías 23; Ezequiel 13; Miqueas 3; Mateo 7; 1 Juan 4; 1 Tes. 5; 1 Cor. 14; Balaam; Caifás; Lucas 1; inspiración/revelación/profecía; impresión/guía/iluminación |
| Otras fichas | Afirmaciones de White sobre don y autoridad; Rochester/Daniels del capítulo 8 |
| Metodología | Instrucciones, matriz y prompt histórico de auditoría de C2 |
| Notas y fuentes | Las notas principales están dentro de los capítulos; no se encontró en el árbol auditado una colección independiente de originales históricos ni un inventario de autógrafos |
| Documentos auxiliares suministrados | *The White Lie*, Rea; *Messenger of the Lord*, Douglass; *Profecías dramáticas*, Douglass; copia de la skill normativa |
| PR 1 y 2 | Antecedentes de auditorías de C2 y C1 |
| PR 3 y 4 | Desarrollo de C3 y revisión posterior de C1 |
| PR 5 | Desarrollo de C8 y correcciones de Rochester/Daniels |
| Comentarios y revisiones | Los cinco PR consultados no devolvieron comentarios, revisiones ni hilos de revisión; no hay una validación independiente documentada en esas superficies |
| Rama `audit/capitulo-03` | La comparación con `main` la muestra detrás, sin cambios exclusivos por integrar; no aporta un capítulo adicional |

Los identificadores de `main` y del PR 5 fijan el corpus; los números de sección citados abajo corresponden a esas versiones.

Un problema bibliográfico transversal: el PDF auxiliar cuyo nombre anuncia una edición de *Profecías dramáticas* de 2013 contiene portada legal, ficha catalográfica y colofón de **2009**, con original inglés de 2007. Debe citarse la edición realmente consultada, o documentarse otra edición de 2013. El nombre del archivo no determina la edición.

## ¿Qué resiste y qué debe corregirse en el capítulo 1?

**Archivo:** `capitulos/01-que-significa-inspiracion-iluminacion-revelacion-y-don-de-profecia.md`.

### ¿Cuál es su pregunta y qué intenta demostrar?

Pregunta principal: qué significan inspiración, iluminación, revelación, impresión, guía, profecía y don de profecía. Preguntas secundarias: autoridad, dictado, investigación, conciencia del hablante, canonicidad y errores personales. Conclusión explícita: son categorías relacionadas que no deben confundirse. Conclusión implícita: no puede evaluarse a White mediante una definición que la autentique o descalifique de antemano.

La conclusión responde a la pregunta. Es un capítulo de definiciones y exégesis, no una demostración histórica de que Dios causó determinadas experiencias.

### ¿Cuál es el estado general?

**Sólido en sus distinciones básicas; necesita controles menores de alcance y mejor trazabilidad de bibliografía técnica.** No se encontró un error material confirmado que obligue a cambiar su conclusión central. Esa apreciación no certifica las voces de BDAG/HALOT ni todos los comentarios citados: no se cotejaron íntegramente sus ediciones.

### ¿Qué afirmaciones importantes fueron sometidas a prueba?

| Afirmación | Qué permite comprobar la fuente | Evaluación |
|---|---|---|
| *Theopneustos* califica a Escritura, 2 Tim. 3:16 | La construcción y el contexto 3:14–17; no reconstruye el mecanismo literario | Establecido como observación textual; el alcance canónico requiere interpretación |
| 2 Pedro 1:20–21 combina hablar humano y acción del Espíritu | Eso afirma el pasaje; *epilysis* no resuelve por sí solo toda teoría de interpretación | Resiste la cautela actual |
| Lucas 1:1–4 reconoce transmisión, relatos y composición | El prólogo lo registra; no identifica cada fuente ni cuánto dependió de ellas | Establecido en ese alcance |
| Natán no convierte toda opinión personal en revelación | 2 Sam. 7 diferencia la respuesta inicial y la palabra nocturna posterior | Interpretación razonable; no prueba una teoría universal de profecía falible |
| Caifás profetiza sin quedar autenticado moralmente | Juan 11:49–52 atribuye significado profético a la declaración | Resiste; no convertirlo en ministerio profético estable |
| Agabo, Antioquía e hijas de Felipe | Hechos registra actividad profética sin libros canónicos atribuidos | Resiste; ausencia de atribución canónica no demuestra inexistencia de escritos perdidos |
| Profecía congregacional y canonicidad no son equivalentes | 1 Cor. 12–14 y 1 Tes. 5 mandan evaluar | Establecido el mandato; discutidas sus consecuencias para falibilidad y autoridad |

### ¿Hay problemas críticos?

No se confirmó un P0 propio del capítulo. Hay un riesgo que debe impedirse al aplicar estas definiciones: usar “la inspiración admite fuentes humanas” como inmunidad frente a cualquier atribución falsa de origen. El capítulo distingue correctamente esas cuestiones; los capítulos posteriores deben conservar esa distinción.

### ¿Qué problemas importantes requieren corrección?

**C1-01 — P2. Definición y autenticación.** En §§4, 12 y la tabla de §30, las expresiones “ayuda divina” y “acto por el cual Dios…” son definiciones teológicas. En una auditoría histórica se debe registrar primero **ayuda u origen divino reclamado**. El texto lo aclara en otros lugares, pero la tabla final debería mantener esa advertencia. De otro modo puede parecer que la clasificación verifica la causa.

**C1-02 — P2. Argumento de Lucas.** §§9 y 26 son fuertes dentro de la tradición que reconoce Lucas como inspirado. No demuestran empíricamente que una obra actual dependiente de otras esté inspirada. El capítulo ya introduce la premisa cristiana: preservarla explícitamente cada vez que el argumento se utilice fuera de este capítulo.

**C1-03 — P1 documental. Bibliografía exegética sin localizadores finos.** Las notas identifican obras serias, pero frecuentemente sólo “comentario a” un pasaje o una voz léxica. Conseguir página/entrada completa para Towner, Mounce, Bauckham, Green, Alexander, Adams, Fee y Thiselton, y verificar qué posición sostiene cada autor. Citar varios libros no establece consenso ni independencia argumental.

### ¿Qué problemas menores y estructurales aparecen?

**C1-04 — P3. Repetición.** §§9/26 vuelven al uso de fuentes; §§17/27 a comprensión y formulación; §§18–23 distribuyen muy finamente acto, don e identidad. No hace falta reescribir: fusionar o abreviar remisiones donde la segunda sección no agregue una dificultad.

Todos los encabezados del manuscrito están formulados como preguntas. La neutralidad es generalmente buena. El título es muy largo, pero contiene categorías necesarias; una versión más corta puede dejar la enumeración en la apertura. Las preguntas sobre definiciones funcionan mejor que las respuestas con varias reservas académicas acumuladas.

### ¿Cuál es la mejor defensa, objeción, respuesta y límite?

Defensa: los textos bíblicos describen procesos diversos; una sola escala de “más inspiración” los simplifica indebidamente. Objeción fuerte: una clasificación moderna puede imponer fronteras que el lenguaje bíblico no mantiene, especialmente Ef. 1:17–18 y la profecía congregacional. Respuesta: el capítulo reconoce superposición y usa categorías analíticas. Contrarespuesta válida: esas categorías deben ceder ante cada texto, en vez de convertirse en reglas para proteger un caso posterior.

Los trabajos de Blaylock y Schreiner son argumentos teológicos accesibles de sus autores, no testigos de los hechos de White. Begbie examina la inspiración desde un enfoque trinitario; no es por sí solo una prueba filológica de cada distinción del capítulo.

### ¿Qué evidencia nueva y reemplazos convienen?

Se localizó el [artículo original de Jeremy Begbie](https://www.tyndalebulletin.org/article/30483.pdf), *Tyndale Bulletin* 43.2 (1992), pp. 259–282. Agregar el enlace y citar la página del argumento utilizado. Los artículos de [Blaylock](https://www.thegospelcoalition.org/themelios/article/towards-a-definition-of-new-testament-prophecy/) y [Schreiner](https://www.thegospelcoalition.org/themelios/article/it-all-depends-upon-prophecy-a-brief-case-for-nuanced-cessationism/) permiten comprobar directamente posiciones que deben mantenerse como discutidas.

No reemplazar una discusión crítica por comentarios devocionales de las fichas. Las fichas son mapas de investigación, no fuentes independientes de los capítulos que las desarrollaron.

### ¿Qué conclusiones requieren recalibración y cuáles resisten?

La frase “inspiración no exige ausencia de investigación” resiste como rechazo de una incompatibilidad definitoria dentro del marco bíblico declarado. No convertirla en “el uso de fuentes confirma inspiración”. “Autor canónico”, “profeta” y “acto profético” siguen siendo distinciones sólidas. La relación exacta entre frecuencia de profecía y ministerio estable permanece indeterminada.

**Prueba de falsación:** un uso textual que identifique necesariamente esas categorías o un contexto que invalide una definición obligaría a corregirla. La mera aparición conjunta de términos no basta para demostrar equivalencia. Un caso histórico de falsa atribución de origen no refuta la posibilidad general de mediación humana, pero sí puede refutar una aplicación concreta a White.

## ¿Qué resiste y qué debe corregirse en el capítulo 2?

**Archivo:** `capitulos/02-que-credenciales-debe-reunir-un-profeta-autentico.md`.

### ¿Cuál es su pregunta y qué intenta demostrar?

Pregunta principal: qué criterios permiten evaluar una pretensión profética. Secundarias: continuidad, señales, predicciones, condicionalidad, contradicción, medios, autocontrol, carácter, dinero y origen. Conclusión: un conjunto de criterios con pesos diferentes; ni éxito aislado ni conducta atractiva autentican por sí solos. Implícitamente promete que esas reglas se fijarán antes de evaluar a White.

### ¿Cuál es el estado general?

**Buen fundamento; su mayor vulnerabilidad es una regla que los capítulos aplicados pueden flexibilizar retrospectivamente.** Debe sincronizarse la matriz auxiliar con este capítulo y especificarse cómo se pasa de un mensaje fallido a la evaluación global de una persona. No corresponde resolver ese paso contando puntos.

### ¿Qué afirmaciones importantes resisten el cotejo textual?

| Criterio | Texto y contexto necesario | Resultado |
|---|---|---|
| Una señal cumplida no basta | Deut. 13, lealtad a YHWH | Establecido como regla del texto; no implica que toda señal extraordinaria sea engaño |
| Una palabra atribuida a Dios que no acontece es una objeción seria | Deut. 18:20–22, en un marco de autorización y juicio | Resiste; necesita distinguir anuncio, atribución, condición y resultado |
| Condicionalidad real | Jer. 18:7–10; Jonás 3–4 | Resiste; no convierte automáticamente todo en condicional |
| Hananías y Jeremías | Jer. 28; mensaje de paz, plazo y muerte del opositor | Resiste como ejemplo del relato, no como verificación histórica externa del episodio |
| Revelación contradictoria | 1 Reyes 13 | Resiste la norma narrativa; no fabricar equivalencias exactas con todo cambio posterior |
| Instrucción y testimonio | Isa. 8:16–20 y consulta a muertos | Resiste el contexto inmediato; no reducir “ley” a un único catálogo denominacional |
| Examen comunitario | 1 Tes. 5:19–22; 1 Cor. 14:29–33 | Establecido; no presupone ya una doctrina de mensajes divinos falibles |
| Autocontrol | 1 Cor. 14:30–32, turnos de habla | Resiste la limitación al orden de asamblea; no exige atención ordinaria durante toda visión |
| Frutos y dinero | Mat. 7; Miq. 3 | Resiste; ingreso o imperfección no equivalen por sí solos a fraude |
| Sinceridad insuficiente | Jer. 23; Ez. 13 | Resiste como límite lógico; el texto no permite medir la sinceridad psicológica de cada acusado |
| Un acto verdadero no autentica todo un ministerio | Balaam y Caifás | Resiste; tampoco permite declarar irrelevante cualquier acto verdadero |

### ¿Qué problemas críticos requieren resolver antes de publicar el conjunto?

**C2-01 — P1/P2 transversal. Regla de condicionalidad parcialmente operacionalizada.** §6 ya admite, en cuarto lugar, evidencia anterior al desenlace de que el mensajero consideraba modificable el resultado. Por eso **no existe una contradicción formal automática** con el uso que C7 hace de 1883, si se entiende por desenlace la desaparición de todos los asistentes. La tensión está en el peso: “anterior a la muerte de todos” no equivale a “parte identificable del anuncio original”. Explicar qué evidencia basta para incorporar una condición no expresada y cómo se distingue de una reinterpretación tardía pero anterior al cierre definitivo. Aplicar esa misma regla a predicciones favorables y desfavorables.

La mejora no consiste en declarar automáticamente falsa a White. Consiste en hacer comprobable el grado de apoyo de una defensa condicional. El incumplimiento puede estar establecido mientras la clasificación teológica permanezca discutida; su peso adverso debe describirse, no neutralizarse con la palabra “indeterminado”. C7 ya reconoce una dificultad seria y la falta de condición en 1856; conservar ese reconocimiento.

### ¿Qué problemas importantes existen?

**C2-02 — P2. Mensaje versus persona.** §§21–22 advierten que un acierto no autentica globalmente. Falta una explicación igualmente precisa del movimiento inverso: ¿qué clase de error invalida un mensaje, qué errores desacreditan gravemente un ministerio y qué admisiones personales son ajenas a esa prueba? La regla debe depender de la atribución de origen y de la sustancia del error, no de excepciones ad hoc.

**C2-03 — P2. Matriz desactualizada.** La matriz auxiliar resume con menos cautelas algunas cuestiones: contradicción con revelación previa, sinceridad en Ezequiel y autocontrol. Actualizarla desde el texto más matizado; no usarla como una segunda autoridad independiente. “Ezequiel muestra sinceridad” debe significar, si acaso, que la convicción subjetiva no autentica, no que el historiador ha verificado intenciones interiores.

**C2-04 — P1. Lecturas críticas distintas.** Los trabajos de Atkins y Bosman sobre Deut. 18 tienen preguntas y reconstrucciones literarias diferentes. Verificar páginas concretas antes de presentarlos como apoyo conjunto. Que una lectura normativa de la forma final sea coherente no verifica la fecha histórica de composición ni todos los acontecimientos narrados.

### ¿Qué problemas menores aparecen?

**C2-05 — P3. Criterios repartidos.** §§4–6 y §25 repiten la misma decisión; las listas de §§22–24 reaparecen en §30. Conservar la explicación y usar una sola tabla final. No reducir por abreviación la discusión del mejor contraargumento.

Todos los títulos son preguntas. Las preguntas de §§18–19 se superponen parcialmente, pero la segunda aporta falsa seguridad y consecuencias, por lo que puede conservarse si la transición lo hace visible. El tono no es apologético ni acusatorio.

### ¿Cuál es la controversia más fuerte?

Defensa de la metodología: Deut. 18 debe leerse junto con Jer. 18, Jonás y otros límites bíblicos. Objeción: ese conjunto puede producir un sistema inmune a cualquier incumplimiento. Respuesta: condiciones documentadas, género y destinatarios deben fijarse sin mirar el resultado. Contrarespuesta: apelar después a un principio universal sin explicar su conexión con la frase concreta sigue sin permitir una prueba adversa.

Criterio de cierre propuesto: cuando no se pueda resolver la clasificación de un caso, conservar separadas la **evidencia contra una lectura determinada** y la **incertidumbre sobre su alcance teológico**. Una explicación posible no tiene automáticamente el mismo peso que una formulación explícita anterior.

### ¿Qué fuentes conviene obtener o sustituir?

Priorizar texto bíblico en contexto, luego discusión lingüística y literaria con páginas precisas. Fuentes académicas localizadas: [Atkins, DOI 10.2307/26424832](https://doi.org/10.2307/26424832) y [Bosman, artículo de *Acta Theologica*](https://journals.ufs.ac.za/index.php/at/article/view/6193). La localización bibliográfica y el resumen no equivalen a cotejo completo de todas las páginas usadas. No se pudo verificar íntegramente el aparato de comentarios y léxicos; conseguirlo sigue siendo P1 documental.

### ¿Qué requiere recalibración y qué resiste?

La regla “una señal cumplida no demuestra por sí sola autenticidad” es sólida. La exigencia de evaluar origen, mensaje y resultado antes de concluir también. “Una condición general basta para explicar un incumplimiento particular” no está establecido por el capítulo y no debe introducirse después como si lo estuviera. La continuidad del don después de los apóstoles sigue siendo una cuestión interpretativa abierta; los pasajes no autentican a White.

**Falsación:** una promesa específica, inequívocamente atribuida a Dios, fijada antes del resultado y sin condición identificable debe poder contar seriamente contra la pretensión. Si todas esas condiciones pueden reinterpretarse sin límite, el sistema pierde capacidad de prueba.

## ¿Qué resiste y qué debe corregirse en el capítulo 3?

**Archivo:** `capitulos/03-que-afirmo-ellen-white-sobre-su-propio-don-y-sobre-el-origen-y-la-autoridad-de-sus-mensajes.md`.

### ¿Cuál es su pregunta y qué intenta demostrar?

Reconstruye la pretensión que realmente hizo White: origen divino, función de mensajera, autoridad, inspiración no universal, edición, falibilidad personal y primacía bíblica. Su conclusión es descriptiva: White reclamó revelación con mediación humana y autoridad derivada. No determina si esa pretensión era verdadera. Implícitamente establece qué clase de atribuciones deben ponerse a prueba después.

### ¿Cuál es el estado general?

**La reconstrucción central resiste; el capítulo delimita bien varias citas usadas habitualmente fuera de contexto.** Necesita incorporar un reconocimiento concreto del uso de historiadores, reducir una generalización sobre infalibilidad y documentar mejor versiones y fechas de los originales privados.

### ¿Qué documentos y afirmaciones son decisivos?

| Documento | Lo que prueba | Lo que no prueba |
|---|---|---|
| Carta del 20-XII-1845, publicada 24-I-1846 | Primera atribución divina conocida en su relato personal publicado | Fecha exacta de la experiencia ni ausencia de narración oral anterior |
| Registro de discurso de 1904, Ms 140 de 1905; aclaraciones de 1905–1906 | Tensión verbal y posterior afirmación de función profética | Que todos los oyentes entendieran ya esa precisión en 1904 |
| Folleto Battle Creek 1882, pp. 47–49; No. 33, 1889 | Autoridad fuerte y rechazo de reducir testimonios a juicio ordinario | Inspiración de todas las frases privadas y datos cotidianos |
| Ms 107, 1909 | Distinción común/sagrado y reconocimiento del dato erróneo de habitaciones | Clasificación completa de cada texto mixto |
| RH 8-X-1867; Lt 206 y 225 de 1906 | Lenguaje propio, rechazo de pretensión universal y asistencia editorial | Que ningún pasaje revelado hubiera tenido palabras dadas; que toda edición fuera inocua |
| Ms 24, 1886 | Modelo sobre la inspiración bíblica | Regla exhaustiva para cada escrito propio |
| Lt 10, 1895; Lt 27, 1876 | Negación de infalibilidad personal y perfección moral | Admisión explícita de error en una revelación inequívoca |
| Introducción de GC 1888; texto de 1903 sobre dos luces | Primacía bíblica declarada y referente probable de sus libros | Que la práctica histórica de toda comunidad respetara esa jerarquía |

Se cotejó el argumento de aplicación sin nueva visión en una reproducción digital de 1949 y en el facsímil de **No. 33 (1889), pp. 211–218**, que incluye el argumento de Chloe y la frase de rechazo del testimonio como rechazo del Señor. La primera edición permite sostener la conclusión sin depender sólo de 5T o *Testimony Treasures*.

### ¿Hay problemas críticos?

No se confirmó un P0 que invierta la reconstrucción central. **No debe usarse esta reconstrucción como prueba de coherencia efectiva de todas sus actuaciones:** lo establecido es lo que declaró, no que cada relato, fuente o revisión se ajuste siempre a su modelo.

### ¿Qué problemas importantes existen?

**C3-01 — P1/P2. Reconocimiento explícito de historiadores omitido.** §§7, 9 y 11 discuten edición, Biblia y dependencia, pero falta el reconocimiento de la introducción de *The Great Controversy* de que utilizó obras de historiadores y autores sobre la Reforma, a veces sin crédito específico. Es una declaración propia que afecta directamente la reconstrucción de cómo entendía su escritura. No basta con decir en abstracto que la inspiración puede admitir fuentes.

El pasaje favorece una defensa importante: no toda semejanza textual contradice una atribución divina según el modelo declarado. También fortalece una pregunta crítica: ¿qué parte de la narración provino de lectura, qué presentó como visto y cómo distinguió ambas? Incluirlo no resuelve el debate sobre exactitud histórica, proporción de dependencia o atribución de origen. Se localizó su reproducción en [*Use of Historical Writings*](https://text.egwwritings.org/read/725.84); falta cotejar aquí la página de un ejemplar original de GC 1888. No se certifica una comparación integral 1888/1911.

**C3-02 — P2. Generalización sobre infalibilidad.** §8 concluye: “no se presentó como infalible en su conocimiento, memoria, conducta o juicio humanos”. Lt 10 niega infalibilidad personal, pero no enumera todas esas facultades; Lt 27 se refiere a conducta. El error común reconocido en 1909 permite ampliar parte del cuadro. Mejor: “Negó infalibilidad personal, reconoció errores de conducta y admitió al menos un dato ordinario equivocado. Estos textos no delimitan exhaustivamente errores de memoria o juicio en mensajes revelados”.

**C3-03 — P1. Documento conservado versus acto original.** Ms 140 está catalogado en 1905 para un discurso de 1904. Se necesita identificar si es transcripción contemporánea, copia posterior o reconstrucción, y si existe otra versión del discurso. La probable armonización con 1905–1906 no debe sustituir ese dato.

**C3-04 — P2. Paulson.** La carta rechaza la conjunción extrema “cada palabra pública/privada y cada carta, en cualquier circunstancia”. No demuestra por sí sola ausencia de una pretensión verbal para cada clase de comunicación revelada. El capítulo lo matiza con 1867, Ms 24 y trabajo editorial; mantener esa combinación y no citar sólo el “nunca afirmé” como solución universal.

### ¿Qué problemas menores aparecen?

**C3-05 — P3. Fechas y localizadores.** Añadir páginas originales de No. 33 junto a las de 5T. Corregir la ficha cuando remite al capítulo 2 para la discusión de Lucas: esa discusión está principalmente en C1. Los encabezados son preguntas neutrales. §12 reúne demasiadas conclusiones; una tabla corta de pretensión, evidencia y límite ayudaría sin reescribir el capítulo.

### ¿Cuál es el mejor intercambio argumental?

Defensa fuerte, desarrollada por Douglass: revelación, lenguaje humano, edición y aplicación pueden coexistir coherentemente. Objeción fuerte: las fórmulas de autoridad de 1882/1889 son tan amplias que no se las puede rebajar a consejo opcional cuando aparece un error. Respuesta: hay asuntos ordinarios y aplicación de luz previa documentados. Contrarespuesta: la clasificación debe fijarse por el documento y su atribución concreta, no por el resultado conveniente.

Rea sirve para localizar la tensión entre autoridad y dependencia, pero sus generalizaciones no autentican cada acusación. El reconocimiento de historiadores es una mejor prueba de la posición de White que una paráfrasis de un apologista o de Rea.

### ¿Qué fuentes requieren reemplazo o comprobación adicional?

Usar [No. 33 original, digitalizado por el Center for Adventist Research](https://www.truthseeker.church/_files/ugd/ff8319_ab842bbcc907444caba705ad30178d1c.pdf), pp. 211–218, en lugar de depender de la compilación de 1949. El anfitrión del PDF sostiene sus propias polémicas; el facsímil se usa por su contenido de 1889, no por esas interpretaciones. Conservar simultáneamente la referencia archivística original.

Quedan sin autenticación material en esta auditoría los autógrafos de Lt 55, 206, 225, 244, 10, 27, 11 y los manuscritos 140, 63, 24 y 107. Las ediciones documentales identificadas permiten seguir la investigación, pero no sustituyen el examen de soporte, copia y variantes. No se pudo cotejar aquí íntegramente cada primera publicación citada.

### ¿Qué conclusiones resisten y qué las podría cambiar?

Resisten: función profética incluida en la comisión que afirmó; autoridad divina reclamada para testimonios; distinción de asuntos comunes; mediación humana admitida; Biblia como norma declarada. Permanece indeterminada su posición precisa sobre error sustantivo en un mensaje inequívocamente revelado.

**Falsación:** un original que mostrara interpolación editorial de las fórmulas de autoridad; una retractación explícita sostenida del don; una admisión inequívoca de error revelatorio; o una dependencia documentada incompatible con una atribución concreta. Ninguna etiqueta general de “inspiración de pensamiento” debe impedir que esos documentos cambien la evaluación.

## ¿Qué resiste y qué debe corregirse en el capítulo 4?

**Archivo:** `capitulos/04-que-ocurrio-realmente-en-las-primeras-visiones-de-ellen-g-white.md`.

### ¿Cuál es su pregunta y qué intenta demostrar?

Reconstruye comienzo, primeras versiones, testigos, puerta cerrada, Atkinson y cambios del relato. Conclusión: están documentadas experiencias públicas y su interpretación religiosa temprana, pero no un origen sobrenatural verificado ni una cronología completa contemporánea. Implícitamente presenta un relato estable en su núcleo, con detalles y revisiones posteriores.

### ¿Cuál es el estado general?

**Una de las reconstrucciones más cuidadosas del libro. Tiene una omisión material precisamente en la fuente empleada para comparar las versiones.** La puerta cerrada y Dammon no deben cerrarse sólo por armonizaciones tardías ni por convertir un periódico en acta judicial íntegra.

### ¿Qué cronología soporta el argumento?

| Acontecimiento o afirmación | Fecha atribuida | Documento/publicación | Peso |
|---|---|---|---|
| Primera visión | Diciembre de 1844, reconstrucción probable | Primer relato personal fechado 20-XII-1845; publicación 24-I-1846 | No es documentación de diciembre de 1844 |
| Noticias de visiones de Miss Harmon | Antes de agosto de 1845 | James White, carta 19-VIII; publicación 6-IX-1845 | Temprana; James es participante favorable, no independiente del círculo |
| Reunión Atkinson | 15-II-1845 | Juicio 17–18-II; *Piscataquis Farmer* 7-III | Muy próxima, pero periodística y abreviada |
| Nichols escribe a Miller | 20-IV-1846 | Carta conservada/reproducida después | Temprana a varios episodios, no testimonio presencial de la primera visión de diciembre |
| Primer relato reimpreso con referencias | 1847 | *A Word to the Little Flock* | Texto y notas deben separarse |
| Revisión abreviada | 1851 | *Experience and Views* / Extra de RH | Cambios verificables; motivo no se deduce automáticamente |
| Randolph, Biblia y prueba | Invierno 1845–1846 | Nichols publicado en 1860 | Testimonio presencial reclamado, memoria retrospectiva |
| Hannibal, no respiración y Biblia | 1848 | James a Hastings, 26-VIII-1848, transcripción de Record Book 1 | Nueva línea temprana; pendiente autenticar copia/manuscrito |
| Denegación retrospectiva de cierre universal en visiones | 1874 y posteriores | Declaraciones explicativas de White | No anulan por sí solas lo dicho en documentos anteriores |

### ¿Qué problemas críticos aparecen?

**C4-01 — P0 de cobertura. Paralelos con Foy y 2 Esdras omitidos.** §§16–18 emplean la comparación de Ronald Graybill sobre versiones de la primera visión, pero no examinan dos datos relevantes que él señala: referencias editoriales a 2 Esdras y el paralelo verbal de las puertas/bisagras con Foy, incluido el cambio posterior de “golden” a “glittering”. Son precisamente datos capaces de modificar la evaluación de independencia y origen del relato.

La corrección indispensable es **incorporar y evaluar la evidencia**, no declarar plagio ni revelación por adelantado. La fecha atribuida a la experiencia de White precede al folleto de Foy de 1845, mientras que el relato personal impreso de White en 1846 es posterior. Esa diferencia impide tanto “copió necesariamente su primera experiencia del impreso” como “el impreso no pudo influir en su primera redacción publicada”. El acceso oral anterior, el vocabulario religioso compartido y la revisión de 1851 son hipótesis diferentes que requieren pruebas diferentes.

### ¿Qué problemas importantes existen?

**C4-02 — P1/P2. Cronología fisiológica incompleta.** §19 y su tabla deben integrar la carta de James a Hastings de 1848. No demuestra apnea medida, pero acorta sustancialmente el intervalo entre un episodio y un testimonio que afirma ausencia de respiración. Remitir todo ese asunto a una descripción general de 1868 deja fuera una línea documental favorable relevante.

**C4-03 — P1. Puerta cerrada: proposiciones diferentes.** §§9 y 18 deben mantener separadas: (a) creencia personal inicial; (b) límite de salvación atribuido a la visión; (c) aplicación a quienes rechazaron el movimiento; (d) desarrollo posterior de evangelización. El texto suprimido en 1851 es evidencia de redacción, no prueba automática del motivo de supresión. Las posteriores negativas de White son una respuesta que debe pesarse frente a las primeras expresiones, no una clave que las vuelva inocuas por definición.

**C4-04 — P2. Estabilidad textual no es corroboración del acontecimiento.** La repetición del núcleo entre escritos propios y reediciones demuestra transmisión y estabilidad relativa. No ofrece varias confirmaciones independientes de lo ocurrido en diciembre de 1844. James y Ellen compartían contexto y relato; la genealogía documental debe indicarlo.

**C4-05 — P1. Dammon.** El periódico no es transcripción taquigráfica íntegra ni expediente original. La afirmación posterior de que se revocó la condena o se anuló el procedimiento, si procede de Dammon, debe seguir siendo **afirmación de parte** hasta localizar el registro de apelación. Tampoco llamar “médico” a un testigo o atribuirle una medición que el texto no describe.

### ¿Qué problemas menores aparecen?

**C4-06 — P3. Organizar por interrogante decisivo.** §§16–18 tienen información parcialmente repetida; §23 es útil como trazabilidad, pero puede ir a un anexo documental. Conservar el contraste de versiones y la pregunta pendiente. Títulos y subtítulos son preguntas y el tono es generalmente neutral.

### ¿Cuál es el mejor argumento de cada lado y su límite?

Favorable: testimonios tempranos de estados públicos, la disposición de Nichols/Bates a examinar y un relato identificable antes de una tradición denominacional extensa impiden reducir todo a invención muy tardía. Objeción: no hay registro contemporáneo de diciembre de 1844; relatos propios y allegados no autentican su origen, y el contenido comparte imágenes y fórmulas disponibles.

Respuesta: semejanza literaria y marco cultural no demuestran fabricación ni excluyen la mediación humana admitida por White. Contrarespuesta: cuando la afirmación es “vi esto”, hay que estudiar si el contenido concreto procede de una fuente anterior, qué versión lo contiene y cuándo se documentó. No basta una doctrina abstracta de inspiración.

Sobre Atkinson: un informe hostil cercano puede ser más útil cronológicamente que una memoria favorable de décadas después, pero su hostilidad y abreviación limitan su fidelidad. La participación en una reunión tampoco prueba que White apoyara todas las prácticas atribuidas a todos los presentes.

### ¿Qué evidencia nueva y reemplazos se encontraron?

- [Graybill, “Visions and Revisions—Part 1”, *Ministry*, febrero de 1994, pp. 11–13](https://www.ministrymagazine.org/archive/1994/02/visions-and-revisions?mode=app): localizar los apartados sobre apócrifos, Foy y revisión de 1851. El artículo **ya está citado**; los datos son nuevos respecto del desarrollo actual del capítulo, no nuevos para la historiografía.
- [Foy, folleto de 1845](https://documents.adventistarchives.org/Books/WFoy1845.pdf): contiene el paralelo de la puerta y las bisagras. El PDF servido es una edición textual moderna del folleto, no debe llamarse facsímil de la impresión de 1845 sin comprobarlo.
- [*A Word to the Little Flock*, reproducción textual](https://www.aplib.org/files/ebooks/pdf/James%20White%20-%20A%20Word%20to%20the%20Little%20Flock.pdf): conserva la escena y un aparato/añadidos posteriores. Obtener facsímil que permita comprobar las referencias tal como se imprimieron en 1847; no datar prefacio/apéndice moderno en 1847.
- [James White a Hastings, 26-VIII-1848, en colección del White Estate](https://whiteestate.org/about/issues1/unusual/shut-door/door-docs/): episodio de Hannibal y fuente declarada Record Book 1, pp. 18–20. Es transcripción accesible; solicitar imagen del registro y precisar cuándo se copió.
- [Transcripción anotada sobre el juicio de Dammon](https://whiteestate.org/legacy/issues-israel_damman-html/): usar el artículo de 1845 como fuente y separar anotaciones editoriales modernas. La transcripción no constituye un segundo testigo independiente del periódico.

### ¿Qué conclusiones requieren recalibración y cuáles resisten?

“No existe testimonio independiente contemporáneo de la primera visión de diciembre” resiste **dentro del corpus localizado**, sin convertirse en afirmación universal de inexistencia. “El núcleo permaneció estable” debe añadir “en la transmisión escrita conocida” y no implicar una certificación del episodio. Cualquier conclusión que presente el contenido inicial sin examinar los paralelos es incompleta.

Resisten: fecha de diciembre como probable, distinción entre experiencia y primera impresión, relevancia del informe Dammon, modificación de redacción y necesidad de separar recuerdo de documento temprano. La ausencia de una explicación natural demostrada no prueba origen divino.

**Falsación:** una carta de diciembre de 1844 con contenido preciso, un original anterior de Nichols, un testigo realmente independiente, el texto de una apelación o una primera versión distinta podrían modificar mucho la reconstrucción. Un paralelo verbal sólo refuta independencia textual si se demuestra dirección y acceso suficientes; no prueba automáticamente fingimiento de la experiencia.

## ¿Qué resiste y qué debe corregirse en el capítulo 5?

**Archivo:** `capitulos/05-que-ocurria-fisicamente-durante-las-visiones-de-ellen-g-white.md`.

### ¿Cuál es su pregunta y qué intenta demostrar?

Pregunta principal: qué puede saberse de los fenómenos físicos. Secundarias: ojos, respuesta, rigidez, respiración, pulso, voz, recuperación, médicos, Biblias e independencia de testigos. Conclusión: hubo estados públicos inusuales; los rasgos más extraordinarios no están demostrados con la precisión atribuida después. Implícitamente separa una experiencia real de interpretaciones fisiológicas y religiosas.

### ¿Cuál es el estado general?

**Tiene buenos controles de memoria y medición, pero requiere dos correcciones materiales y varias referencias exactas.** La prudencia sobre apnea completa resiste. La inferencia que obliga a descartar literalidad no está formulada con la misma neutralidad que el resto del capítulo. La carta de 1848 modifica el mapa de fuentes, aunque no prueba el fenómeno fisiológico.

### ¿Qué problemas críticos se confirmaron?

**C5-01 — P0. Cronología de la afirmación respiratoria incompleta.** §7 pregunta por la primera fuente y responde a partir de *Life Incidents* (1868); §3 ofrece esa fecha como comienzo de la descripción general. La carta de James White a los Hastings, fechada **26 de agosto de 1848**, ya afirma que en Hannibal Ellen estuvo en visión una hora y media sin respirar y que manipuló una Biblia grande.

Matiz indispensable: el capítulo dice “primera descripción **impresa** que hemos podido localizar”. No se ha establecido aquí la primera impresión de la carta privada de 1848, por lo que no corresponde acusarlo de fechar mal esa primera impresión. **Sí hay que corregir la impresión global de que el primer registro documental inequívoco sólo aparece veinte años después.** Añadir una fila separada: carta fechada en 1848, conservada mediante registro/transcripción posterior; fecha de copia y autógrafo pendientes. Mantener 1868 como descripción general impresa localizada, con alcance explícito.

No convertir la nueva carta en medición: el marido reporta ausencia de respiración, no describe instrumentación ni garantiza continuidad de observación. La carta favorece anterioridad del testimonio; no autentica apnea completa, sobrenaturalidad ni todas las historias posteriores.

**C5-02 — P0. Inferencia fisiológica que cierra una alternativa antes de probarla.** §12 dice: “Obliga a reconocer que al menos una parte de la descripción no está siendo entendida o transmitida literalmente”. De “incompatible con fisiología humana conocida” no se sigue lógicamente que el relato deba ser no literal si el libro mantiene abierta una hipótesis de intervención extraordinaria. Tampoco la anomalía establece un milagro.

Corrección breve: “La descripción literal sería extraordinariamente incompatible con la fisiología humana ordinaria. Las fuentes disponibles no permiten establecerla; error de observación, duración o transmisión son alternativas que deben examinarse. La incompatibilidad fisiológica, por sí sola, no decide entre esas alternativas y una intervención extraordinaria”. Después puede argumentarse cuál tiene mejor apoyo documental, sin convertir la medicina ordinaria en premisa metafísica.

### ¿Qué problemas importantes requieren corregirse?

**C5-03 — P0 documental. Páginas equivocadas de *Rise and Progress* (1892).** El cotejo del facsímil confirma:

| Nota de C5 | Referencia actual | Referencia correcta en la edición de 1892 |
|---|---|---|
| 7, Daigneau/Diagneau, 5-XI-1862 | pp. 264–265 | **pp. 247–248**, comienzo en p. 247; la ortografía del libro es Daigneau |
| 8, Bourdeau, declaración 4-II-1891 | pp. 98–99 | **p. 97** |
| 10, Kellogg/Drummond | pp. 95–96 | Correcta |
| 12, Fowler y otros, Lord | pp. 96–98 | El bloque pertinente comienza en **p. 96** y sigue en **p. 97**; precisar autores |
| 13, Brown en Parkville | pp. 209–211 | **pp. 97–98** para Brown; **236–237** para la narración de la guerra, otro pasaje |

Fuente: [*Rise and Progress*, 1892](https://documents.adventistarchives.org/Books/RP1892.pdf). Se usan **páginas impresas**, no el contador del lector PDF. El PDF tiene portadas y láminas, por lo que no existe un desplazamiento único para todas las páginas. Estas referencias deben corregirse antes de publicar aunque no inviertan la conclusión sobre respiración.

**C5-04 — P2. Un examen versus varias declaraciones.** §9 acierta al no multiplicar exámenes de Lord. Pero varias declaraciones personales de Fowler, Glover, Carpenter y F. C. Castle sobre una misma ocasión pueden aportar corroboración parcial si se determina cómo fueron recogidas. Una ocasión no son varios exámenes; varios documentos tampoco son necesariamente una sola voz. La dependencia se prueba por circulación de relatos, recopilación, redacción conjunta o copia, no simplemente porque presenciaran el mismo episodio.

**C5-05 — P1. Médicos por referencia.** No hay notas clínicas de Drummond, Lord o Brown en el corpus cotejado. Kellogg refiere Drummond décadas después y recibió formación médica posteriormente. Bourdeau describe una prueba en primera persona, pero su declaración es tardía. Las denominaciones “médico” e “incrédulo” requieren identificar al sujeto y no convertir una anécdota favorable en certificación clínica independiente.

**C5-06 — P2. Objeto conservado versus hazaña.** §16 separa bien la gran Biblia del prodigio. Mantener además la diferencia entre fecha de impresión del objeto, pertenencia tradicional a Harmon, prueba de posesión en 1845 y fecha de la narración de la hazaña. La existencia actual del libro no establece por sí sola lugar, postura, duración o contenido de una visión. El relato de Randolph/Nichols tampoco debe fusionarse con el de la Biblia de Portland.

**C5-07 — P2. Grados de certeza.** §12 “Muy probable: los observadores no detectaban una respiración normal” debería precisar que se refiere al núcleo compartido **de lo que reportaron**, con incertidumbre sobre percepción real en cada episodio. La repetición de una tradición no aumenta automáticamente el grado de certeza fisiológica.

### ¿Qué problemas menores y estructurales aparecen?

**C5-08 — P3. Amadon.** La nota 6 reconoce que RH de mayo de 1944 reproduce *Ministry*. Citar primero la publicación anterior de *Ministry*, con mes/página una vez cotejada, y no llamar RH la publicación más antigua localizada si ya se reconoce una anterior. La fecha de escritura del testimonio sigue pendiente y su publicación fue póstuma.

**C5-09 — P1/P2. Dos fechas distintas del cantero.** El cotejo del [*General Conference Daily Bulletin*, 18-III-1891, p. 145](https://documents.adventistarchives.org/Periodicals/GCSessionBulletins/GCB1891-11.pdf) añade una discrepancia que el capítulo no registra: Loughborough sitúa allí el episodio del cantero en el **otoño de 1863**, sin nombrarlo; el libro de 1892 lo vincula al **5-XI-1862** e identifica a Daigneau. La misma similitud de escena sugiere que son versiones del mismo episodio, pero su identidad exacta y la fecha deben comprobarse. No presentar 1862 como fecha independiente confirmada por ambos textos. Es diferencia documental establecida; error de memoria, corrección posterior o episodios distintos siguen siendo hipótesis. Esta página también distingue la Biblia de Portland y otra copia en Topsham con Truesdail: no fusionarlas con Randolph.

Todos los encabezados son preguntas. §§7–13 forman una secuencia clara. Las conclusiones repetidas de §§21, 23 y 24 pueden abreviarse. El título “¿Podía hablar sin respirar?” exige explicar qué sentido de “respirar” se evalúa: ausencia de inspiración visible, ausencia de ventilación, ausencia de todo flujo de aire y sostén vital no son la misma proposición.

### ¿Qué afirmaciones resisten y cuáles permanecen abiertas?

| Afirmación | Clasificación después de la auditoría |
|---|---|
| Existían informes de estados físicos inusuales | Establecido documentalmente; respaldo temprano en Atkinson/Bates y ahora carta de 1848 |
| Ojos abiertos y mirada elevada en algunas ocasiones | Probable; no certificación de cero parpadeos en todas las visiones |
| Rigidez y respuesta reducida al entorno | Probable en algunas ocasiones; mecanismo indeterminado |
| Fuerza que superaba límites humanos medidos | No establecido; no medición de fuerza o protocolo |
| Testigos dijeron que no percibían respiración | Establecido que lo escribieron; probable núcleo observacional, con grados variables |
| Apnea completa durante toda una visión larga | Indeterminado/no establecido por estas fuentes |
| Los médicos demostraron origen divino | No establecido |
| La Biblia conservada prueba la hazaña | Inferencia inválida |
| Toda fisiología relatada es ficción | Tampoco establecido |

### ¿Cuál es el mejor argumento favorable y la mejor objeción?

Favorable: hay un testimonio fechado muy cerca de un episodio en 1848, observadores que describen pruebas, escépticos que cambiaron de opinión y persistencia de un núcleo físico. Objeción: no se midieron variables decisivas, las pruebas no garantizan observación continua y gran parte de los detalles procede de memorias seleccionadas décadas después.

Respuesta favorable: una fuente histórica no necesita instrumental moderno para registrar un hecho extraordinario y la ausencia de instrumental no vuelve falso un testimonio. Contrarespuesta: cuanto más extraordinario y fisiológicamente preciso sea el hecho afirmado, más importa distinguir relato, percepción, medición y causalidad. Un testigo sincero puede errar sobre una variable invisible sin fingir toda la experiencia.

No basta decir “no respiraba porque era profeta” ni “debía respirar porque no puede haber milagros”. En ambos casos se importa la conclusión a la premisa.

### ¿Qué evidencia nueva y fuentes anteriores se encontraron?

La **carta de 1848** es la adición material principal. F. C. Castle es una declaración relevante presente en el bloque de 1892; agregarla si se inventaría allí la participación de testigos, sin multiplicar episodios.

Se cotejó [Butler, RH 9-VI-1874, pp. 201–202](https://documents.adventistarchives.org/Periodicals/RH/RH18740609-V43-26.pdf), y la recopilación de [1919 reproducida en *Spectrum*](https://www.andrews.edu/library/car/cardigital/Periodicals/Spectrum/1979-1980_Vol_10/22253166.READER_044.pdf). La transcripción de 1919 aporta reservas epistemológicas de Daniells; no es un examen de White ni una declaración de que toda visión fuera falsa. Sustituir compilaciones modernas de la descripción de James por [*Life Incidents*, 1868, pp. 272–273](https://www.gutenberg.org/files/61394/61394-h/61394-h.htm), reproducción textual de la edición, no facsímil de sus páginas.

Pendientes: autógrafo/copia de James 1848; originales de declaraciones de 1890–1897; expediente y fecha de escritura de Amadon; registros directos de los médicos; testimonio Nichols de 1860 frente a cartas anteriores; procedencia documental de la Biblia. No se localizaron mediciones clínicas contemporáneas verificables.

**Falsación:** un registro instrumental autenticado, una nota clínica contemporánea precisa o un testimonio temprano que describa respiración ordinaria en la misma ocasión modificarían el análisis. Una carta temprana mejora anterioridad, pero no soluciona automáticamente la medición. Una explicación natural posible no basta para probar que ocurrió.

## ¿Qué resiste y qué debe corregirse en el capítulo 6?

**Archivo:** `capitulos/06-que-podria-explicar-las-visiones-de-ellen-g-white.md`.

### ¿Cuál es su pregunta y qué intenta demostrar?

Examina lesión infantil, epilepsia, disociación, trance, entorno, Foy/Foss, sinceridad, fraude y diversidad de experiencias. Conclusión: ninguna causa única queda demostrada; hay explicaciones posibles con apoyos desiguales. Implícitamente intenta evitar tanto diagnóstico retrospectivo como inferencia sobrenatural por descarte.

### ¿Cuál es el estado general?

**La conclusión cauta resiste. Se confirmó un error numérico en una fuente médica y una limitación importante de selección que debe hacerse más explícita.** Su discusión de epilepsia es más equilibrada que las formulaciones categóricas de algunos críticos y defensores, pero las historias físicas no pueden aceptarse como datos clínicos firmes sólo al evaluar una hipótesis natural.

### ¿Qué problemas críticos se encontraron?

No se confirmó un P0 factual que determine la causa de las visiones. **Sí hay un P0 transversal si se conserva C5-02:** C6 no puede mantener abierta la hipótesis divina mientras C5 obliga lógicamente a reinterpretar todo fenómeno incompatible con la fisiología ordinaria.

### ¿Qué problemas importantes requieren corrección?

**C6-01 — P2 factual. Pacientes confundidos con registros.** Nota 8: “84 episodios de 53 pacientes”. La tabla 1 del estudio de Larsen y colaboradores contiene **52 pacientes, 53 registros y 84 crisis** para *focal impaired awareness*. La cifra 53 corresponde a registros, no personas. Corregirla. No cambia la mediana de 42,5 segundos ni establece un diagnóstico de White.

**C6-02 — P1/P2. La muestra no evalúa estados epilépticos.** §3 menciona episodios prolongados y estados epilépticos, pero la nota del estudio omite que se excluyeron **20 pacientes con estado epiléptico** por la imposibilidad de medir duración con el procedimiento usado. Los pacientes estudiados no estaban sometidos a retirada de medicación. La duración de las crisis habituales sirve como comparación limitada, no como exclusión empírica de estados prolongados del siglo XIX.

El capítulo ya distingue la excepción y exige signos positivos, lo cual es correcto. Añadir la exclusión evita que el lector piense que el estudio midió precisamente la alternativa que se está discutiendo. Tampoco la mera existencia del estado epiléptico permite atribuírselo retrospectivamente a White.

**C6-03 — P2. Evidencia física asimétrica.** Las duraciones y la articulación de mensajes que debilitan una crisis típica dependen en parte de recuerdos que C5 declara imprecisos. Debe expresarse el argumento condicionalmente: **si esas duraciones y conductas son fiables**, no encajan bien con una sola crisis focal habitual. No aceptar horas como dato firme contra epilepsia y rechazarlas como recuerdo débil al discutir apnea.

**C6-04 — P1. Kellogg 1906.** La carta de Merritt a John, 3-VI-1906, es accesible mediante la reproducción de Couperus. Se cotejó el extracto, no el autógrafo ni la carta completa. Es una memoria de un testigo cuya interpretación cambió, no un diagnóstico contemporáneo. Obtener original y contexto para evaluar observaciones estables frente a etiquetas añadidas. Su declaración favorable de 1890 y la interpretación posterior no son dos testigos independientes.

**C6-05 — P1/P2. Foy y Foss.** La corrección de Rea sobre continuidad de Foy es valiosa. Pero C6 debe integrar el paralelo verbal concreto detectado en C4; “semejanza de ambiente” es demasiado general para ese dato. En Foss, separar evento reclamado de 1844, memoria/documentación posterior y conversación de 1890. La fecha tardía de una carta no autentica por sí sola la experiencia inicial. No afirmar incumplimiento de la comisión, transferencia del don o causalidad como hechos históricos establecidos.

**C6-10 — P1/P2. Comparación natural relevante en el mismo estudio.** Larsen et al. también registraron episodios no epilépticos psicógenos (PNES), algunos de más de treinta minutos. Es información relevante cuando el capítulo compara duración y estados psicofisiológicos. Incluirla como evidencia de que duración prolongada no excluye por sí sola todas las alternativas naturales. No equivale a diagnosticar PNES, disociación o enfermedad a White, ni explica automáticamente una descripción precisa de información oculta. Son categorías distintas; evitar tratarlas como sinónimos de trance religioso.

**C6-06 — P1. Albany/Nueva York.** §5 y nota 12 atribuyen a Albany la resolución contra manifestaciones no bíblicas siguiendo Douglass. C4 distingue una reunión de Nueva York de mayo y su relación con Albany. El ejemplar consultado de Douglass efectivamente la atribuye a Albany; **no se ha cotejado aquí el impreso de *Advent Herald* del 21-V-1845 que resuelva el origen exacto**. Registrar la discrepancia y verificar adopción original, repetición y publicación antes de declarar equivocada una localización. No confundir fecha de reunión con fecha de periódico.

### ¿Qué problemas menores y de escritura aparecen?

**C6-07 — P2. Contexto versus causa.** §7 usa “Influyeron claramente” sobre las expectativas. La coincidencia temática está documentada; influencia causal concreta es una interpretación probable o posible según el detalle. Preferir “Es probable que influyeran en la interpretación y narración; no está demostrado cuánto determinaron el estado o su contenido”.

**C6-08 — P2. Resumen del accidente.** §2 lo clasifica correctamente como probable en su núcleo. §13 lo incluye en el párrafo iniciado por “Está establecido”. Separar el hecho de que ella lo relató de la probabilidad histórica del accidente y de la lesión neurológica indeterminada.

**C6-09 — P3. Densidad.** Todas las preguntas son neutrales, pero respuestas y notas acumulan varias discusiones clínicas. Dar primero la explicación sencilla y remitir detalles de selección de muestra al aparato de fuentes. No eliminar las reservas que cambian la fuerza del argumento.

### ¿Qué dice realmente la evidencia médica y qué no dice?

Fuente cotejada: [Larsen et al., “Duration of epileptic seizure types: A data-driven approach”, *Epilepsia* 64 (2023), pp. 469–478](https://pmc.ncbi.nlm.nih.gov/articles/PMC10107943/), tablas 1–2, métodos y resultados. La mediana de 42,5 segundos es correcta. Los valores extremos y los criterios de exclusión deben acompañarla. **No hay muestra clínica de White.**

La respuesta adventista de [*Ministry*, agosto de 1984](https://www.ministrymagazine.org/archive/1984/08/was-ellen-g.-white-an-epileptic) argumenta contra la hipótesis de Hodder; sus expresiones de imposibilidad exceden una revisión retrospectiva sin exploraciones. El capítulo lo reconoce, y eso resiste. El trabajo de [Hodder](https://www.nonegw.org/egw79.shtml) y el de [Couperus](https://www.nonegw.org/headinjury.shtml) se consultaron en reproducciones: conseguir la publicación original de cada uno y distinguir afirmaciones médicas generales de diagnóstico personal.

La revisión de During et al. sobre trastornos de trance/posesión requiere texto completo para cotejar todos sus datos; se identificó [PMID 21507280](https://pubmed.ncbi.nlm.nih.gov/21507280/), pero no se obtuvo aquí el artículo íntegro. No puede trasladarse su población clínica a todo trance religioso ni a White.

### ¿Cuál es el mejor intercambio argumental?

Defensa: duración informada, comunicación organizada y evolución de experiencias hacen insuficiente una etiqueta única de crisis típica. Objeción: algunos fenómenos pueden ser compatibles con epilepsia o disociación; productividad y sinceridad no las excluyen. Respuesta: compatibilidad parcial no identifica causa sin signos positivos y no explica automáticamente todos los episodios. Contrarespuesta: exigir confirmación clínica imposible no debe convertirse en razón para asignar probabilidad especial a una causa divina igualmente no verificada.

La hipótesis natural y la religiosa deben enfrentar las mismas historias con el mismo grado de fiabilidad. No toda experiencia sin diagnóstico es evidencia positiva de revelación; tampoco toda experiencia culturalmente reconocible es prueba de causa natural única.

### ¿Qué conclusiones requieren recalibración y cuáles resisten?

| Conclusión | Clasificación |
|---|---|
| White relató un accidente infantil y enfermedad prolongada | Establecido documentalmente |
| Ocurrió un golpe grave en el núcleo descrito | Probable; gravedad neurológica indeterminada |
| El golpe produjo las visiones | Hipótesis posible, no demostrada |
| Una sola crisis focal típica explica todos los episodios largos | Débil si los relatos son fiables; no diagnóstico excluido de manera absoluta |
| Disociación o trance describe rasgos | Posible/compatible; mecanismo causal indeterminado |
| Contexto influyó en interpretación y narración | Probable en términos generales |
| Todo fue fraude consciente | No establecido |
| Una causa divina quedó demostrada por descarte | No establecido |

**Falsación:** notas clínicas contemporáneas con patrón repetido, una historia neurológica independiente, documentos de preparación deliberada de un episodio o información concreta inaccesible registrada antes de su confirmación podrían cambiar el peso de las hipótesis. Ni la falta de EEG ni la posibilidad abstracta de una enfermedad cierran la investigación.

## ¿Qué resiste y qué debe corregirse en el capítulo 7?

**Archivo:** `capitulos/07-predijo-ellen-white-acontecimientos-que-no-podia-conocer.md`.

### ¿Cuál es su pregunta y qué intenta demostrar?

Pregunta principal: si existen anuncios anteriores, suficientemente específicos e inesperados que favorezcan revelación. Secundaria, igualmente decisiva: si existen incumplimientos que debiliten la pretensión. Conclusión explícita: ningún caso analizado obliga por sí solo a sobrenaturalidad; 1856 tiene incumplimiento literal establecido, con defensa condicional discutida. Implícitamente ofrece una prueba separable de otros fenómenos y deja pendiente el peso global.

### ¿Cuál es el estado general?

**Buen contraste de casos favorables y adversos; necesita afinar el peso de 1856 y la independencia documental de 1888.** El punto de mayor riesgo no es una fecha menor: es que una explicación posible termine neutralizando una dificultad que el marco metodológico había llamado seria.

### ¿Qué cronologías y estados corresponden a cada caso?

| Caso | Antes del resultado y documentación | Qué queda en pie / qué falta |
|---|---|---|
| Parkville, 12-I-1861 | Relato publicado en 1892, pp. 236–237; Loughborough dice apoyarse en diario | No se cotejó entrada original; no certificar cada palabra como escrita en 1861 |
| Guerra en agosto de 1861 | RH 27-VIII-1861, después de Bull Run; visión fechada 3-VIII | Juicios anteriores a fases posteriores, pero guerra y tensión ya públicas |
| Inglaterra, enero de 1862 | Folleto No. 7 de 1862; desenlace sin guerra británica-estadounidense | Modalidad de “when” y condición requieren análisis; no convertirlo en acierto |
| Jerusalén, 1851 | Texto anterior a Israel moderno, con contexto de expectativas de restauración | Referente de “built up” discutido; 1948 por sí solo no decide |
| Battle Creek, 1901–1902 | Lt 138 de 1901 debe cotejarse materialmente; incendios posteriores en 1902 | Imagen de fuego, temor y advertencia condicionada no son una sola predicción incondicional precisa |
| San Francisco/Oakland, 1902–1906 | Advertencias generales de 1902; visión fechada 16-IV sólo narrada después del terremoto | No está demostrada descripción específica registrada antes del 18-IV-1906 |
| Propiedades del sur de California, 1902–1904 | Carta 157 de 1902; Paradise ya en venta; compra después | Anticipación práctica compatible con mercado; acceso real y costo original por comprobar |
| Hull, 1862 | Advertencia sobre un riesgo ya visible y condicional | No demostrar conocimiento inaccesible del futuro ni independencia del desenlace |
| Messenger Party, 1855 | Advertencia impresa antes del cierre; precisión espectacular relatada después | Separar frase previa, detalle tardío y resultado comunicado por el propio bando |
| Asistentes de 1856 | Folleto original de 1856, p. 22; todos pertenecían a generación ya desaparecida | Incumplimiento de lectura literal establecido; alcance de condición posterior discutido |
| Creyentes de 1888 | RH 31-VII-1888, p. 482, anterior al agotamiento de esa generación | Reiteración documentada; menos clara atribución de esa oración a nueva revelación |

### ¿Hay un problema crítico confirmado en la conclusión de 1856?

**C7-01 — P1/P2 argumental. Condición posterior y peso de 1856.** §§14, 16 y 17 reconocen que la condición no está junto a la frase de 1856. No se confirmó que el capítulo declare auténtico el anuncio ni que lo exonere de una dificultad seria. Su frase de §16, “impide describir con precisión el caso como una simple excusa inventada después de que todo estuviera perdido”, rechaza correctamente esa caricatura concreta. El punto pendiente es cuánto pesa la defensa de 1883: **no prueba que la condición perteneciera al sentido original, fuera comunicada a los asistentes o existiera antes de tensiones previas con la expectativa**.

Se debe conservar el mejor argumento favorable: la condicionalidad bíblica puede ser implícita y White formuló una teología de demora antes del cierre moderno del caso. Se debe conservar la mejor objeción: la frase asigna destinos a un grupo identificable bajo voz angélica; no expresa dependencia y no aconteció en su sentido ordinario.

Recalibración propuesta: “La lectura literal no se cumplió y constituye una dificultad seria para la atribución profética de este mensaje. Existe una defensa condicional documentada en 1883; todavía no se ha demostrado que esa condición explique legítimamente el anuncio de 1856. El alcance teológico de la dificultad permanece discutido”. Evita tanto veredicto global anticipado como falsa equivalencia de apoyos.

### ¿Qué problemas importantes aparecen?

**C7-02 — P2. 1888 no es mera repetición de fuente.** §15: “no debería contarse como una segunda ‘profecía fallida’ independiente”. Correcto si rechaza sumar puntos mecánicos; excesivo si elimina una afirmación publicada distinta por compartir doctrina. Es **otro documento, otra fecha y otra formulación**, que aporta evidencia de persistencia de la expectativa. No es una nueva línea independiente para la verdad de la misma hipótesis ni tiene la misma atribución revelatoria que 1856. Describir esas relaciones, en vez de llamar indistintamente “dependencia” a copiar una fuente y a compartir una creencia.

**C7-03 — P1. Diario de Parkville.** La declaración del prefacio de Loughborough de que llevaba diario desde 1853 mejora el caso frente a memoria desnuda. No demuestra que las palabras de p. 236 fueran anotadas antes de la guerra, que la entrada no fuera ampliada ni que se midieran plazos. Obtener imagen, procedencia, secuencia de cuaderno y edición de la entrada del 12-I-1861. No rebajar todo a recuerdo puro ni elevarlo a transcripción literal ya verificada.

**C7-04 — P1. Documentos privados de Battle Creek y California.** Las páginas de Lt 138 (1901), Lt 157 (1902) y Ms 4 (1883) no pudieron cotejarse íntegramente en sus originales materiales. Solicitar copia de archivo y fijar fecha de escritura/envío, receptor, circulación y primera publicación. La fecha de catálogo no basta para probar que un destinatario tuvo el texto antes del desenlace. Esta limitación no demuestra que las fechas sean falsas.

**C7-05 — P2. Mercado y costo.** Paradise se ofrecía por 11.000 dólares en 1902 y se compró por 4.000 en 1904 según una historia de 1989. Ese cotejo apoya la trayectoria de precios, pero la afirmación de White compara con **costo original**, no necesariamente con precio pedido en 1902. Verificar costo de construcción, valor del inmueble, fecha de visita/carta y documentación de compraventa. Disponibilidad pública del mercado no prueba que ella conociera precisamente cada cifra.

**C7-06 — P1/P2. Comparación con expectativas contemporáneas.** §12 usa el terremoto de Hayward de 1868 como antecedente. Para evaluar “no podía inferir”, falta un conjunto pertinente de pronósticos contemporáneos sobre guerra, secesión, sanatorios y ciudades, con fechas. Un peligro conocido no demuestra que White tuviera la noticia; un pronóstico acertado tampoco implica que nadie pudiera hacerlo. No calcular probabilidades ficticias sin una base comparable.

**C7-07 — P2. Umbral de prueba.** Que ninguna predicción “obligue” a sobrenaturalidad es un umbral demasiado absoluto para contestar cuánto favorece una hipótesis. Valorar si alguna reduce razonablemente explicaciones ordinarias aun sin demostración deductiva. La prueba más fuerte requeriría documentación previa específica y exclusión razonable de canales, no omnisciencia del auditor sobre toda posibilidad imaginable.

### ¿Qué evidencia nueva o contexto material se encontró?

Se obtuvo y examinó el [facsímil de No. 2 (1856)](https://www.truthseeker.church/_files/ugd/ff8319_823527d4e0d945b7a56ef846eb23a7db.pdf), **p. 22**. El anuncio se refiere a la compañía presente; la nota inferior identifica a Clarissa M. Bonfoey y dice que murió tres días después y se consideró incluida entre quienes morirían. Es contexto material ausente del desarrollo de C7 aunque su nota 20 alude genéricamente a muertes tempranas.

Incluir ambos límites: la nota ofrece una aplicación temprana favorable al primer subconjunto, pero fue impresa después de la muerte y no demuestra que White identificara por anticipado a Bonfoey. La muerte concreta requiere registro contemporáneo independiente si se usa como hecho corroborado. **No convierte el subconjunto superviviente en condicional ni soluciona su incumplimiento.** Tampoco omitirla porque dificulta una lectura crítica simple.

Se cotejó directamente [RH del 31-VII-1888, p. 482](https://documents.adventistarchives.org/Periodicals/RH/RH18880731-V65-31.pdf): el grupo de quienes entonces creían y estarían vivos aparece realmente en el texto. El contexto exhortativo no borra esa referencia temporal.

Se cotejó [RH del 27-VIII-1861](https://documents.adventistarchives.org/Periodicals/RH/RH18610827-V18-13.pdf), “Slavery and the War”, y [Russell, historia de escuelas de enfermería de San Diego (1989)](https://sandiegohistory.org/journal/1989/april/hospital/). Este último es fuente secundaria tardía del resultado, no testigo de la redacción de la carta de 1902.

### ¿Qué fuentes requieren reemplazo y qué falta verificar?

Reemplazar compilaciones por folletos originales No. 1, 2 y 7 y periódicos correspondientes. Para Inglaterra, Jerusalén, incendios y terremoto, completar comparación de primera edición, reimpresiones, cartas y relato posterior. Conseguir diario de Loughborough, actas de reuniones/receptores de cartas y documentos inmobiliarios. Corregir la edición consultada de *Profecías dramáticas*: el ejemplar auxiliar es 2009, no demuestra por su nombre ser 2013.

Las predicciones amplias de Douglass sobre espiritismo, papado y Estados Unidos, presentes en esa obra, **no están agotadas por estos casos del capítulo**. Son temas pendientes del libro, con texto inicial, fecha, especificidad y criterios de cumplimiento por fijar; no declararlas confirmadas ni refutadas porque se auditó Parkville.

### ¿Qué problemas menores de estructura aparecen?

**C7-08 — P3. Balance y repeticiones.** §§16–17 reiteran casi todo el balance. Conservar una síntesis y la pregunta siguiente. Los encabezados son preguntas; el de §17 (“qué queda demostrado”) puede mantenerse si las respuestas explican qué no alcanza ese grado. Mejor preguntar “¿Hasta dónde llega la evidencia?” si se quiere evitar expectativa de prueba definitiva.

### ¿Qué resiste y qué podría cambiarlo?

Resisten: no identificar una advertencia urbana amplia con anuncio preciso de terremoto; no fechar una narración posterior como si hubiera sido impresa antes; no decidir Jerusalén sólo por 1948; no inferir independencia del resultado en conductas influidas por una amonestación; no negar el problema literal de 1856. Es fuerte también la distinción entre pronóstico humano acertado y conocimiento inaccesible.

**Falsación:** un diario autenticado previo con predicción concreta; constancia de recepción previa de cartas; evidencia de modificación posterior de un anuncio; una condición original de 1856 reconocida por destinatarios; o datos que muestren una lectura distinta de “algunos presentes”. La defensa no debería poder invocar cualquier conducta posterior como condición suficiente sin documento o argumento contextual controlable.

## ¿Qué resiste y qué debe corregirse en el capítulo 8?

**Archivo:** `capitulos/08-conocio-ellen-white-cosas-que-no-podia-saber-por-medios-normales.md`, versión del PR 5.

### ¿Cuál es su pregunta y qué intenta demostrar?

Evalúa conocimientos ocultos, vías de información, Faulkhead, Salamanca, Rochester, cartas, Daniels y omisiones. Conclusión: algunos episodios conservan interés, pero no se ha excluido razonablemente información humana; hay errores concretos sin evidencia suficiente de una red de fraude. Implícitamente distingue información real, presunta inaccesibilidad y atribución revelatoria.

### ¿Cuál es el estado general?

**Borrador metodológicamente cuidadoso, especialmente en Rochester y Daniels.** Resisten varias correcciones del PR; quedan pendientes documentos primarios capaces de elevar o reducir el peso de Faulkhead y Salamanca. No presentar las posibilidades naturales como mecanismos ya probados.

### ¿Qué problemas críticos aparecen?

No se confirmó un error P0 nuevo que invierta los balances de Rochester o Daniels. **Antes de publicar cualquier afirmación de conocimiento sobrenatural**, la precisión y anterioridad de señales, escenas y mensajes deben quedar mejor documentadas. El capítulo actual mantiene reservas; conservarlas y completar los expedientes señalados abajo.

### ¿Qué problemas importantes requieren investigación?

**C8-01 — P1. Faulkhead: el texto previo y las capas del relato.** §§4–5 reconocen que no se conservan las cincuenta páginas como carta única. Esa ausencia impide verificar contenido preparado en 1891 frente a conversación de diciembre de 1892. No usar la fecha de un testimonio general de la editorial como fecha de todo detalle personal.

Lt 46 lleva fecha de 13-XII-1892, pero su narración retrospectiva debe compararse con adiciones, fecha de envío y copia. La carta/edición que combina material de varios días necesita identificación de capas. *Experiences in Australia* también reúne episodios de 1891 y 1892 bajo una organización editorial; la fecha de encabezado de la sección no fecha todo su contenido.

**C8-02 — P1. Señales masónicas: falta la variable decisiva.** El relato próximo de White y el recuerdo de Faulkhead de 1908 dan apoyo a que él interpretó un movimiento como señal. No se dispone de descripción inequívoca suficiente para reproducir el gesto, comprobar grado, exclusividad ni probabilidad de coincidencia. La memoria del destinatario dieciséis años después no sustituye esa identificación.

La defensa más fuerte es el reconocimiento espontáneo por un miembro competente y la referencia cercana al encuentro. La objeción más fuerte es que precisión y carácter secreto dependen del mismo participante, con vías de aprendizaje no reconstruidas. La réplica favorable correcta es que no hay prueba de transmisión ordinaria; la contrarespuesta correcta es que ausencia de vía identificada no equivale a exclusión positiva. Ningún gesto genérico parecido prueba por sí solo copia.

**C8-03 — P1. Faulkhead y registros masónicos.** El capítulo incorpora afiliación/reafiliación de 1894/1896 y membresía en 1923 a través de Hook/Devine. Es una corrección importante frente a ruptura definitiva. Aquí no se autenticaron los registros originales de logia. Obtener imágenes, identificación de organización y miembro, fechas de baja/alta y alcance de cada registro. No presentar una noticia secundaria como inspección del registro ni usar la persistencia de membresía para desacreditar automáticamente el relato gestual.

**C8-04 — P1. Salamanca: antes de la escena, antes del discurso y antes de publicarse son fechas distintas.** Se cotejó la edición que identifica **Ms 40, 1890** pero aclara **escrito en marzo de 1891**. El número archivístico no prueba redacción en 1890. C8 ya lo señala; es un punto sólido que debe preservarse.

Falta separar qué detalles estaban escritos antes de la reunión privada del 7-III-1891, cuáles antes de narrarla el 8-III y cuáles sólo aparecen después. Un apunte de visión de noviembre de 1890 con contenido general no autentica automáticamente la descripción posterior del encuentro. Obtener imagen secuencial del diario, cambios de tinta/papel si el archivo los conserva, primera copia y testimonios con su fecha de escritura.

**C8-05 — P2. Vía de W. C. White.** Su presencia o comunicación posible es evidencia de oportunidad, no de transmisión efectiva. El análisis crítico de horarios merece cotejo con diarios y cartas originales. No invertir la carga de prueba exigiendo que el defensor demuestre que nunca pudo hablar ni afirmar que efectivamente informó sin documento.

**C8-06 — P2. Testigos de reconocimiento no prueban inaccesibilidad.** Varios asistentes pueden corroborar que White describió una escena y que reconocieron detalles. Su número no excluye información previa ni fecha cada redacción. Precisar dependencia, solicitudes de recuerdo y contacto entre declarantes; no eliminar por compartir ocasión ni multiplicar por cada reproducción posterior.

### ¿Qué casos fueron cotejados y cómo queda su genealogía?

| Caso | Fuentes y secuencia | Qué sobrevive |
|---|---|---|
| Rochester, episodio atribuido a 1852 | Loughborough RH 1884 → mismo autor 1892 → mismo autor 1909 → compilación 1987 y autores modernos | Una línea principal retrospectiva, con detalles crecientes |
| Rochester, fecha | Loughborough: primer sábado de octubre; James, RH 14-X-1852: retorno día 6 | Incompatibilidad/ambigüedad de fecha que el PR ya reconoce |
| Rochester, identidad | 1892 nombra Mrs. Riggs en escena siguiente; 1909 identifica mujer como esposa sin nombrar al viajero | No basta para nombrar Riggs al hombre |
| Daniels | Acusación del *Advocate Extra* citada por oponente → Daniels, 25-VII/publicación 14-VIII-1883 → Canright/Nichol | Error de persona y lugar reconocido por Daniels; niega atribución visionaria de esa información |
| Faulkhead | Relato próximo de White → recuerdos del destinatario 1893/1908 → A. L. White, Douglass, biografías | Corroboración parcial de encuentro, no varias certificaciones independientes del gesto |
| Salamanca | Relatos/diario → selección documental del Estate → defensas/críticas modernas | Historia documental compleja; cada recuerdo necesita fecha y relación con anteriores |
| Stephen Smith | Farnsworth 1885, publicado/transcrito mucho después → biografía de A. L. White | No contar biografía y Farnsworth como dos confesiones independientes |
| Fuller | Testimonio publicado 1869 + hechos judiciales posteriores + narración tardía de Canright | Falta de omnisciencia no es contradicción de cada mensaje; intervalos específicos pendientes |

### ¿Qué confirma el cotejo de Rochester?

Se cotejaron [RH 4-III-1884, p. 154](https://documents.adventistarchives.org/Periodicals/RH/RH18840304-V61-10.pdf), [*Rise and Progress*, pp. 171–173](https://documents.adventistarchives.org/Books/RP1892.pdf), [PUR 15-VII-1909, p. 1](https://documents.adventistarchives.org/Periodicals/PUR/PUR19090715-V08-50.pdf) y [“Eastern Tour”, RH 14-X-1852, p. 96](https://documents.adventistarchives.org/Periodicals/RH/RH18521014-V03-12.pdf).

La separación del PR entre anuncio de transgresión de “uno” de los mandamientos y precisión sexual en la confesión posterior es correcta. Paw Paw y coincidencia de “mismo día” aparecen en una versión posterior. No se encontró un documento de 1852 que registre el secreto antes de la llegada del hombre. El retorno del día 6 obliga a dejar abierta la fecha del primer sábado; la cronología tradicional no queda íntegramente autenticada.

**C8-07 — P2. Frases de conocimiento inaccesible.** La conclusión debe hablar de “Loughborough recordó que…” cuando el detalle procede de esa línea. No pasar de probable encuentro/reconocimiento a secreto realmente inaccesible. La versión de 1884 mejora la antigüedad frente a 1987, pero sigue distante unos treinta y un años del episodio.

### ¿Qué confirma el cotejo de Daniels?

El [suplemento de RH 14-VIII-1883, p. 10](https://documents.adventistarchives.org/Periodicals/RH/RH18830814-V60-33s.pdf) contiene la réplica firmada por Daniels el 25-VII. Reconoce confusión de nombre y de localidad; explica una información recibida de un hombre. No presenta el hecho como visión. El PR distingue correctamente el error reconocido de la versión acusatoria que dice “el Señor me mostró”.

La réplica es interesada y contemporánea a la polémica, no necesariamente a la conversación original. Debe encontrarse el *Advocate Extra*, la declaración del informante y cualquier carta de White sobre el encuentro para avanzar. [Canright, 1919, cap. 17](https://www.nonegw.org/canright/can17.htm) y Nichol son interpretaciones posteriores; no equivalen a dos nuevos testigos de la escena. Rea no resuelve la identificación de informantes por citar la anécdota.

### ¿Qué fuentes requieren reemplazo y qué evidencia adicional conviene?

**C8-08 — P2/P3. Nota 2 enlaza una compilación distinta.** Su etiqueta anuncia 5T, pp. 683–687, pero el enlace abre **Testimony Treasures, vol. 2 (1949), capítulo 41**. El contenido reproduce material de 1889, pero la referencia debe decir qué edición se está leyendo. Mejor sustituir por **No. 33 (1889), pp. 211–218**, ya localizado en facsímil, con correspondencia a 5T.

Para Faulkhead, reemplazar biografía por las cartas completas de 1893 y 1908 y el registro masónico. Para Salamanca, sustituir la conclusión de un autor moderno por el diario y testimonios fechados, sin perder la comparación crítica. Para Smith, localizar la carta original de Farnsworth de 1885. Para Fuller, obtener registro judicial contemporáneo y texto inicial de No. 18. Los expedientes no se completan simplemente abriendo otra reproducción de la misma historia.

Nueva verificación directa: [Ms 40, editado con aclaración “Written in 1891”](https://ellenwhiteresearch.com/works/1888/115); [*Experiences in Australia*, sección con episodios de 1891/1892](https://ellenwhiteresearch.com/works/EA/3); [W. C. White sobre circulación de cartas y noticias](https://whiteestate.org/legacy/issues-integrity-html/). Son reproducciones útiles; no se las presenta como autógrafos autenticados. El último documento debe fecharse y situarse como declaración favorable de un participante, no como demostración de cada vía específica.

### ¿Qué problemas menores de estructura aparecen?

**C8-09 — P3. Doble conclusión.** §§12–14 repiten el balance. §13 pregunta si queda un caso difícil de explicar y responde con reservas que §14 vuelve a distribuir. Puede conservarse una respuesta conjunta con una dificultad pendiente. Títulos y subtítulos son preguntas. La pregunta principal sobre “no podía saber” exige un umbral razonable, no exclusión absoluta de toda posibilidad imaginable.

### ¿Qué resiste y qué podría cambiarlo?

Resisten: la afiliación de Faulkhead no era un secreto inaccesible demostrado; las señales conservan interés sin exclusividad verificada; Salamanca requiere capas documentales; Rochester es retrospectivo y creciente; Daniels documenta error sin demostrar allí falsa visión; la existencia de asistentes y correspondencia no prueba una conspiración; omitir un pecado no supone omnisciencia reclamada.

**Falsación:** una carta previa con detalle secreto preciso y recepción comprobada, descripción reproducible de señales, testimonios independientes escritos antes de circular el relato, un registro de transmisión efectiva por William, o el original crítico de Daniels. Cualquiera podría alterar el balance. No rellenar las ausencias con “hubo informante” ni con “sólo Dios podía saberlo”.

## ¿Qué problemas atraviesan más de un capítulo?

### ¿Qué contradicciones y tensiones deben distinguirse?

| Relación | Tipo de problema | Corrección necesaria |
|---|---|---|
| C5 §12 / C6 hipótesis abiertas | Tensión lógica real: exigir no literalidad desde fisiología ordinaria cierra una alternativa que C6 mantiene abierta | C5-02: separar incompatibilidad ordinaria, calidad del testimonio y causa |
| C4–C5 / carta de James 1848 | Omisión documental compartida | Añadir fecha de carta, conservación y alcance; no confundir primera carta con primera impresión general |
| C2 §6 / C7 §§14–17 | Tensión de peso, **no contradicción formal demostrada** | Definir desenlace, relación con 1856 y fuerza de condición tardía |
| C5 / C6 duración de estados | Riesgo de fiabilidad asimétrica | Mismo grado de confianza para duración al evaluar apnea, crisis y trance |
| C6 §2 / §13 | Resumen susceptible de elevar probable a establecido | Separar relato documentado, accidente probable y lesión indeterminada |
| C4 / C6 sobre Foy | C4 omite paralelos concretos que C6 trata de manera general | Comparación textual y cronológica común, con dirección y acceso |
| C4 / C6 sobre Albany/Nueva York | Localización pendiente de resolver en fuente primaria | No adoptar una paráfrasis de Douglass como solución sin impreso de 1845 |
| C3 / C7–C8 | La negación de dictado/infalibilidad universal no resuelve cada atribución concreta | Fijar qué presentó como revelado antes de clasificar un error como ordinario |
| C5 / C8 / criterio de independencia | Misma ocasión, mismo autor y misma doctrina se tratan a veces como dependencias equivalentes | Distinguir independientes observadores, documentos, ocasiones e inferencias |
| Matriz y fichas / capítulos revisados | Algunas síntesis tienen menos reservas que el texto principal | Sincronizar; una ficha anterior no debe reintroducir una afirmación eliminada |

No se encontró en estos ocho capítulos una conclusión final explícita que declare auténtica o falsa a White. Varias conclusiones locales son compatibles precisamente porque responden a preguntas distintas. No fabricar una contradicción entre “afirmó revelación” y “no la hemos verificado”: la primera describe una pretensión y la segunda evalúa evidencia.

### ¿Qué genealogías impiden multiplicar artificialmente la evidencia?

| Línea principal | Reproducciones o desarrollos | Cómo pesarla |
|---|---|---|
| Ellen a Jacobs 1845/1846 | Hoja 1846 → folleto 1847 → 1851 → recuerdos/autobiografía → compilaciones | Una tradición autoral revisada, no seis observadores de la primera visión |
| Periódico del juicio Dammon 1845 | Hoyt 1987 → ensayo del Estate → capítulos actuales | Una base periodística; sus testigos internos tienen posiciones distintas |
| Nichols | Carta temprana a Miller y relato retrospectivo de Randolph → obras posteriores | Separar documentos, objeto y fecha; no sumarlos como testigos distintos de un mismo detalle |
| James 1848 | Registro/copia → colección de puerta cerrada → biografía/compilaciones | Una línea temprana en fecha declarada; autenticación del soporte pendiente |
| James 1868 | Butler/Loughborough y compilaciones de descripciones generales | Influencia probable/posible; no declarar copia total sin cotejo de vocabulario y acceso |
| Declaraciones reunidas por Loughborough 1890–1897 | 1892 → 1905 → biografías/Douglass | Una declaración reproducida no se vuelve testigo adicional; declarantes distintos requieren evaluación propia |
| Loughborough, cantero 1891/1892 | Versiones posteriores | Misma voz, fecha 1863/1862 discordante; no corroboración cronológica independiente |
| Loughborough, Rochester 1884/1892/1909 | *Miracles in My Life* 1987 → Douglass/otras obras | Una voz con ampliaciones; no cuatro líneas independientes |
| Daniels 1883 | Canright 1919 / Nichol / autores modernos | Volver a acusación y réplica; no confundir comentario con testimonio nuevo |
| White/Faulkhead | A. L. White → Douglass/Devine | Dos participantes con fechas distintas; verificar contaminación, selección y contenido compartido |
| Salamanca | Diario y recuerdos → colección del Estate → críticas y defensas | El expediente compila voces, pero cada una necesita fecha y relación con relato público |
| Merritt Kellogg 1890/1906 | Loughborough / Couperus | Mismo observador con interpretación cambiante, no dos exámenes clínicos |
| Promesa de 1856 / afirmación de 1888 | Tradición común de inminencia | Dos documentos diferentes; misma familia de expectativa, distinta atribución y evidencia |

No se debe contar ni descartar por cantidad. Un escrito privado temprano autenticado puede pesar más que muchas biografías. Un testigo tardío puede conservar información correcta y, aun así, no controlar las palabras exactas o la fecha. La dependencia debe probarse o calificarse como probable, no presumirse siempre que dos personas pertenecen a la misma iglesia.

### ¿Qué cronología global necesita controlarse?

Cada caso debe registrar cinco fechas sin fusionarlas:

1. experiencia o acontecimiento atribuido;
2. declaración oral que se dice emitida;
3. redacción conservada, con capas si existen;
4. copia, primera publicación y edición consultada;
5. supuesto cumplimiento o información que habría confirmado el mensaje.

Aplicaciones urgentes: diciembre de 1844 frente a 1845/1846; el episodio de Hannibal de 1848 y la fecha de su registro; 1862/1863 en el cantero; diario alegado de Parkville frente a impresión de 1892; 1856 frente a formulación condicional de 1883; material de 1891/1892 de Faulkhead; Ms 40 “1890” escrito en 1891; Rochester “primer sábado” frente a retorno del 6 de octubre; visión fechada 16 de abril de 1906 relatada después del terremoto; ediciones de 1888/1911 de GC.

Un catálogo moderno que titula un documento con un año no certifica autógrafo, envío ni recepción ese año. Un PDF con portada antigua y apéndice de 1944 no data todo el PDF en el año antiguo. Una edición electrónica con códigos de párrafo no es necesariamente facsímil. Estas distinciones deben aparecer en las notas decisivas.

### ¿Qué afirmaciones son especialmente sólidas?

- White reclamó mensajes de origen divino y autoridad religiosa; el término “mensajera” no elimina esa pretensión.
- Admitió lenguaje propio, asistencia editorial y una distinción entre asuntos comunes y mensajes que consideraba revelados.
- La Biblia como norma declarada y la autoridad reclamada para testimonios no son proposiciones incompatibles; la segunda tampoco se vuelve opcional automáticamente.
- Existen testimonios tempranos de experiencias públicas inusuales. Su interpretación sobrenatural no queda establecida por ese dato.
- Numerosos detalles físicos célebres dependen de memoria retrospectiva; las fuentes no contienen una certificación instrumental de apnea prolongada.
- El anuncio de 1856 y la afirmación generacional de 1888 están realmente documentados; la lectura temporal ordinaria no se cumplió.
- La historia de Rochester no debe fecharse por la compilación de 1987, pero sus fuentes anteriores siguen siendo retrospectivas y de una misma voz.
- Daniels reconoció un error en persona/localidad y negó en su réplica el origen visionario que sus críticos atribuían a esa información.
- Una explicación natural posible no es una explicación natural demostrada. Un hecho todavía sin explicación no verifica una causa divina.

Estas son conclusiones locales sobre documentos y límites de inferencia. No constituyen una certificación global de autenticidad o falsedad.

### ¿Qué afirmaciones son especialmente vulnerables?

- Que cada minuto de una visión larga transcurrió sin ventilación, que médicos certificaron ese hecho científicamente o que la voz no necesitó flujo de aire.
- Que una incompatibilidad fisiológica **obliga** a no literalidad, sin argumentar la relación con las hipótesis que el libro mantiene abiertas.
- Que una versión posterior con lugar, mandamiento y coincidencia temporal equivale al contenido anunciado antes de conocer el resultado.
- Que las condiciones generales de 1883 explican con suficiente seguridad lo que entendieron los asistentes de 1856.
- Que el número de gestos o su carácter secreto en Faulkhead ya excluye aprendizaje, información o coincidencia.
- Que el año “1890” del manuscrito Salamanca prueba que todos sus detalles estaban escritos en 1890.
- Que fuente humana legítima significa inmunidad frente a toda falsa atribución de origen, o que semejanza textual significa automáticamente fraude.
- Que una carrera productiva excluye enfermedad neurológica, o que duración larga identifica un trastorno específico.
- Que varias reproducciones o varias formulaciones de una creencia deban contarse, respectivamente, como varios testigos o como una única afirmación sin valor adicional.

### ¿Qué cuestiones todavía no están investigadas de manera suficiente?

**Dentro de los capítulos:** cronología material de cartas privadas; originales de registros de respiración; comparación exhaustiva Foy/White/2 Esdras; recepción de 1856; diario de Parkville; fuentes previas efectivamente disponibles; diarios Salamanca; gesto masónico y registros de logias; expediente completo Daniels; cartas oportunas comparadas con texto previo y desenlace.

**Para el libro completo:** préstamos literarios con atribución de origen caso por caso; historia de asistentes y modificaciones de contenido; exactitud histórica de GC y revisión de 1911; afirmaciones científicas y sanitarias, con antecedentes disponibles; astronomía y relato de Bates sobre planetas; doctrinas, incluido desarrollo del santuario y puerta cerrada; frutos y ejercicio institucional de autoridad; predicciones sobre Estados Unidos, papado y espiritismo; recepción contemporánea favorable y hostil no seleccionada sólo desde archivos denominacionales; archivos judiciales y médicos externos.

La fuente de 1891 sobre fenómenos físicos también narra conocimiento astronómico que habría convencido a Bates. Es una **línea de investigación pendiente**, no corroboración ya obtenida: determinar primera atestación, palabras de White frente a identificación de planetas por Bates, número de satélites y conocimientos disponibles en cada fecha. No cerrar ese tema con la conversión de Bates ni con astronomía actual aplicada sin contexto.

Estos asuntos no prueban que el libro omita deliberadamente evidencias: marcan lo que no puede considerarse cerrado al continuar su desarrollo.

### ¿Qué fuentes primarias deberían conseguirse primero?

| Documento | Pregunta que puede resolver | Prioridad |
|---|---|---|
| James White a Hastings, 26-VIII-1848; Record Book 1, pp. 18–20, autógrafo/copia e información archivística | Testimonio temprano de respiración y procedencia de la transcripción | P1, con incorporación de transcripción ya disponible P0 |
| Diario de Loughborough, 12-I-1861, cuaderno completo y primera copia | Anterioridad y precisión de Parkville | P1 |
| No. 2 de 1856 más cartas/reacción de asistentes, registro de Bonfoey y primeras respuestas a demora | Significado original y recepción de promesa/condiciones | P1 |
| Primera impresión de Foy y facsímiles 1846/1847/1851 de White | Dirección y cambios del paralelo textual | P1, con reconocimiento del dato P0 |
| Diario y manuscritos Salamanca, 1890–1891, con procedencia y capas | Qué detalle antecede a cada reunión | P1 |
| Lt 21b y 46 de 1892; cincuenta páginas si se localizan; cartas Faulkhead 1893/1908 | Fecha y contenido de conocimiento personal/señales | P1 |
| Registros originales de logias Faulkhead | Afiliación, baja, retorno y grado | P1 |
| *Advocate Extra* y documentos de Daniels/informante/White | Si hubo atribución divina original y cuál fue la confusión | P1 |
| Lt 138 de 1901 y Lt 157 de 1902, autógrafos/copias, envío/recepción | Anterioridad de fuego y propiedades, forma de advertencia | P1 |
| Declaraciones originales de Bourdeau, Kellogg, Fowler, Castle, Lamson, Seeley y Amadon | Redacción, recopilación, cambios, independencia y fecha | P1 |
| Carta completa Kellogg 3-VI-1906 | Cambio de interpretación frente a observaciones de 1890 | P1 |
| *Advent Herald*, 21-V-1845; actas de Albany/Nueva York | Origen exacto de resolución y circulación | P1 |
| Expediente judicial Dammon y apelación | Diferencias entre periódico, sentencia y declaración posterior | P1 |
| GC 1888/1911 y materiales editoriales, cartas completas de 1906 | Uso de historiadores y límites reales de intervención de asistentes | P1 |

## ¿Qué correcciones deben hacerse primero?

### ¿Qué corresponde a P0, antes de publicar?

| Orden | Identificador | Acción concreta | Comprobación de cierre |
|---|---|---|---|
| 1 | C5-02 | Eliminar la inferencia obligatoria de no literalidad desde fisiología ordinaria; mantener abierto el examen causal | C5 y C6 usan premisas compatibles sin afirmar milagro ni descartar por definición |
| 2 | C5-01 / C4-02 | Incorporar el testimonio fechado en 1848, con procedencia y límites | Tabla separa fecha de carta, copia, impresión y medición; no sustituye 1868 por 1848 como primera impresión demostrada |
| 3 | C5-03 | Corregir las páginas de Bourdeau, Brown y Daigneau | Cada nota lleva al pasaje citado del facsímil, en página impresa |
| 4 | C4-01 | Incluir paralelos Foy/2 Esdras y revisión de bisagras; explicitar alternativas y límites | Comparación distingue experiencia atribuida, publicación, oportunidad de acceso y revisión; sin conclusión automática de plagio |

La clasificación P0 de las omisiones no significa que su interpretación causal esté decidida. Significa que publicar el balance actual sin reconocer esos documentos o datos ofrecería una base incompleta en una cuestión material.

### ¿Qué corresponde a P1, investigación adicional importante?

| Orden | Identificador | Investigación | Qué podría cambiar |
|---|---|---|---|
| 1 | C7-01 / C2-01 | Recepción y condiciones del anuncio de 1856, antes y después de 1883 | Peso de objeción al mensaje, sin prejuzgar autenticidad global |
| 2 | C7-03 | Diario original de Parkville | Anterioridad y precisión del mejor caso de guerra |
| 3 | C8-04 / C8-05 | Diario y comunicaciones Salamanca | Existencia de detalle anterior o vía ordinaria documentada |
| 4 | C8-01–03 | Originales Faulkhead, gesto y registros de logia | Precisión, exclusividad y resultado conductual |
| 5 | C4-01 / C6-05 | Comparación completa Foy/White/2 Esdras con primeras ediciones | Independencia del contenido y alcance de mediación humana |
| 6 | C5-01 / C5-05 / C5-09 | Procedencia de 1848, médicos y fecha 1862/1863 | Peso y exactitud de fenómenos públicos |
| 7 | C8, Daniels | Original de acusación, informante y correspondencia | Si el error fue presentado como revelación |
| 8 | C7-04–06 | Cartas, recepción y mercado/pronósticos contemporáneos | Precisión y explicación ordinaria de anuncios favorables |
| 9 | C3-01 / C3-03 | GC 1888 y registro del discurso de 1904 | Alcance de pretensión, uso de fuentes y evolución verbal |
| 10 | C6-02 / C6-04 / C6-10 | Selección del estudio, carta Kellogg y comparación clínica limitada | Fuerza relativa de hipótesis; nunca diagnóstico retrospectivo automático |
| 11 | C1-03 / C2-04 | Textos completos de comentarios, léxicos y estudios citados | Exactitud de interpretación exegética y consenso atribuido |
| 12 | C6-06 / C4-05 | Impreso de 1845 y expediente Dammon | Cronología temprana y límites de reconstrucción |

### ¿Qué corresponde a P2, método y argumentación?

- Diferenciar independencia de observadores, ocasiones, documentos y argumentos; conservar el valor parcial de testigos de una misma ocasión.
- Aplicar el mismo grado de fiabilidad a relatos de duración, respiración y atención al contrastar todas las causas.
- Separar definiciones teológicas de origen **reclamado** al clasificar documentos históricos.
- Precisar negación de infalibilidad personal frente a exactitud del mensaje revelado.
- Explicar cuánto cuenta una defensa condicional tardía y qué evidencia la fortalecería o debilitaría.
- Tratar 1888 como documento diferente dentro de una expectativa compartida, sin suma mecánica ni eliminación de su valor.
- Sustituir influencia “clara” por grado de inferencia apropiado y separar accidente relatado/probable de lesión no demostrada.
- Corregir 52 pacientes/53 registros/84 crisis, añadir exclusión de estado epiléptico y comparación PNES sin diagnosticar.
- Sincronizar matriz y fichas con cautelas actuales; no convertir la ficha de una auditoría previa en fuente corroborante.
- Añadir criterio de cierre de cada expediente: qué está documentado, qué se infiere, qué falta y qué podría cambiarlo.

### ¿Qué corresponde a P3, edición?

- Reemplazar enlaces cuyo destino es otra compilación o etiquetarlos correctamente; añadir correspondencia de páginas.
- Citar edición real del PDF de Douglass y describir ediciones textuales electrónicas sin llamarlas automáticamente facsímiles.
- Reducir balances duplicados y remitir a una única tabla de conclusión por capítulo.
- Mantener preguntas reales, sencillas y neutrales. Los ocho títulos y los subtítulos examinados ya tienen forma interrogativa; no corresponde inventar un incumplimiento formal.
- Abreviar el aparato técnico en el cuerpo conservando las reservas que afectan la evidencia. La profundidad puede quedar en fichas y notas.

## ¿Qué fuentes se cotejaron y cuáles siguen pendientes?

### ¿Qué significa “cotejado” en esta auditoría?

**Facsímil cotejado:** se examinó el pasaje relevante de una reproducción de páginas de la edición. No equivale a autenticar su ejemplar físico original. **Texto cotejado:** se leyó el pasaje en transcripción/edición digital; se mantienen pendientes soporte y variantes. **Localizado:** se verificó una identificación bibliográfica o acceso parcial; no se certifica todo su argumento. **Pendiente:** no se obtuvo el documento íntegro pertinente o su forma original.

### ¿Cuál es el registro de fuentes externas decisivas?

| ID | Fuente y localizador | Naturaleza / resultado |
|---|---|---|
| E01 | [Begbie, 1992, pp. 259–282](https://www.tyndalebulletin.org/article/30483.pdf) | Artículo original localizado y texto consultado; argumento teológico, no prueba histórica de White |
| E02 | [Blaylock, “Towards a Definition”](https://www.thegospelcoalition.org/themelios/article/towards-a-definition-of-new-testament-prophecy/) | Texto del autor consultado; definición discutida |
| E03 | [Schreiner, “Nuanced Cessationism”](https://www.thegospelcoalition.org/themelios/article/it-all-depends-upon-prophecy-a-brief-case-for-nuanced-cessationism/) | Texto del autor consultado; posición, no consenso |
| E04 | [Atkins, DOI](https://doi.org/10.2307/26424832) / [Bosman, revista](https://journals.ufs.ac.za/index.php/at/article/view/6193) | Bibliografía/resumen localizados; cotejo integral pendiente |
| E05 | [No. 33, 1889, pp. 211–218](https://www.truthseeker.church/_files/ugd/ff8319_ab842bbcc907444caba705ad30178d1c.pdf) | Facsímil digitalizado por CAR; autoridad/aplicación corroboradas |
| E06 | [Testimony Treasures 2, cap. 41](https://ellenwhiteresearch.com/works/2TT/41) | Compilación 1949 cotejada; no original de 1889 |
| E07 | [Reproducción de introducción GC 1888](https://text.egwwritings.org/read/725.84) | Reconocimiento de historiadores localizado; primera edición material pendiente |
| E08 | [Graybill, febrero 1994, pp. 11–13](https://www.ministrymagazine.org/archive/1994/02/visions-and-revisions?mode=app) | Texto cotejado; paralelos/variantes omitidos en C4 |
| E09 | [Foy, texto del folleto de 1845](https://documents.adventistarchives.org/Books/WFoy1845.pdf) | Edición textual posterior consultada; primera impresión facsimilar pendiente |
| E10 | [WLF 1847, reproducción](https://www.aplib.org/files/ebooks/pdf/James%20White%20-%20A%20Word%20to%20the%20Little%20Flock.pdf) | Texto y añadidos; no fechar conjunto de edición en 1847 |
| E11 | [Colección de puerta cerrada](https://whiteestate.org/about/issues1/unusual/shut-door/door-docs/) | Transcripciones y comentarios separados; James 1848 identificado |
| E12 | [Dammon, transcripción anotada](https://whiteestate.org/legacy/issues-israel_damman-html/) | Artículo periodístico reproducido; expediente judicial completo pendiente |
| E13 | [James White, *Life Incidents*, 1868, pp. 272–273](https://www.gutenberg.org/files/61394/61394-h/61394-h.htm) | Transcripción de edición cotejada; descripción general impresa |
| E14 | [Butler, RH 9-VI-1874, pp. 201–202](https://documents.adventistarchives.org/Periodicals/RH/RH18740609-V43-26.pdf) | Facsímil cotejado; descripción general, no medición clínica |
| E15 | [Loughborough, *Rise and Progress*, 1892](https://documents.adventistarchives.org/Books/RP1892.pdf) | Facsímil cotejado, pp. 95–98, 171–173, 236–237 y 247–248; errores de páginas confirmados |
| E16 | [GCB 18-III-1891, p. 145](https://documents.adventistarchives.org/Periodicals/GCSessionBulletins/GCB1891-11.pdf) | Facsímil/texto cotejados; cantero en 1863 y relatos de Biblias diferenciados |
| E17 | [Biblia conservada, White Estate](https://whiteestate.org/about/issues1/about-egw/life-and-ministry/big-bible/) | Descripción del objeto consultada; no certifica hazaña |
| E18 | [Actas 1919, reproducción *Spectrum*](https://www.andrews.edu/library/car/cardigital/Periodicals/Spectrum/1979-1980_Vol_10/22253166.READER_044.pdf) | Transcripción publicada posteriormente; reservas de Daniells, no examen de White |
| E19 | [Larsen et al., *Epilepsia*, 2023](https://pmc.ncbi.nlm.nih.gov/articles/PMC10107943/) | Estudio íntegro, métodos/tablas consultados; error pacientes/registros y exclusión confirmados |
| E20 | [Respuesta médica adventista, 1984](https://www.ministrymagazine.org/archive/1984/08/was-ellen-g.-white-an-epileptic) | Texto cotejado; juicio retrospectivo sin exploración personal |
| E21 | [Hodder, reproducción](https://www.nonegw.org/egw79.shtml) / [Couperus, reproducción](https://www.nonegw.org/headinjury.shtml) | Hipótesis consultadas; original de carta Kellogg no autenticado aquí |
| E22 | [During et al., PMID 21507280](https://pubmed.ncbi.nlm.nih.gov/21507280/) | Identificación localizada; texto completo no obtenido |
| E23 | [No. 2, 1856, p. 22](https://www.truthseeker.church/_files/ugd/ff8319_823527d4e0d945b7a56ef846eb23a7db.pdf) | Facsímil y página visual cotejados; anuncio y nota Bonfoey |
| E24 | [RH 31-VII-1888, p. 482](https://documents.adventistarchives.org/Periodicals/RH/RH18880731-V65-31.pdf) | Facsímil cotejado; referencia generacional confirmada |
| E25 | [RH 27-VIII-1861, “Slavery and the War”](https://documents.adventistarchives.org/Periodicals/RH/RH18610827-V18-13.pdf) | Facsímil cotejado; publicación posterior a guerra/Bull Run |
| E26 | [Russell, San Diego, 1989](https://sandiegohistory.org/journal/1989/april/hospital/) | Historia secundaria cotejada; $11.000 / $4.000, no prueba de carta previa |
| E27 | [Rochester RH 4-III-1884, p. 154](https://documents.adventistarchives.org/Periodicals/RH/RH18840304-V61-10.pdf) | Facsímil cotejado; atestación impresa anterior a 1892, todavía retrospectiva |
| E28 | [PUR 15-VII-1909, p. 1](https://documents.adventistarchives.org/Periodicals/PUR/PUR19090715-V08-50.pdf) | Facsímil cotejado; ampliaciones de localidad/tiempo |
| E29 | [James, RH 14-X-1852, p. 96](https://documents.adventistarchives.org/Periodicals/RH/RH18521014-V03-12.pdf) | Facsímil cotejado; retorno del día 6 |
| E30 | [Daniels, RH Supplement 14-VIII-1883, p. 10](https://documents.adventistarchives.org/Periodicals/RH/RH18830814-V60-33s.pdf) | Facsímil cotejado; error reconocido y origen humano afirmado |
| E31 | [Canright, 1919, cap. 17](https://www.nonegw.org/canright/can17.htm) | Texto posterior consultado; no sustituye documentos originales |
| E32 | [*Experiences in Australia*, sección 3](https://ellenwhiteresearch.com/works/EA/3) | Texto consultado; mezcla de episodios fechados, soporte/capas pendientes |
| E33 | [Ms 40 / *1888 Materials*, cap. 115](https://ellenwhiteresearch.com/works/1888/115) | Compilación 1987 cotejada; explicita redacción en 1891 |
| E34 | [W. C. White, integridad y circulación de información](https://whiteestate.org/legacy/issues-integrity-html/) | Declaración favorable de participante consultada; fecha y soporte por precisar |
| E35 | [Análisis crítico Salamanca](https://www.nonegw.org/salma.shtml) | Argumentos y extractos consultados; cronología exige originales, no autoridad del crítico |

Los libros suministrados de Rea y Douglass se utilizaron como **mapas de acusaciones y defensas**, no como autoridades finales ni líneas independientes de los originales que citan. El PDF español consultado es de 2009 según sus propias páginas legales. La edición EPUB de *Messenger of the Lord* permite ubicar capítulos y argumentos; se debe indicar edición/paginación de cada cita en la versión impresa correspondiente.

### ¿Qué no pudo verificarse y no debe darse por resuelto?

- Autógrafos, copias originales y fecha de envío/recepción de las cartas y manuscritos privados señalados en C3, C7 y C8.
- Primera atestación material completa de cada episodio médico, con independencia real entre declaraciones recogidas por Loughborough.
- Entrada original de Parkville; condiciones de 1856 reconocidas por destinatarios; muerte de Bonfoey mediante registro externo.
- Primera impresión íntegra de Foy y colación independiente completa de todas las versiones de la primera visión.
- Documento completo y capas de diario Salamanca; gesto masónico reproducible; registros originales Faulkhead.
- Original del *Advocate Extra*, testimonio del informante Daniels y expediente judicial Fuller.
- Periódico de la resolución de 1845 y expediente de apelación Dammon.
- Texto íntegro de todos los léxicos, comentarios exegéticos y algunos artículos médicos/académicos.

Algunas páginas de EGW Writings y ESDA bloquearon la descarga íntegra; se usaron reproducciones o resultados parciales donde se identifican como tales. Eso no demuestra falsedad del documento ni autoriza a decir que se cotejó el autógrafo. Los enlaces bibliográficos en una nota tampoco garantizan que todas sus fuentes sostengan exactamente la oración del cuerpo.

El registro complementario `auditoria-integral-2026-09-29-referencias.json` conserva los textos de las notas del corpus, sus enlaces, localizadores y huellas de archivos. Su propósito es permitir seguimiento de cada referencia. **No marca automáticamente como verificada una nota por haber descargado alguno de sus enlaces.** El estado de los argumentos se determina en este informe.

## ¿Qué significa el resultado de esta prueba para el desarrollo del libro?

La auditoría no dicta una conclusión final sobre White. Establece correcciones concretas, conserva lo que resiste y delimita expedientes que siguen abiertos. El siguiente paso útil es cerrar primero los P0 y obtener las fuentes P1 de mayor capacidad de cambio, manteniendo las conclusiones provisionales en el grado que permite cada documento.

La pregunta de control sigue siendo: **¿Qué evidencia podría demostrar que nuestra interpretación actual está equivocada?** Debe acompañar por igual las defensas, las críticas y esta propia auditoría.
