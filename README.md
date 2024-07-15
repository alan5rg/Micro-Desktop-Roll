Este programa de Python simula la combinación de teclas para rodar
los escritorios virtuales a una frecuencia especificada.

Es importante ejecutar la aplicación con permisos de administrador
para que funcione correctamente. Esto se debe a que el programa
utiliza métodos que requieren interacción a bajo nivel con el
sistema operativo.

-------------------------------------------------------------------

Funcionamiento:

Importaciones: El programa importa las bibliotecas necesarias para su funcionamiento:

threading: Para crear y administrar hilos de ejecución.
time: Para controlar el tiempo y la frecuencia de la acción.
pyautogui: Para simular la interacción con el teclado y el mouse.
keyboard: Para detectar la presión de teclas.


Variables de configuración:

frecuencia: Define el tiempo en segundos entre cada acción de rodar la pantalla.
tecla_escape: Define la tecla que se debe presionar para detener el programa.
combo_rodar: Define la combinación de teclas que se utiliza para rodar la pantalla.


Tiempo de espera inicial:

Se espera 2 segundos antes de iniciar el programa.


Función rodar():

Esta función se ejecuta dentro de un hilo independiente.
Simula la combinación de teclas combo_rodar para rodar la pantalla.
Utiliza un bucle while para repetir la acción a la frecuencia establecida en frecuencia.
Comprueba la variable detener_hilo para determinar si debe detenerse.


Creación e inicio del hilo:

Se crea un objeto threading.Thread con la función rodar() como objetivo.
Se inicia el hilo con el método start().


Bucle principal:

Este bucle se ejecuta en el hilo principal.
Comprueba si la tecla tecla_escape está presionada.
Si la tecla no está presionada, espera 0.1 segundos antes de volver a comprobar.


Detener el hilo:

Cuando se presiona la tecla tecla_escape, se establece la variable detener_hilo en True.
Esto indica al hilo rodar() que debe detenerse.
Se espera a que el hilo termine con el método join().


Detener el monitoreo de teclas:

Se llama a keyboard.unhook_all() para detener el monitoreo de la presión de teclas.

-------------------------------------------------------------------

Ejemplo de uso:

sudo python3 mdsktproll.py

-------------------------------------------------------------------

Notas:

Este programa está diseñado para ejecutarse en sistemas Ubuntu.
La frecuencia de rodar la pantalla se puede ajustar modificando
el valor de la variable frecuencia.
Se puede cambiar la combinación de teclas para rodar la pantalla
modificando el valor de la variable combo_rodar.
Es importante ejecutar la aplicación con permisos de administrador
para que funcione correctamente.

-------------------------------------------------------------------

Explicación de la necesidad de permisos de administrador:

Algunos métodos utilizados en el programa, como la simulación
de la interacción con el teclado a bajo nivel, requieren permisos
de administrador para funcionar correctamente. Esto se debe a que
estos métodos acceden a recursos del sistema que están restringidos
a usuarios con privilegios administrativos.

Al ejecutar el programa con permisos de administrador, se le otorga
el acceso necesario para realizar estas acciones. Si el programa se
ejecuta sin permisos de administrador, es posible que no funcione
correctamente o que genere errores.
