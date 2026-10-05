# proyecto-deswik

Proyecto independiente de miner�a subterr�nea desarrollado en **Deswik CAD 2026.1**. Esta versi�n re�ne la topograf�a original y una veta conceptual con su geometr�a, atributos, exportaciones y evidencia de verificaci�n. Se prepar� el 5 de octubre de 2026 como copia independiente del proyecto de escritorio para continuar su desarrollo mediante GitHub.

## Avance actual

- **Topograf�a dentro del DUF principal:** superficie triangulada, objetos de puntos, curvas de nivel, anotaciones y secciones originales. Estos datos est�n en el mismo archivo que la veta; no se dispone de una exportaci�n DXF independiente de la topograf�a en este repositorio.
- **Veta VETA_001:** buzamiento de 75�, direcci�n de buzamiento ESE (azimut 108.815301�), extensi�n vertical conceptual de 1000 m por debajo de la traza que pasa por la superficie y potencia verdadera variable de 1 a 3 m.
- **S�lido y superficie central:** capas separadas, geometr�a auxiliar DXF y comprobaciones de cierre, orientaci�n y volumen del s�lido. Volumen geom�trico: 2537039.801976 m�.
- **Datos:** ficha CSV con 16 campos, diccionario y atributos incorporados al s�lido. Au 4.2 g/t, Ag 65 g/t y densidad 2.7 t/m� son ejemplos sint�ticos, sin muestreo ni ensayes; el tonelaje calculado tambi�n es un ejemplo. La potencia variable es una hip�tesis geom�trica.
- **Organizaci�n:** 22 capas nativas, grupos de topograf�a, geolog�a, referencias y gu�as, respaldos y documentaci�n de procedencia.

**Todav�a no se ha dise�ado una rampa ni elegido un m�todo de explotaci�n.** No hay modelo de bloques, interpolaci�n de leyes ni clasificaci�n de recursos o reservas. Esta es una base conceptual de trabajo; no constituye un dise�o listo para ejecuci�n ni una estimaci�n mineral validada.

## Vista de referencia

![Vista de referencia de la topograf�a gris y la veta roja](03_documentacion/vista-topografia-veta.png)

Captura aportada durante el trabajo local. Sirve para identificar el modelo; no reemplaza la revisi�n de la geometr�a en Deswik.

## Archivos

| Ruta | Contenido |
|---|---|
| [proyecto-deswik.duf](proyecto-deswik.duf) | Proyecto principal: topograf�a, veta y atributos nativos |
| [01_datos](01_datos/) | Ficha de ejemplo y diccionario de atributos |
| [02_geometria](02_geometria/) | DXF del s�lido con superficie central y DXF de gu�as |
| [03_documentacion](03_documentacion/) | Ficha, procedencia, verificaciones, inventarios y vista de referencia |
| [04_respaldo](04_respaldo/) | Versi�n anterior a la organizaci�n de capas |

El repositorio conserva los datos y documentos del proyecto. No incluye entornos Python, configuraci�n personal de Codex, credenciales, add-ins comunitarios ni archivos temporales de bloqueo o respaldos autom�ticos de Deswik. Las herramientas y habilidades preparadas en el PC est�n descritas en [Herramientas_y_habilidades.md](03_documentacion/Herramientas_y_habilidades.md); ese documento registra la instalaci�n local, no instala componentes en otra m�quina.

## Abrir y continuar

1. Descargar o clonar el repositorio completo.
2. Abrir **proyecto-deswik.duf** en Deswik CAD. La referencia de versi�n usada es 2026.1; no se ha probado compatibilidad con otras versiones.
3. Consultar [Veta_ficha.md](03_documentacion/Veta_ficha.md) y [Diccionario_atributos.csv](01_datos/Diccionario_atributos.csv) antes de modificar o importar datos.
4. Trabajar sobre el DUF principal y guardar los cambios. El archivo de `04_respaldo` conserva una etapa anterior.

Las capas principales son `01_TOPOGRAFIA`, `02_GEOLOGIA_VETA_001`, `03_REFERENCIAS`, `04_SUPERFICIES_AUX` y `90_GUIAS_VETA`. El s�lido est� en `02_GEOLOGIA_VETA_001\01_SOLIDO_POT_1_3M`; la superficie central est� en `02_GEOLOGIA_VETA_001\02_SUPERFICIE_CENTRAL`. Las curvas y objetos de puntos pueden estar ocultos: consultar [Inventario_capas.csv](03_documentacion/Inventario_capas.csv).

Identificador del s�lido: `VETA_ID=VETA_001`, GUID `1387534c-b5c9-4846-b6c5-8d2e859c9c84`, handle guardado `2676` decimal / `A74` hexadecimal. Un handle puede cambiar al editar; comprobar la identidad antes de volver a importar la ficha por HANDLE.

Los CSV usan coma y punto decimal. Los 16 atributos de Deswik se guardaron como texto: convertir expl�citamente los campos num�ricos antes de calcular y conservar los datos ausentes como ausentes. Los metros proceden del diccionario y la procedencia; el DXF R12 auxiliar no declara INSUNITS. No se ha identificado en la documentaci�n un sistema de referencia geod�sico para reinterpretar las coordenadas.

## Evidencia y trazabilidad

- [Verificacion_proyecto_deswik.json](03_documentacion/Verificacion_proyecto_deswik.json): lectura nativa del proyecto guardado, capas, s�lido y atributos.
- [Procedencia_del_modelo.md](03_documentacion/Procedencia_del_modelo.md): construcci�n, copias y cambios de identificadores.
- [Inventario_archivos_sha256.csv](03_documentacion/Inventario_archivos_sha256.csv): tama�os y hashes de los archivos de esta copia, sin incluir el propio inventario ni `.git`.
- [Verificacion_copia_publicacion.json](03_documentacion/Verificacion_copia_publicacion.json): comprobaci�n de integridad al preparar la copia independiente.
- [README_paquete_escritorio_original.md](03_documentacion/README_paquete_escritorio_original.md): instrucciones originales del paquete local, preservadas como documento hist�rico.

Los manifiestos y verificaciones anteriores conservan sus rutas locales y nombres de capa de la etapa en que se generaron. No son rutas que deban existir en el equipo de quien descargue el repositorio. Los archivos con sufijo `_original` son evidencia hist�rica; el DUF de la ra�z y la ficha CSV de `01_datos` corresponden al estado organizado.

## Pr�ximos pasos

Incorporar informaci�n trazable de geolog�a, muestreo, geotecnia y topograf�a; revisar continuidad y potencia de la veta; y comparar m�todos de explotaci�n cuando existan los datos necesarios. El dise�o de accesos, rampas, niveles y tajos se definir� despu�s con par�metros de proyecto acordados y verificaciones espec�ficas.
