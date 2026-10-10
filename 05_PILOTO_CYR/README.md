# Piloto de bloques y corte y relleno

Actualizado el 9 de octubre de 2026. **Estado: el DUF contiene las labores nativas y la referencia relativa al modelo Datamine. La lectura nativa y una revisión independiente verificaron la copia; falta abrirla y comprobar su visualización en Deswik.** Se conservaron las 1407 entidades originales, incluida la topografía, sus puntos y la veta con sus 16 atributos. La copia incorpora 11 capas y 103 figuras: 38 sólidos, 39 polilíneas y 26 rótulos, con 10 atributos por figura.

El centro de la marca CAD es X 5085, Y 10675. Se proyecta sobre la traza de VETA_001 para ubicar un panel de 50 m de rumbo y 30 m de altura vertical. Cotas del panel: 2097.960878–2127.960878 m. Las coordenadas son WCS del proyecto; su CRS/EPSG no está documentado.

- `01_datos`: `Bloques_piloto.dm`, modelo Datamine nativo de 14 000 celdas de 0.5 × 2 × 1.5 m; CSV fuente con centroides WCS, leyes Au/Ag sintéticas, densidad supuesta, fracción mineral y tonelaje ilustrativo; diccionario y datos de labores.
- `02_geometria`: DXF con 38 sólidos cerrados: diez cortes de 3 m, rampa, cuatro niveles de acceso, conexiones, chimeneas locales y reservas geométricas para refugios. Las labores están integradas también en el DUF. El DXF es un archivo auxiliar; el modelo de bloques nativo es el .dm.
- `03_documentacion`: prototipo, manifiesto, comprobación de datos/mallas, selección CAD de origen, cobertura topográfica por muestras y referencias peruanas.

Se preparó `01_datos/Importar_bloques_piloto.dcsvml` con el serializador nativo de Deswik 2026.1. Su lectura nativa confirmó los 17 mapeos y todos los parámetros. Puede cargarse con **Load settings** en el asistente de conversión CSV a Datamine. Es un perfil para las rutas locales de esta PC; trasladar el paquete requiere ajustar los archivos de entrada/salida.

El archivo `.dm` se escribió con el controlador de archivos de Deswik instalado, sin activar la aplicación ni modificar ventanas. Una relectura en un proceso independiente confirmó todos los registros, atributos y parámetros del modelo; error máximo de coordenadas WCS respecto al CSV: 3.64 × 10⁻¹² m. Los informes son `Verificacion_native_dm.json` y `Verificacion_native_dm_relectura.json`.

La rampa usa radio al eje de 8 m, pendiente nominal 12% y sección 3 × 3 m como supuestos de esta demostración. Se representan diez fases de extracción y posterior relleno, no diez vacíos abiertos simultáneamente. Los accesos a cortes intermedios requieren reconfiguración con el relleno. Las chimeneas son conexiones locales; todavía no se modelan dos salidas a superficie.

Las mallas pasaron cierre y orientación; el modelo tabular reconcilia su fracción mineral con los cortes. La comprobación nativa de topografía consultó 300 secciones: no faltó terreno en las muestras y la cobertura vertical mínima muestreada fue 9.137911 m. No garantiza cobertura entre muestras ni estabilidad geomecánica.

Los tamaños de labores son hipótesis conceptuales pendientes de geomecánica, equipos, relleno y ventilación. Las referencias oficiales están en `03_documentacion/peru_referencias.md`. No hay ensayes, recursos, reservas ni diseño operativo aprobado.

Para continuar en Deswik, abrir `proyecto-deswik-piloto-cyr.duf` de esta carpeta y revisar **Geomodel Display**. La referencia guardada es `01_datos\Bloques_piloto.dm`, con una sección horizontal en Z=2112.960878 m. La referencia se verificó en un segundo proceso; la carga y el dibujo en la aplicación siguen pendientes. La topografía y la veta conservan su visibilidad original, por lo que pueden ocultar las labores subterráneas hasta ajustar la vista.

La chimenea de escape incluye ocho marcas de descanso, con separación de 4.436898 m medida a lo largo de su eje. La configuración del modelo cambia únicamente atributos de la capa interna de ajustes y conserva los existentes. Los informes de integración, comparación independiente, referencia Datamine y hashes del paquete están en `03_documentacion`.
