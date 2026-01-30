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

### Prerrequisitos

Este proyecto requiere **Python 3.10** debido a las dependencias de TensorFlow.

#### Verificar versión de Python
```bash
# Windows (CMD o PowerShell)
python --version

# macOS/Linux
python3 --version
```

#### Instalar Python 3.10 en Windows

1. **Descarga Python 3.10**:
   - Ve a [python.org/downloads](https://www.python.org/downloads/)
   - Descarga **Python 3.10.x** (versión estable más reciente de la serie 3.10)

2. **Ejecuta el instalador**:
   - ✅ **IMPORTANTE**: Marca la casilla **"Add Python 3.10 to PATH"**
   - Selecciona **"Install Now"** o personaliza la instalación
   - Espera a que termine la instalación

3. **Verifica la instalación**:
   ```cmd
   python --version
   ```
   Debería mostrar: `Python 3.10.x`

#### Instalar Python 3.10 en Linux

**Ubuntu/Debian**:
```bash
sudo apt update
sudo apt install python3.10 python3.10-venv python3-pip
```

**Arch/Manjaro**:
```bash
sudo pacman -S python310
```

#### Instalar Python 3.10 en macOS
Descárgalo desde [python.org](https://www.python.org/downloads/) o usa Homebrew:
```bash
brew install python@3.10
```

---

## 🪟 Guía de Instalación para Windows

### Paso 1: Instalar Visual C++ Redistributable (Requerido para TensorFlow)

TensorFlow requiere las bibliotecas de Visual C++. Si no las tienes instaladas:

1. Descarga **Microsoft Visual C++ Redistributable** desde:
   - [Visual C++ 2015-2022 Redistributable (x64)](https://aka.ms/vs/17/release/vc_redist.x64.exe)
2. Ejecuta el instalador y sigue las instrucciones
3. Reinicia tu computadora si es necesario

### Paso 2: Clonar el Repositorio

Abre **CMD** o **PowerShell** y ejecuta:

```cmd
git clone https://github.com/BeyondJules08/Intelligent-System.git
cd Intelligent-System
```

Si no tienes Git instalado, descárgalo desde [git-scm.com](https://git-scm.com/download/win) o descarga el repositorio como ZIP desde GitHub.

### Paso 3: Crear el Entorno Virtual

En la carpeta del proyecto, ejecuta:

```cmd
python -m venv venv
```

Esto creará una carpeta `venv` con el entorno aislado.

### Paso 4: Activar el Entorno Virtual

**Opción A - CMD (Símbolo del sistema)**:
```cmd
venv\Scripts\activate.bat
```

**Opción B - PowerShell**:
```powershell
venv\Scripts\Activate.ps1
```

> ⚠️ **Si PowerShell muestra un error de ejecución de scripts**:
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```
> Luego vuelve a intentar activar el entorno.

Cuando esté activado correctamente, verás **(venv)** al inicio de tu línea de comandos:
```
(venv) C:\Users\TuUsuario\Intelligent-System>
```

### Paso 5: Actualizar pip e Instalar Dependencias

```cmd
python -m pip install --upgrade pip
pip install tensorflow==2.15.0 opencv-python pyserial pyttsx3
```

O si existe un archivo `requirements.txt`:
```cmd
pip install -r requirements.txt
```

### Paso 6: Instalar Drivers del Arduino (si es necesario)

1. Descarga e instala el **Arduino IDE** desde [arduino.cc](https://www.arduino.cc/en/software)
2. Conecta el Arduino por USB
3. Windows debería instalar automáticamente los drivers
4. Verifica en **Administrador de dispositivos** > **Puertos (COM y LPT)** que aparezca el Arduino (ej: `COM3`)

### Paso 7: Configurar el Hardware (Arduino)

1. **Conexión de la pantalla LCD I2C al Arduino**:
   ```
   LCD I2C  ->  Arduino
   -------------------------
   SDA      ->  A4 (o pin SDA)
   SCL      ->  A5 (o pin SCL)
   VCC      ->  5V
   GND      ->  GND
   ```

2. **Cargar el sketch al Arduino**:
   - Abre Arduino IDE
   - Ve a **Archivo** > **Abrir** > selecciona `arduino/sketch.ino`
   - Selecciona tu placa: **Herramientas** > **Placa** > **Arduino Uno**
   - Selecciona el puerto: **Herramientas** > **Puerto** > **COM3** (o el que corresponda)
   - Haz clic en **Subir** (botón con flecha →)

### Paso 8: Ejecutar el Proyecto

Con el entorno virtual activado y el Arduino conectado:

```cmd
python main.py
```

### Paso 9: Desactivar el Entorno Virtual

Cuando termines:
```cmd
deactivate
```

---

## 🐧 Guía de Instalación para Linux

### Paso 1: Instalar Dependencias del Sistema

**Ubuntu/Debian**:
```bash
sudo apt update
sudo apt install python3.10 python3.10-venv python3-pip espeak git
```

**Arch/Manjaro**:
```bash
sudo pacman -S python310 espeak-ng git
```

### Paso 2: Clonar el Repositorio

```bash
git clone https://github.com/BeyondJules08/Intelligent-System.git
cd Intelligent-System
```

### Paso 3: Crear y Activar el Entorno Virtual

```bash
python3.10 -m venv venv
source venv/bin/activate
```

### Paso 4: Instalar Dependencias de Python

```bash
pip install --upgrade pip
pip install tensorflow==2.15.0 opencv-python pyserial pyttsx3
```

### Paso 5: Configurar Permisos del Puerto Serial

```bash
sudo usermod -a -G dialout $USER
```

**Cierra sesión y vuelve a iniciar** para que los cambios tengan efecto.

### Paso 6: Configurar Arduino y Ejecutar

Sigue los pasos 7 y 8 de la guía de Windows (son iguales).

---

## 🍎 Guía de Instalación para macOS

### Paso 1: Instalar Homebrew (si no lo tienes)

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Paso 2: Instalar Python 3.10

```bash
brew install python@3.10
```

### Paso 3: Clonar el Repositorio

```bash
git clone https://github.com/BeyondJules08/Intelligent-System.git
cd Intelligent-System
```

### Paso 4: Crear y Activar el Entorno Virtual

```bash
python3.10 -m venv venv
source venv/bin/activate
```

### Paso 5: Instalar Dependencias

```bash
pip install --upgrade pip
pip install tensorflow==2.15.0 opencv-python pyserial pyttsx3
```

### Paso 6: Configurar Arduino y Ejecutar

Sigue los pasos de configuración del hardware y ejecución.

---

## Solución de Problemas

### ❌ Error: "No module named 'tensorflow'"
**Solución**:
- Asegúrate de que el entorno virtual esté activado (debe aparecer `(venv)` en tu terminal)
- Verifica la instalación:
  ```cmd
  pip list | findstr tensorflow
  ```

### ❌ Error: "DLL load failed" (Windows)
**Solución**:
- Instala Visual C++ Redistributable (ver Paso 1 de Windows)
- Reinicia tu computadora

### ❌ Error de Puerto Serial (Windows)
**Solución**:
1. Abre **Administrador de dispositivos**
2. Expande **Puertos (COM y LPT)**
3. Busca tu Arduino (ej: `Arduino Uno (COM3)`)
4. Anota el número de puerto (ej: `COM3`)
5. Asegúrate de usar ese puerto en tu código

### ❌ Error de Puerto Serial (Linux)
**Solución**:
```bash
ls /dev/tty*  # Busca algo como /dev/ttyUSB0 o /dev/ttyACM0
sudo chmod 666 /dev/ttyUSB0  # Reemplaza con tu puerto
```

O configura los permisos permanentemente:
```bash
sudo usermod -a -G dialout $USER
# Cierra sesión y vuelve a iniciar
```

### ❌ Error: "Cannot open camera"
**Solución**:
- Verifica que la cámara no esté siendo usada por otra aplicación
- En Windows, ve a **Configuración** > **Privacidad** > **Cámara** y asegúrate de que las apps de escritorio puedan acceder
- Prueba con otra cámara USB si tienes disponible

### ❌ PowerShell no permite ejecutar scripts
**Solución**:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

**Nota**: Este proyecto fue desarrollado como una iniciativa educativa para explorar la intersección entre la IA y los sistemas embebidos aplicados a la inclusión social.
