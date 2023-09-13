import numpy as np
from nodo import Nodo
class Pila():
    __tope=None
    def __init__(self,tamanio):
        self.__tamanio=tamanio
        self.__tope=None
    def es_vacio(self):
        return self.__tope==None
    # def es_llena(self):
    #     return self.__tope==self.__tamanio
    def insertar(self,objeto):
        nodo=Nodo(objeto)
        if self.__tope==None:
            self.__tope=nodo
        else:
            nodo.setSiguiente(self.__tope)
            self.__tope=nodo
    def suprimir(self):
        if not self.es_vacio():
            self.__tope=self.__tope.getSiguiente()
    def ultimo(self):
        return self.__tope.objeto()
    def mostrar(self):
        aux=self.__tope
        while aux!=None:
            print(aux.objeto())
            aux=aux.getSiguiente()
    def mostrar_completo(self):
        # if self.es_vacio():
        #     print("La pila esta vacia")
        # else:
        cadena=""
        aux=self.__tope
        while aux!=None:
            cadena+=f"\n|   {self.__tope.objeto()}   |"
            aux=aux.getSiguiente()
        return cadena
    # def cerear(self):
    #     if self.es_vacio():
    #         for i in range(self.__tamanio):
    #             self.insertar(0)
    def pop(self):
        obj=self.ultimo()
        self.suprimir()
        return obj
    def fila(self,fila):
        return f"|  {self.__arreglo[fila]}  |"

if __name__=="__main__":
    pila=Pila(3)
    # print(pila.es_llena(),pila.es_vacio())
    pila.insertar(3)
    # print(pila.es_llena(),pila.es_vacio())
    pila.insertar(2)
    # print(pila.es_llena(),pila.es_vacio())
    pila.insertar(1)
    # print(pila.es_llena(),pila.es_vacio())
    pila.mostrar()
    a,b=eval("1,2")
    print(a," ",b)
    # pila.mostrar2()
    # pila.mostrar2()
