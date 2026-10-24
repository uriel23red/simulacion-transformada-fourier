"""
Actividad formativa 2: Simulación y análisis de señales con la Transformada de Fourier.
Autor: [Escribe tu nombre]
Requisitos: numpy, matplotlib
Ejecutar: python simulacion_fourier.py

Nota: La FFT analiza una cantidad finita de muestras. Para señales no periódicas,
como el escalón, el resultado depende de la duración de la ventana observada.
"""
import os
import numpy as np
import matplotlib.pyplot as plt

CARPETA_GRAFICAS = "graficas"
os.makedirs(CARPETA_GRAFICAS, exist_ok=True)

# 1. Parámetros de muestreo
fs = 1000                 # Frecuencia de muestreo: 1000 muestras por segundo
duracion = 2.0            # Duración total de la simulación en segundos
t = np.arange(-duracion / 2, duracion / 2, 1 / fs)
N = len(t)

# 2. Definición de señales en el dominio del tiempo
pulso = np.where((t >= -0.15) & (t <= 0.15), 1.0, 0.0)  # Pulso rectangular
escalon = np.where(t >= 0, 1.0, 0.0)                    # Función escalón unitario
f0 = 5                                                     # Frecuencia de la sinusoide: 5 Hz
seno = np.sin(2 * np.pi * f0 * t)                        # Señal senoidal

def espectro(x):
    """Devuelve frecuencias, magnitud unilateral y fase de la FFT."""
    X = np.fft.rfft(x)
    frecuencias = np.fft.rfftfreq(len(x), d=1 / fs)
    magnitud = np.abs(X) / len(x)
    # Ajuste de amplitud unilateral: duplica componentes salvo DC y Nyquist.
    if len(magnitud) > 2:
        magnitud[1:-1] *= 2
    fase = np.angle(X)
    return frecuencias, magnitud, fase

def graficar_senal(nombre, x, limite_f=40):
    """Grafica la señal temporal y su espectro de magnitud y fase."""
    f, mag, fase = espectro(x)
    fig, ejes = plt.subplots(3, 1, figsize=(10, 8))
    fig.suptitle(f"Análisis de la señal: {nombre}", fontsize=14)
    ejes[0].plot(t, x)
    ejes[0].set_title("Dominio del tiempo")
    ejes[0].set_xlabel("Tiempo (s)")
    ejes[0].set_ylabel("Amplitud")
    ejes[0].grid(True)
    ejes[1].plot(f, mag)
    ejes[1].set_xlim(0, limite_f)
    ejes[1].set_title("Espectro de magnitud")
    ejes[1].set_xlabel("Frecuencia (Hz)")
    ejes[1].set_ylabel("Magnitud")
    ejes[1].grid(True)
    ejes[2].plot(f, fase)
    ejes[2].set_xlim(0, limite_f)
    ejes[2].set_title("Espectro de fase")
    ejes[2].set_xlabel("Frecuencia (Hz)")
    ejes[2].set_ylabel("Fase (rad)")
    ejes[2].grid(True)
    fig.tight_layout()
    ruta = os.path.join(CARPETA_GRAFICAS, f"{nombre.lower().replace(' ', '_')}.png")
    fig.savefig(ruta, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"Gráfica guardada: {ruta}")

# 3. Visualización de cada señal
graficar_senal("Pulso rectangular", pulso, limite_f=40)
graficar_senal("Funcion escalon", escalon, limite_f=40)
graficar_senal("Senal senoidal", seno, limite_f=20)

# 4. Propiedad de linealidad: FFT(a*x + b*y) = a*FFT(x) + b*FFT(y)
a, b = 2.0, -0.5
x1 = seno
x2 = pulso
fft_combinada = np.fft.fft(a * x1 + b * x2)
fft_por_partes = a * np.fft.fft(x1) + b * np.fft.fft(x2)
error_linealidad = np.max(np.abs(fft_combinada - fft_por_partes))
print(f"Error máximo de linealidad: {error_linealidad:.3e}")

# 5. Propiedad de desplazamiento temporal:
# Desplazar una señal circularmente cambia la fase de su FFT, no su magnitud.
desplazamiento_muestras = int(0.05 * fs)  # 50 ms
seno_desplazado = np.roll(seno, desplazamiento_muestras)
X_original = np.fft.fft(seno)
X_desplazado = np.fft.fft(seno_desplazado)
error_magnitud = np.max(np.abs(np.abs(X_original) - np.abs(X_desplazado)))
print(f"Error máximo de magnitud al desplazar: {error_magnitud:.3e}")

# 6. Escalamiento temporal: comprimir en el tiempo eleva la frecuencia.
# Se comparan dos sinusoides de 5 Hz y 10 Hz.
seno_5hz = np.sin(2 * np.pi * 5 * t)
seno_10hz = np.sin(2 * np.pi * 10 * t)
f5, m5, _ = espectro(seno_5hz)
f10, m10, _ = espectro(seno_10hz)
fig, ax = plt.subplots(figsize=(10, 4.5))
ax.plot(f5, m5, label="Seno de 5 Hz")
ax.plot(f10, m10, label="Seno de 10 Hz", alpha=0.8)
ax.set_xlim(0, 20)
ax.set_title("Comparación del espectro: 5 Hz y 10 Hz")
ax.set_xlabel("Frecuencia (Hz)")
ax.set_ylabel("Magnitud")
ax.grid(True)
ax.legend()
fig.tight_layout()
fig.savefig(os.path.join(CARPETA_GRAFICAS, "comparacion_frecuencias.png"), dpi=160)
plt.close(fig)

print("\nSimulación terminada. Revisa las gráficas dentro de la carpeta 'graficas'.")
