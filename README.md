# Actividad Formativa 2: Simulación y análisis de señales con la transformada de Fourier

Este repositorio contiene la implementación y el desarrollo de la actividad práctica enfocada en el análisis de señales en el dominio del tiempo y de la frecuencia utilizando **Python** y la **Transformada Rápida de Fourier (FFT)**.

## 🛠️ Tecnologías y Librerías Utilizadas
- **Python 3.x**
- **NumPy**: Para la manipulación de arreglos numéricos y operaciones matemáticas.
- **SciPy / NumPy FFT**: Para el cálculo eficiente de la Transformada Rápida de Fourier (`np.fft.fft`).
- **Matplotlib**: Para la visualización gráfica de las señales temporales y espectros de frecuencia.

## 📈 Contenido del Proyecto
El script principal (`fourier_actividad.py`) abarca los siguientes puntos solicitados en la actividad:
1. **Generación de Señales Elementales**:
   - Pulso rectangular (ventana de tiempo definida).
   - Función escalón unitario.
   - Función senoidal (con una frecuencia de prueba de 50 Hz).
2. **Transformada de Fourier**:
   - Implementación del algoritmo FFT para convertir las señales del dominio del tiempo al dominio de la frecuencia.
   - Extracción de la magnitud y normalización del espectro de frecuencias positivas.
3. **Verificación de Propiedades**:
   - Demostración de la propiedad de **linealidad** combinando dos señales sinusoidales (a 20 Hz y 100 Hz) y comprobando la aparición de sus respectivos picos en el espectro frecuencial.

## 🚀 Instrucciones de Ejecución
1. Clona este repositorio o descarga los archivos en tu equipo:
   ```bash

(https://github.com/lalom1914-sys/analisis-SYS)
