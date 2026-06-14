# Micro-Desktop-Roll

[![Python v3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![PyQt5](https://img.shields.io/badge/UI-PyQt5-green.svg)](https://pypi.org/project/PyQt5/)
[![Ecosistema](https://img.shields.io/badge/Environment-Xubuntu%20%2F%20XFCE-orange.svg)](https://xubuntu.org/)


Un script de automatización en Python compacto y de diseño minimalista desarrollado para realizar un desplazamiento cíclico automático entre los escritorios virtuales de tu sistema operativo.

> **Nota de testeo:** Desarrollado y probado con éxito sobre entornos **Xubuntu (XFCE / X11)**.

> **⚠️ Importante:** Es mandatorio ejecutar la aplicación con permisos de administrador para que funcione correctamente. Esto se debe a que el programa utiliza métodos que requieren interacción a bajo nivel con el sistema operativo. Puede utilizar la interfaz gráfica `runasadmin` incluida en este repositorio.

---

## 🚀 Características
*   **Diseño despejado:** Implementación minimalista evitando dependencias innecesarias de relleno.
*   **Concurrencia limpia:** Procesamiento del bucle de rodado en un hilo secundario independiente para evitar congelamientos de la interfaz.
*   **Salida segura:** Cierre controlado del script y desvinculación limpia de procesos mediante la tecla de escape.

## 🛠️ Requisitos del Sistema y Dependencias

Al interactuar directamente con periféricos de hardware simulados y capturar eventos del teclado a bajo nivel, el proyecto utiliza las siguientes librerías:

*   **`pyautogui`**: Utilizada para simular la combinación de teclas físicas encargadas de rotar la pantalla.
*   **`keyboard`**: Encargada de escuchar globalmente en segundo plano la pulsación de teclas para detener el proceso de forma segura.

### Instalación de dependencias:
Asegúrate de contar con `pip` e instala los módulos necesarios ejecutando en tu terminal:

```bash
pip install pyautogui keyboard
```

## 🔐 Nota Importante sobre Permisos (Linux Input Devices)
Debido a las estrictas restricciones de seguridad que posee Linux sobre la interceptación y simulación de eventos en dispositivos de entrada (*input devices*), **este script requiere obligatoriamente ejecutarse con privilegios de administrador (`sudo`)**. 

Esta elevación de permisos es de carácter lógico y mandatorio para permitir que las librerías interactúen de forma directa con el servidor gráfico (X11).

## 💻 Modo de Uso

1. Descarga o clona este repositorio en tu máquina local.
2. Abre una terminal dentro del directorio del proyecto.
3. Lanza el script principal invocando al intérprete de Python con permisos elevados:

```bash
sudo python3 mdsktproll.py
```

### 🛑 Cómo detener la ejecución
El script se mantendrá rodando los escritorios de manera cíclica basándose en la frecuencia de tiempo configurada en el archivo. Para finalizar el programa de forma limpia y segura en cualquier momento, simplemente presiona la tecla:

*   **`ESC` (Escape)**

Al detectarla, el hilo secundario se detendrá de inmediato y se limpiarán todos los hooks activos del teclado.

---

## ⚙️ Funcionamiento Detallado

### 1. Importaciones
El programa importa las bibliotecas necesarias para su correcto funcionamiento:
*   **`threading`**: Para crear y administrar hilos de ejecución.
*   **`time`**: Para controlar el tiempo y la frecuencia de la acción.
*   **`pyautogui`**: Para simular la interacción con el teclado y el mouse.
*   **`keyboard`**: Para detectar la presión de teclas.

### 2. Variables de Configuración
*   **`frecuencia`**: Define el tiempo en segundos entre cada acción de rodar la pantalla.
*   **`tecla_escape`**: Define la tecla que se debe presionar para detener el programa.
*   **`combo_rodar`**: Define la combinación de teclas que se utiliza para rodar la pantalla.

### 3. Tiempo de Espera Inicial
Se establece una espera obligatoria de **2 segundos** antes de iniciar el bucle principal del programa.

### 4. Función `rodar()`
Esta función se ejecuta dentro de un **hilo independiente**:
*   Simula la combinación de teclas `combo_rodar` para rodar la pantalla.
*   Utiliza un bucle `while` para repetir la acción a la frecuencia establecida en `frecuencia`.
*   Comprueba constantemente la variable `detener_hilo` para determinar si debe detenerse.

### 5. Creación e Inicio del Hilo
*   Se crea un objeto `threading.Thread` con la función `rodar()` como objetivo.
*   Se inicia el hilo mediante la invocación del método `start()`.

### 6. Bucle Principal
Este bucle se ejecuta en el **hilo principal** del sistema:
*   Comprueba de forma continua si la tecla `tecla_escape` es presionada.
*   Si la tecla no es presionada, espera **0.1 segundos** antes de volver a comprobar para no sobrecargar los procesos del procesador.

### 7. Detener el Hilo
*   Cuando se presiona la tecla `tecla_escape`, se establece la variable `detener_hilo` en `True`.
*   Esto le indica explícitamente al hilo `rodar()` que debe detenerse de inmediato.
*   Se aguarda a que el hilo termine su ciclo de manera limpia utilizando el método `join()`.

### 8. Detener el Monitoreo de Teclas
*   Se llama a la función `keyboard.unhook_all()` para detener por completo el monitoreo de la presión de teclas en el sistema.

---

## 📝 Notas de Personalización
*   La frecuencia de rodar la pantalla se puede ajustar modificando el valor de la variable `frecuencia`.
*   Se puede cambiar la combinación de teclas para rodar la pantalla modificando el valor de la variable `combo_rodar`.
