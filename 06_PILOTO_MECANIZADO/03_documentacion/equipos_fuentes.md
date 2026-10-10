# Flota de referencia para variante mecanizada compacta

Consulta: 2026-10-09, America/Lima. Estado: geometría conceptual; no selección comercial ni diseño operativo aprobado. Se prioriza **Sandvik Toro LH307 + TH315 + DD210**. El fabricante relaciona expresamente LH307 con TH315. Sus dimensiones dependen del cucharón, cabina, neumáticos, plataforma y módulo de perforación; no mezclar columnas de opciones.

## Datos primarios

| Equipo y opción | Largo × ancho × alto de transporte, m | Giro del fabricante, m | Operación y capacidad | Fuente |
|---|---|---|---|---|
| LH307, cucharón estándar bare lip 3.1 m³ | 9.327 × 2.232 × 2.252; cabina opcional aumenta altura a 2.286 | Interior R1=2.998; exterior R2=5.848; T1=3.728; T2=2.978 | 7 t; altura máxima del cucharón/protección H6=4.709. Opciones G.E.T. alcanzan 4.885 de altura y R2=6.041. | [PDF oficial LH307, edición 2024, TS3-LH307-B-04B](https://www.mining.sandvik/siteassets/product-documents/loaders/diesel-loaders/lh307-specification-sheet-english.pdf), páginas 3–4 y 6–9 |
| TH315, caja estándar 7.5 m³ | 7.710 × 2.274 × 2.395 | Interior R1=3.126; exterior R2=6.041; ancho T=3.830 | 15 t; borde de caja H3=2.238; caja levantada H2=4.096; articulación 44°. El PDF recomienda carga con LH307. | [PDF oficial TH315, edición 2024, TS3-TH315-11B](https://www.mining.sandvik/siteassets/product-documents/trucks/diesel-trucks/th315-specification-sheet-english.pdf), páginas 2 y 5–6 |
| DD210, opción seleccionada B14SNV + CFX-XS + RD314 | 7.650 × 1.400; altura conservadora 2.735 del dibujo de portador/FOPS elevado | R1=5.500; radio interno del dibujo=4.280; cornering C=2.430 | Paquete NV; mínimos de trabajo del dibujo W=2.100, H=2.530 (FOPS mínimo), con nota de holgura 100 mm. Techo hasta 5.5 m requiere definir procedimiento. | [PDF oficial DD210, edición 2026, TS2-576:04ENG](https://www.mining.sandvik/siteassets/product-documents/underground-drill-rigs/development-drill-rigs/dd210-specification-sheet-english.pdf), páginas 2 y 6–8 |

LH307: en 10% ascendente, tabla cargado indica 3.7 km/h en primera y 6.4 km/h en segunda. La tabla cubre pendientes hasta 20%; esa última columna **no es una pendiente admisible del proyecto**. El cucharón estándar tiene densidad máxima de material fragmentado 2350 kg/m³ al llenado indicado; no usar directamente la densidad in situ sintética 2700 kg/m³ para calcular volumen transportable. [Ficha LH307](https://www.mining.sandvik/siteassets/product-documents/loaders/diesel-loaders/lh307-specification-sheet-english.pdf).

TH315: tabla con resistencia a la rodadura del 3% y lock-up; en 10% cargado indica 5.7 km/h en primera y 10.5 km/h en segunda. No sustituye el cálculo de frenado, adherencia, visibilidad y control en bajada. [Ficha TH315](https://www.mining.sandvik/siteassets/product-documents/trucks/diesel-trucks/th315-specification-sheet-english.pdf).

DD210: traslado 6.5 km/h horizontal y 4 km/h en 14%; inclinación longitudinal máxima declarada 15° y lateral 3° con CFX. **15° no significa 15%**. Se selecciona la opción B14SNV + CFX-XS + RD314. La altura FOPS mínima del dibujo es 2.530 m; 1.900 m no es la altura normal con protección elevada. Los valores 24 m² y 2.83–3.44 m son generales de la gama, no promesa del CFX-XS. El paquete NV muestra perforación de techo hasta 5.5 m: requiere procedimiento. Como alternativa **distinta**, B14F+TF512 tiene largo 9.830, R1=6.230, C=2.850; sus cifras no se usan para el CFX-XS. [Ficha DD210](https://www.mining.sandvik/siteassets/product-documents/underground-drill-rigs/development-drill-rigs/dd210-specification-sheet-english.pdf).

### Vigencia y disponibilidad de las fuentes

LH307 y DD210 se descargaron directamente con HTTP 200, archivados bajo `fuentes`, texto extraído y planos renderizados/inspeccionados. TH315 se leyó en la fuente primaria indexada de la web, pero sus enlaces directos y de producto devolvieron HTTP 404 durante el intento de descarga local. Por eso TH315 es **referencia técnica de la ficha 2024**, y su disponibilidad comercial actual queda sin comprobar. No se compraron ni instalaron equipos/paquetes.

SHA256 de archivos descargados: LH307 `912e670dfa2ebaffa9541e5e547a3334f5e7f3897c92cc6a7aadeb3432bd6352`; DD210 `4206f68f588667c03efbbb7a302c055241730d497344011c5dd977b7368bba4a`.

## Hipótesis iniciales de geometría

Estas propuestas pertenecen al piloto, no a la normativa ni al fabricante:

- Principal: bóveda elíptica de ancho máximo 4.5 m y altura al eje 4.5 m, paredes hasta 3 m y alza de bóveda 1.5 m, un carril; radio de eje inicial 20 m; gradiente nominal 10%. Comprobar ancho y altura **libres** después de sostenimiento, drenaje, manga y servicios. Las cifras Ri/Re del fabricante son envolventes a giro máximo; no radios de eje de una carretera. R20 no demuestra por sí solo la trayectoria barrida.
- Galería: 3.5 × 3.5 m con paredes hasta 3 m y bóveda elíptica de alza 0.5 m, hipótesis para circulación recta y desarrollo con DD210 B14SNV+CFX-XS opcional. Ensanchar intersecciones: los anchos T de maniobra del LH307/TH315 superan 3.5 m. Comprobar giro, retroceso y orientación del jumbo.
- Cruce: ensanche inicial 6.5 m con 18 m de longitud **útil a ancho completo**; añadir transiciones fuera de esos 18 m o validar su longitud efectiva. Dos camiones de 2.274 m ocupan 4.548 m; el espacio restante es presupuesto geométrico, no margen legal de seguridad ni aprobación del cruce.
- Estación de carga: altura inicial 5.2–5.5 m para la opción estándar LH307; ampliar localmente en ancho y comprobar el cucharón contra toda la bóveda. La altura del eje no garantiza altura suficiente fuera del eje. La principal de 4.5 m se propone para traslado, no para elevar completamente el cucharón. Descarga del camión y carguío son maniobras distintas; trayectoria pendiente.
- Proyectar transiciones de gradiente y curvatura; verificar gálibo inferior y superior con batalla/voladizos y trayectoria real. No asignar un radio vertical universal sin geometría y equipo exactos.
- En veta de 1–3 m, separar la envolvente mineralizada de la excavación para equipos. Medir dilución por intersección de sólidos y fracción mineralizada, y mantener las leyes/densidades sintéticas identificadas; no asignar ley global al estéril ni convertir esas leyes en recursos.

LH202/LH203 pueden servir para una variante de menor ancho, pero no se declaró compatibilidad directa con TH315: requiere revisar la trayectoria completa del cucharón y la caja. Comparar solo la altura de la punta en posición completamente volcada no prueba ni descarta compatibilidad. Se usa la pareja LH307/TH315 porque tiene respaldo explícito del fabricante.

## Perú: reglas aplicables y límites

Fuentes oficiales: [DS 034-2023-EM promulgado](https://busquedas.elperuano.pe/dispositivo/NL/2249422-2) y [compilación MINEM 2026](https://cdn.www.gob.pe/uploads/document/file/6437172/5631689-rsso-reglamento-2026.pdf?v=1774646092).

La [ficha MINEM de edición 2026](https://www.gob.pe/institucion/minem/informes-publicaciones/5631689-reglamento-de-seguridad-y-salud-ocupacional-en-mineria-ed-2024) declara actualización al 30/05/2024 con DS 023-2017 y DS 034-2023. La búsqueda oficial adicional del 09/10/2026 no identificó cambios posteriores de los artículos seleccionados; no constituye certificación jurídica exhaustiva.

| Artículo | Paráfrasis breve y efecto para el piloto |
|---|---|
| 33 y 214 g/h | Geomecánica local, dimensiones calculadas, uso y servicios determinan sección/gradiente. Los tamaños del piloto no acreditan cumplimiento. |
| 214 i/j | Refugios cada 50 m; galerías principales con cruces señalizados; accesos/cruces adicionales cada 150–200 m considerando vehículo mayor y drenaje. |
| 215 | Salida a superficie con pendiente >5%: evaluar necesidad de carreteras de alivio mediante identificación de peligros y riesgos. |
| 216 | En rampas: refugios y puntos de cruce ≤50 m en tangentes largas; ≤30 m en tangentes cortas y curvas. |
| 246/252 | Definir circuito y caudal por personas, diésel, altura, calor y gases. Un sólido de ventilación no representa un cálculo. |
| 277 b | Dos accesos a superficie con separación ≥30 m o comunicación permitida; excepciones delimitadas, no asumidas para el piloto. |

En la rampa curva manda la separación específica de artículo 216; no reemplazarla por 150–200 m del artículo 214 j. Refugio peatonal, área de cruce y estación de refugio de emergencia son elementos diferentes. No atribuir a Perú una sección, radio ni pendiente subterránea universal; el 12% citado en artículo 262 corresponde a cielo abierto.

Evaluaciones pendientes: macizo/soporte, portal y cobertura, estabilidad local, trayectoria barrida 3D, frenado/visibilidad, servicios/drenaje, ventilación diésel, accesos a superficie y perforación de la estación alta. Conservar estado `CONCEPTUAL_PENDIENTE_VALIDACION`.
