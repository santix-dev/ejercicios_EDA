import numpy as np
from nodo import Nodo
class Cola_sec():
    __arreglo=None
    __primero=None
    __ultimo=None
    __tamanio=None
    def __init__(self,tamanio):
        self.__arreglo=np.empty(tamanio, dtype=int)
        self.__primero=-1
        self.__ultimo=-1
        self.__tamanio=tamanio
    def insertar(self,objeto):
        if self.lleno():
            print("cola llena, espere")
            return
        if self.need_order():
            self.ordenar()
        if self.__primero==-1 and self.__ultimo==-1:
            self.__primero=0
            self.__ultimo=0
            self.__arreglo[self.__primero]=objeto
        elif self.__primero<=self.__ultimo:
            self.__ultimo+=1
            self.__arreglo[self.__ultimo]=objeto
        elif self.__primero>self.__ultimo:
            self.__primero=-1
            self.__ultimo=-1
            self.insertar(objeto)
    def need_order(self):
        return self.__primero>0 and self.__ultimo==self.__tamanio-1
    def ordenar(self):
        cantidad=self.__ultimo-self.__primero
        for i in range(cantidad+1):
            print(self.__ultimo-self.__primero,cantidad)
            self.__arreglo[i]=self.__arreglo[i+self.__primero]
            print(f"i: {i}    num:  {self.__arreglo[self.__primero+i]}")
            print(f"i: {i}    num:  {self.__arreglo[i]}")
        self.__primero=0
        self.__ultimo=cantidad
    def lleno(self):
        return self.__ultimo+1==self.__tamanio and self.__primero==0
    def eliminar(self):
        self.__primero+=1
    def mostrar_cola(self):
        for i in range(self.__primero,self.__ultimo+1):
            print(self.__arreglo[i])
        print("======")


if __name__=="__main__":
    cola=Cola_sec(5)
    cola.insertar(1)
    cola.mostrar_cola()
    cola.insertar(2)
    cola.mostrar_cola()
    cola.insertar(3)
    cola.mostrar_cola()
    cola.insertar(4)
    cola.mostrar_cola()
    cola.insertar(5)
    cola.mostrar_cola()
    cola.insertar(5)#
    cola.mostrar_cola()
    cola.eliminar()
    cola.mostrar_cola()
    cola.eliminar()
    cola.mostrar_cola()
    cola.insertar(2)
    cola.mostrar_cola()
    cola.insertar(3)
    cola.mostrar_cola()
    