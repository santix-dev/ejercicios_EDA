from cola_secuencial_1 import Cola_sec
from cola_enlazada import Cola_link
import random


if __name__=="__main__":
    cola=Cola_link()
    acumulador=0
    contador=0
    caja=0
    tiempo_limite=int(input("Ingrese tiempo limite: "))
    frecuencia=int(input("Ingrese frecuencia llegada: "))
    tiempo_caja=int(input("Ingrese tiempo caja: "))
    for i in range(tiempo_limite):
        llego=random.randint(0,frecuencia)
        # print60(llego)
        if llego==frecuencia:
            cola.insertar(i)
        if caja==0:
            if not cola.vacia():
                acumulador+=i-cola.eliminar()
                contador+=1
                caja=1
        elif caja<tiempo_caja:
            caja+=1
        else:
            caja=0
    print(f"Clientes que quedaron en cola: {cola.cantidad()}")
    print(f"Tiempo total acumulado de espera: {acumulador}")
    if cola.vacia():
        print("No quedo nadie en cola")
    else:
        print(f"Tiempo que lleva esperando el ultimo en la cola: {tiempo_limite-cola.ultimo()}")
        print(f"Tiempo que lleva esperando el que seguia en la cola: {tiempo_limite-cola.primero()}")
    print(f"Clientes atendidos: {contador}")
    print(f"Tiempo de espera promedio: {round(acumulador/contador,2)}")
    
