# Paquete completo de geometría y evidencia

El ZIP original se conserva byte por byte en tres partes para su subida mediante el conector. El DUF, el modelo de bloques, las mediciones y las imágenes se abren directamente; reconstruir este ZIP es opcional para consultar los DXF y la evidencia extensa.

Con Python 3, desde esta carpeta:

```text
python reconstruir_evidencia.py
```

Se verifican tamaño y SHA-256 de cada parte, SHA-256 del ZIP unido y CRC de sus entradas. El resultado aparece en la carpeta superior como `Geometria_y_evidencia.zip`, con exactamente los mismos bytes que el archivo local original. El programa conserva cualquier archivo diferente que ya exista y se detiene.
