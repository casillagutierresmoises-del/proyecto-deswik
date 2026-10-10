# Proyecto Deswik mecanizado: ampliación conceptual

Fecha: 09/10/2026, Lima. **Estado: archivo principal actualizado, abierto en Deswik CAD y sin cambios pendientes de guardar; relectura independiente y comprobación de carga aprobadas.** Se conserva el mismo nombre, carpeta y distribución de ventanas. El archivo único vigente es `proyecto-deswik-mecanizado.duf` en `06_PILOTO_MECANIZADO`, dentro del mismo proyecto.

Se conservan la topografía original, la veta `02_GEOLOGIA_VETA_001` y los 14.000 bloques del piloto, con los mismos datos. La ampliación ocupa unos 340 m de rumbo y 100 m entre sus niveles extremos. Los bloques siguen cubriendo sólo el piloto original de 50 × 30 m: no representan el nuevo sector completo. Veta, potencia variable, leyes y densidad son sintéticas; no son recursos ni reservas. Coordenadas en metros WCS, sin EPSG ni datum documentados.

## Acceso y niveles

| Nivel | Cota de piso, m WCS | Intervalo local de rumbo, m |
|---|---:|---:|
| N01 | 2210 | 350–490 |
| N02 | 2190 | 150–490 |
| N03 | 2170 | 150–490 |
| N04 | 2150 | 150–490 |
| N05 | 2130 | 150–490 |
| N06 | 2110 | 150–490 |

La rampa tiene cinco vueltas de radio de eje 30 m, sección nominal de excavación 4,5 × 4,5 m con arco, descansos y ensanches hasta 6,5 m cada 25 m. Las estaciones principales están aproximadamente cada 188,50 m de eje en planta. Longitud 3D: **947.83 m**; volumen bruto de sus cinco sólidos: **21,059.47 m³**, antes de deduplicar encuentros con accesos. Pendiente nominal ideal por vuelta: 10,61%; máxima real de los tramos inclinados: **11.0826%**; los descansos son horizontales. Los accesos de nivel son 4,5 × 4,5 m con curvas de radio de eje 20 m. Galerías y cruceros de producción: 3,5 × 3,5 m con arco.

Bocamina BOC-V2: piso WCS (5059,7007; 11095,6370; 2217,0000). Socavón cubierto de 70 m horizontales, seguido hacia el exterior por una trinchera de 44,418 m y envolvente de movimiento de tierras de 8 m. La mínima cobertura vertical de techo calculada sobre el TIN original es **4.190 m** en el acceso cubierto. No acredita roca competente. El TIN original no se recorta ni se altera; el corte (1,289.25 m³) y relleno (70.39 m³) de trinchera se modelan como derivados independientes.

La cobertura vertical mínima de las labores ordinarias, fuera de bocamina y salidas de chimeneas, es **21.936 m**, superior al criterio de corona de 20 m. Se incluyen cámaras de carga 6,5 × 5,0 × 18 m, reservas de refugio 5,0 × 3,5 × 10 m, sumideros 4,0 × 3,5 × 6 m, estocadas, ventanas de carga y enlaces de servicio. Los refugios y sumideros son envolventes de excavación: capacidad, equipos y drenaje quedan pendientes.

## Tajeos, cortes y relleno

TJ-A1 a TJ-A4: corte y relleno ascendente, entre 2170 y 2210 m; 12 cortes por tajeo con avance mineral de 3,3333 m y pilares de 10 m entre los cuatro tajeos. TJ-C1: segundo sector CyR independiente, entre 2130 y 2170 m, también con 12 cortes. La excavación mecanizada tiene ancho mínimo 3,5 m, distinto de la potencia variable mineral. Su arco alcanza 3,8333 m de altura, mientras el avance entre cortes es 3,3333 m; la superposición de bóveda corresponde a etapas consecutivas.

TJ-B1: taladros largos hacia el lado de rumbo negativo/izquierdo, entre 2130 y 2190 m; subniveles cada 20 m, galerías de perforación/extracción, puntos de extracción, ventanas y líneas de anillos. El DD210 es un jumbo de desarrollo; falta seleccionar la perforadora de producción. No se fuerza una Zona D de cámaras y pilares porque la veta fuente mantiene 75° y no muestra un dominio de bajo buzamiento.

Los sólidos de mineral siguen los contactos de la veta original. Mineral, excavación y relleno tienen identidades y categorías distintas. Los ramp-in y distribuidores A/C de C01 a C12 son 24 configuraciones temporales alternativas, reconformadas tras el relleno; sólo la primera fase queda visible por defecto. No se suman como 12 accesos simultáneos. Las fases y conexiones próximas requieren revisión de la secuencia de explotación.

| Tajeo | Mineral, m³ | Toneladas con densidad supuesta 2,7 t/m³ | Relleno geométrico, m³ |
|---|---:|---:|---:|
| TJ-A1 | 1,598.0 | 4,314.5 | 3,570.0 |
| TJ-A2 | 1,788.2 | 4,828.2 | 3,570.0 |
| TJ-A3 | 2,004.1 | 5,411.2 | 3,570.0 |
| TJ-A4 | 2,237.9 | 6,042.3 | 3,570.0 |
| TJ-B1 | 3,255.4 | 8,789.5 | 3,228.6 |
| TJ-C1 | 1,772.6 | 4,786.0 | 4,760.0 |
| Total | 12,656.2 | 34,171.6 | 22,268.6 |

