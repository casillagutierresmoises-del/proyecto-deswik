# Proyecto Deswik mecanizado: ampliación vigente

Abrir **[proyecto-deswik-mecanizado.duf](proyecto-deswik-mecanizado.duf)** en Deswik CAD 2026.1, manteniendo esta carpeta y `01_datos` juntas. Es el mismo proyecto mejorado; la base y el piloto anterior son antecedentes.

La ampliación comprende seis niveles entre cotas 2210 y 2110 m WCS, seis tajeos (cinco de corte y relleno ascendente y uno de taladros largos), rampa y accesos mecanizados, galerías, servicios y cuatro chimeneas hasta superficie. Se preservan la topografía, la veta y los 14.000 bloques originales. La rampa tiene sección nominal 4,5 × 4,5 m, radio de eje 30 m, longitud 947,83 m y pendiente máxima 11,08%.

- [Resumen, supuestos, dimensiones y pendientes](03_documentacion/Ampliacion/Resumen_ampliacion.md).
- [Estado del proyecto](03_documentacion/LEEME_estado_actual.md).
- [Mediciones editables](01_datos/Ampliacion/Mediciones_mecanizado.xlsx).
- [Captura real de Deswik](04_imagenes/README.md).
- [Vista isométrica](02_geometria/Ampliacion/Isometrica_ampliacion.png).
- [Proyección longitudinal](02_geometria/Ampliacion/Seccion_longitudinal.png).
- [Comprobación del último guardado publicado](03_documentacion/Publicacion/Verificacion_ultimo_guardado.json).
- [Paquete completo de geometría y evidencia](02_geometria/Ampliacion/Paquete_evidencia/README.md).

Los informes de `03_documentacion/Ampliacion` corresponden al archivo ampliado y verificado previamente. El usuario volvió a guardar antes de publicar; su hash y las diferencias de presentación o serialización están documentados en `03_documentacion/Publicacion`. Los informes anteriores fuera de esas carpetas y el README del piloto de 50 × 30 m se conservan como históricos.

Los bloques cubren sólo el piloto original de 50 × 30 m. Veta, potencia, leyes y densidad son sintéticas; no se declaran recursos ni reservas. La densidad de referencia 2,7 t/m³ y los factores de relleno se pueden editar en Excel.

**Diseño conceptual, no apto para ejecución sin validar geotecnia, sostenimiento, ventilación, vías de escape y maniobras de equipos.** La longitudinal entregada es una proyección; falta una sección nativa de CAD. El EPSG/datum no está documentado.
