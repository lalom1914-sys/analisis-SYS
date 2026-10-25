import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# 1. CONFIGURACIÓN INICIAL
# ==========================================
Fs = 1000  # Frecuencia de muestreo (Hz)
T = 1.0    # Duración total de la señal (segundos)
t = np.linspace(0, T, int(Fs * T), endpoint=False)

# ==========================================
# 2. CREACIÓN DE SEÑALES ELEMENTALES
# ==========================================
# A. Pulso rectangular
ancho_pulso = 0.1
pulso_rect = np.where((t >= 0.4) & (t <= 0.4 + ancho_pulso), 1.0, 0.0)

# B. Función escalón unitario (comienza en t = 0.2s)
escalon = np.where(t >= 0.2, 1.0, 0.0)

# C. Función senoidal (frecuencia de 50 Hz)
f0 = 50
senoidal = np.sin(2 * np.pi * f0 * t)

# ==========================================
# 3. FUNCIÓN PARA CÁLCULO DE LA FFT
# ==========================================
def calcular_fft(signal, Fs):
    N = len(signal)
    yf = np.fft.fft(signal)
    xf = np.fft.fftfreq(N, 1 / Fs)
    idx_positivo = xf >= 0
    return xf[idx_positivo], np.abs(yf[idx_positivo]) * 2 / N

# ==========================================
# 4. VISUALIZACIÓN DE SEÑALES EN EL TIEMPO
# ==========================================
plt.figure(figsize=(12, 10))

plt.subplot(3, 2, 1)
plt.plot(t, pulso_rect, 'r')
plt.title('Pulso Rectangular (Tiempo)')
plt.grid(True)

plt.subplot(3, 2, 3)
plt.plot(t, escalon, 'g')
plt.title('Función Escalón (Tiempo)')
plt.grid(True)

plt.subplot(3, 2, 5)
plt.plot(t, senoidal, 'b')
plt.title('Función Senoidal 50 Hz (Tiempo)')
plt.grid(True)

# Cálculo y gráfica de espectros de frecuencia
f_rect, mag_rect = calcular_fft(pulso_rect, Fs)
f_esc, mag_esc = calcular_fft(escalon, Fs)
f_sen, mag_sen = calcular_fft(senoidal, Fs)

plt.subplot(3, 2, 2)
plt.plot(f_rect[:200], mag_rect[:200], 'r')
plt.title('Espectro - Pulso Rectangular')
plt.grid(True)

plt.subplot(3, 2, 4)
plt.plot(f_esc[:200], mag_esc[:200], 'g')
plt.title('Espectro - Escalón Unitario')
plt.grid(True)

plt.subplot(3, 2, 6)
plt.plot(f_sen[:150], mag_sen[:150], 'b')
plt.title('Espectro - Senoidal (Pico en 50 Hz)')
plt.grid(True)

plt.tight_layout()
plt.show()

# ==========================================
# 5. VERIFICACIÓN DE LA PROPIEDAD DE LINEALIDAD
# ==========================================
# Linealidad: La FFT de una suma ponderada es la suma ponderada de las FFTs.
sig1 = np.sin(2 * np.pi * 20 * t)   # Señal a 20 Hz
sig2 = np.sin(2 * np.pi * 100 * t)  # Señal a 100 Hz
senal_combinada = 2 * sig1 + 3 * sig2

f_comb, mag_comb = calcular_fft(senal_combinada, Fs)

plt.figure(figsize=(8, 4))
plt.plot(f_comb[:150], mag_comb[:150], 'k')
plt.title('Verificación de Linealidad (Se visualizan picos en 20 Hz y 100 Hz)')
plt.xlabel('Frecuencia (Hz)')
plt.ylabel('Magnitud')
plt.grid(True)
plt.show()