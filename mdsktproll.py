#!UTC/Encode to Python with Monkey Python Coddebuging Circus by Alan.R.G.Systemas
import threading 
import time
import pyautogui
import keyboard

# Variables de configuración
frecuencia = 1.9 # tiempo en segundos
tecla_escape = 'esc'
combo_rodar = ['ctrl', 'alt', 'right']

# Variable de control para detener el hilo
detener_hilo = threading.Event()

time.sleep(2) # tiempo de espera antes de comenzar el programa

# Funcion que se ejecuta dentro del hilo
def rodar():
    """Simula la combinación de teclas para rodar la pantalla."""
    next_time = time.time() + frecuencia
    while not detener_hilo.is_set():
        pyautogui.hotkey(*combo_rodar)
        sleep_time = next_time - time.time()
        if sleep_time >= 0:
        	if detener_hilo.wait(sleep_time):
                    break
        next_time += frecuencia

# Crea y comienza el hilo que ejecuta rodar
hilo = threading.Thread(target=rodar)
hilo.start()

# Bucle principal para escuchar la tecla de escape
while not keyboard.is_pressed(tecla_escape):
    time.sleep(0.1)

# Detiene el hilo asegurando que termine sus tareas
detener_hilo.set()
hilo.join()

# Detiene el monitoreo de teclas
keyboard.unhook_all()