El Excel permite editar densidad y factor de relleno por tajeo. Las cantidades por labor son volúmenes brutos de cada sólido cerrado; no se publica un total neto de excavación sin unión geométrica de encuentros. La sección nominal máxima y el área equivalente volumen/longitud se distinguen en las tablas. El relleno comprende 60 cortes CyR y una etapa final B; mezcla, cemento, resistencia, densidad y consolidación no están medidos.

## Chimeneas y circuito conceptual

| Chimenea | Sección, m | Cota inferior, m | Cota superior, m | Longitud, m |
|---|---|---:|---:|---:|
| CH-VENT | 3 × 3 | 2110.00 | 2257.26 | 147.26 |
| CH-ESC | 3 × 3 | 2110.00 | 2240.45 | 130.45 |
| CH-ORE | 2.4 × 2.4 | 2110.00 | 2247.89 | 137.89 |
| CH-RLL | 2.4 × 2.4 | 2110.00 | 2240.99 | 130.99 |

Las cuatro chimeneas conectan geométricamente los seis niveles hasta un collar visible sobre el TIN en su propio XY. CH-VENT retorna aire, CH-ESC corresponde al escape, CH-ORE al pase de mineral y CH-RLL al relleno; capas y atributos separados. Los enlaces de servicio de 2,4 × 2,4 m no son accesos de camiones. Aire fresco: bocamina → rampa → accesos/galerías → frentes; retorno: enlaces independientes → CH-VENT → superficie. Caudales, ventiladores, puertas, reguladores y conductos auxiliares no están calculados. CH-ESC necesita compartimentos, escaleras y descansos; el sólido vertical no es una escalera de tránsito terminada.

## Capas, evidencia y vistas

La rama `03_PILOTO_MECANIZADO\AMPLIACION_V2` contiene métodos, niveles y funciones con colores distintos. `21_ROTULOS` contiene nombres, cotas y dimensiones. Los 24 grupos del piloto de 50 × 30 m se conservan bajo `HISTORICO_50x30`, ocultos; no se borran sus 162 figuras. Las etapas futuras, rellenos y ejes auxiliares se conservan ocultos para evitar una vista congestionada. La topografía, veta y referencia original del modelo Datamine se preservan.

- 407 sólidos nuevos cerrados, orientados y de volumen positivo; 383 polilíneas y 40 textos: 830 figuras nuevas.
- 274 comprobaciones continuas de cobertura sobre triángulos del TIN y 274 revisiones de ejes; 66 envolventes minerales y una comprobación adicional conservadora de pertenencia del relleno B1 a la veta; tres pilares A aprobados.
- La revisión de interferencias y separación comprobó 1.297.801 pares candidatos de celdas. Las labores independientes mantienen el criterio de 15 m; componentes conectados y fases excluyentes se identifican expresamente. Las intersecciones permitidas comprenden nodos de conexión y configuraciones temporales expresamente excluyentes tras relleno, sin excepción de solape entre ramp-in A y rampa principal.
- La relectura nativa independiente compara geometría, identidades, atributos, recursos y datos de bloques. El archivo preparado tiene 163 capas y 2.540 entidades nativas. SHA-256: `2f25c0a47ba4c4b931fbf9f5ab7eb556b8b662e7c35c3647353865a323b9b6b7`. La carga se comprobó en la sesión licenciada de CAD: documento sin cambios pendientes, todas las capas nativas presentes y 830 figuras nuevas cargadas. Las muestras de rampa, TJ-A1 y CH-VENT coinciden en geometría y volumen; también coinciden sus atributos reales. Se comprobaron las fases futuras y el relleno ocultos. CAD añade dos capas temporales de recorte, por lo que la sesión muestra 165 capas. La comprobación acotada se registra en `CAD_carga_final_verificacion.json`; no acredita todas las funciones de edición de CAD ni una aprobación de ingeniería.

Las vistas PNG/SVG se generaron con las mismas coordenadas y mallas: isométrica y proyección longitudinal. La longitudinal es una proyección sobre rumbo, no una intersección por plano; la banda de corona es ilustrativa y no sustituye la comprobación 3D. Las vistas no son capturas ni layouts nativos guardados en Deswik. Las tablas y las vistas se encuentran en `01_datos/Ampliacion` y `02_geometria/Ampliacion`; los informes aprobados y criterios están en esta carpeta. La evidencia comprimida explica la reutilización exacta de comprobaciones geométricas de la revisión 02 y el recálculo completo de sus colisiones en la revisión 03.

## Pendientes de ingeniería

**Diseño conceptual, no apto para ejecución sin validación.** Validar geotecnia y agua; roca competente, sostenimiento y taludes de bocamina; estabilidad de corona/pilares/tajeos; resistencia y secuencia del relleno; ventilación y servicios; vías de escape y capacidad de refugios; maniobras, frenado y gálibos dinámicos de scoop, camión y jumbo; equipo de taladros largos; selectividad, dilución, recuperación y costos con datos reales. Los mínimos de corona/separación/pilares son criterios del encargo, no mínimos normativos universales. Las fuentes oficiales peruanas y fichas de equipos se documentan en `Criterios_y_fuentes.md`; falta evaluar su aplicación a la operación efectiva.

Se conservaron la geometría, los atributos y los cambios del último guardado del usuario de SHA a8349eab…; la organización del piloto se trasladó al histórico al incorporar la ampliación: geometría original idéntica, color de topografía blanco con alfa 128 y propiedades de presentación actualizadas. La comparación y trazabilidad están en `Compatibilidad_base_guardada.json` e `Integracion_principal.json`.
