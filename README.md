# Traductor de Lengua de Señas Mexicana (LSM) con IA y Arduino

El sistema captura video en tiempo real a través de una cámara web y procesa cada fotograma utilizando un modelo de Red Neuronal Convolucional (CNN) entrenado con Teachable Machine.
Una vez que el modelo identifica una seña (por ejemplo, una letra del abecedario o una palabra como "Hola"), el sistema realiza dos acciones simultáneas:
Retroalimentación Auditiva: La computadora verbaliza la letra o palabra detectada utilizando síntesis de voz (TTS).
Visualización Externa: Envía el texto vía comunicación Serial a un microcontrolador Arduino, el cual lo muestra en una pantalla LCD para que el receptor pueda leer el mensaje.

## Tecnologías Utilizadas
### Software
- Python 3.10: Lenguaje principal del proyecto (versión requerida para compatibilidad con TensorFlow).

- TensorFlow / Keras (v2.15): Framework de Deep Learning para ejecutar el modelo de clasificación de imágenes (.h5).

- OpenCV (cv2): Procesamiento de imágenes y captura de video.

- PySerial: Comunicación asíncrona entre la PC y el Arduino.

- pyttsx3: Motor de texto a voz (Text-to-Speech) offline.

- Teachable Machine: Plataforma de Google utilizada para el entrenamiento y exportación del modelo.

### Hardware
- Arduino Uno (o compatible).

- Pantalla LCD 16x2 con módulo I2C (para reducir el cableado a 4 hilos).

- Cámara Web (integrada o USB).

- PC/Laptop (procesamiento de IA).

## Arquitectura del Sistema
El flujo de datos del sistema se comporta de la siguiente manera:

1. Entrada: La cámara captura el gesto del usuario.

2. Procesamiento: Python redimensiona la imagen y la normaliza para el modelo.

3. Inferencia: El modelo retorna una probabilidad. Si la confianza supera el umbral (e.g., 0.90), se acepta la predicción.

4. Salida Híbrida:

    Se genera el audio localmente.

    Se envía la cadena de texto (String) por el puerto COM/TTY al Arduino.
   
## Instalación y Uso
Prerrequisitos

Este proyecto requiere Python 3.10 debido a las dependencias de TensorFlow. Si usas Linux (Arch/Ubuntu), se recomienda usar pyenv.

Librerías de Python:
Bash

pip install tensorflow==2.15.0 opencv-python pyserial pyttsx3

Para usuarios de Linux (Arch/Manjaro): Es necesario instalar el motor de voz del sistema:
Bash

sudo pacman -S espeak-ng

Configuración del Hardware (Arduino)

    Conecta la pantalla LCD al Arduino:

        SDA -> A4 (o pin SDA)

        SCL -> A5 (o pin SCL)

        VCC -> 5V

        GND -> GND

    Carga el código sketch.ino (incluido en la carpeta arduino/) usando el Arduino IDE.

Ejecución

    Conecta el Arduino por USB.

    Ejecuta el script principal:
    Bash

    python main.py

Nota: Este proyecto fue desarrollado como una iniciativa educativa para explorar la intersección entre la IA y los sistemas embebidos aplicados a la inclusión social.
