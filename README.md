# Simulación y análisis de señales con la Transformada de Fourier

Proyecto académico que genera un pulso rectangular, una función escalón y una señal senoidal, y analiza sus espectros de magnitud y fase mediante la FFT de NumPy.

## Requisitos
- Python 3.10 o posterior
- NumPy
- Matplotlib

## Instalación
En la terminal de Visual Studio Code, dentro de esta carpeta, ejecuta:

```bash
python -m pip install -r requirements.txt
```

## Ejecución
```bash
python simulacion_fourier.py
```

El programa guarda las gráficas en la carpeta `graficas`.

## Qué analiza
1. Señales en el dominio del tiempo.
2. Espectro de magnitud y fase.
3. Linealidad de la FFT.
4. Desplazamiento temporal y su efecto sobre la fase.
5. Comparación de senoidales de 5 Hz y 10 Hz para observar el escalamiento de frecuencia.

## Importante
La FFT trabaja con muestras finitas. En señales no periódicas, como el escalón, el espectro observado depende de la duración de la ventana y del muestreo.

## Autor
[Escribe tu nombre]
