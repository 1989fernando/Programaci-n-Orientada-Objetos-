import threading
import time

# Definición de la tarea que se ejecutará en cada hilo
def tarea(nombre):
    print(f"Tarea {nombre} iniciada")
    # Simulación de una tarea que toma tiempo (por ejemplo, una operación de I/O o procesamiento)
    time.sleep(2)
    print(f"Tarea {nombre} finalizada")

# Creación de los hilos
hilo1 = threading.Thread(target=tarea, args=("Hilo 1",))
hilo2 = threading.Thread(target=tarea, args=("Hilo 2",))

# Inicio de los hilos
hilo1.start()
hilo2.start()

# Sincronización de hilos: esperar a que ambos hilos terminen
hilo1.join()
hilo2.join()

# Finalización del programa
print("Todos los hilos han terminado")