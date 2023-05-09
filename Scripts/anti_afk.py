# Autor: @strpalgato
# Fecha: 09-05-2023
# Descripción: Programa que mueve el personaje en un juego para evitar que el juego se cierre por inactividad.

import pyautogui # libreria para controlar el mouse y el teclado (requiere descargarla previamente)
import time # libreria para controlar el tiempo
from tqdm import tqdm # libreria para mostrar una barra de progreso (requiere descargarla previamente)

def mover():
    i = 1 # contador de repeticiones
    while(i<=3):
        print("Ejecutando primer movimiento")
        pyautogui.keyDown('w')
        time.sleep(3.5) 
        pyautogui.keyUp('w')
        time.sleep(0.1)
        print("Ejecutando segundo movimiento")
        pyautogui.keyDown('a')
        time.sleep(3.5)
        pyautogui.keyUp('a')
        time.sleep(0.1)
        print("Ejecutando tercer movimiento")
        pyautogui.keyDown('s')
        time.sleep(3.5)
        pyautogui.keyUp('s')
        time.sleep(0.1)
        print("Ejecutando cuarto movimiento")
        pyautogui.keyDown('d')
        time.sleep(3.5)
        pyautogui.keyUp('d')
        time.sleep(0.1)
        i+=1

print('\nPrograma iniciado\n')
for i in tqdm(range(100)):
    time.sleep(0.04)

print("\nCarga completada\n")

while True:
    try:
        mover()
        print('\nEl siguiente ciclo comenzará en 3 minutos\n') # mensaje que se muestra antes de comenzar el siguiente ciclo
        for i in tqdm(range(100)):
            time.sleep(1.8) # 1.8 segundos = 0.03 minutos | 3 minutos = 180 segundos | 180/1.8 = 100%
        print("")
    except KeyboardInterrupt:
        break
print('\nPrograma detenido\n')
        
# NOTA: para detener el programa presiona la tecla CTR+C
# NOTA: para que el programa funcione correctamente debes tener el juego en pantalla completa.

