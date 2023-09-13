import numpy as np
from nodo import Nodo
class Cola_circular():
    __arreglo=None
    __primero=None
    __ultimo=None
    __tamanio=None
    __cant=0
    def __init__(self,tamanio):
        self.__arreglo=np.empty(tamanio, dtype=int)
        self.__tamanio=tamanio
        self.__cant=0
        self.__primero=0
        self.__ultimo=0
    def insertar(self,objeto):
        if self.lleno():
            print("cola llena, espere")
            return
        if self.__cant<self.__tamanio:
            self.__arreglo[self.__ultimo]=objeto
            self.__ultimo=(self.__ultimo+1)%self.__tamanio
            self.__cant+=1
        # if self.need_order():
        #     self.ordenar()
        # if self.__primero==-1 and self.__ultimo==-1:
        #     self.__primero=0
        #     self.__ultimo=0
        #     self.__arreglo[self.__primero]=objeto
        # elif self.__primero<=self.__ultimo:
        #     self.__ultimo+=1
        #     self.__arreglo[self.__ultimo]=objeto
        # elif self.__primero>self.__ultimo:
        #     self.__primero=-1
        #     self.__ultimo=-1
        #     self.insertar(objeto)
    # def need_order(self):
    #     return self.__primero>0 and self.__ultimo==self.__tamanio-1
    # def ordenar(self):
    #     cantidad=self.__ultimo-self.__primero
    #     for i in range(cantidad):
    #         self.__arreglo[i]=self.__arreglo[i+self.__primero]
    #     self.__primero=0
    #     self.__ultimo=cantidad-1
    def lleno(self):
        return self.__cant==self.__tamanio
    def eliminar(self):
        aux=self.__arreglo[self.__primero]
        self.__primero=(self.__primero+1)%self.__tamanio
        self.__cant-=1
        return aux
        # self.__primero+=1
    def mostrar_cola(self):
        # for i in range(self.__primero,self.__ultimo+1):
        #     print(self.__arreglo[i])
        i=self.__primero
        j=0
        while j<self.__cant:
            print(self.__arreglo[i])
            i=(i+1)%self.__tamanio
            j+=1

        print("======")


if __name__=="__main__":
    cola=Cola_circular(5)
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
    cola.insertar(5)
    cola.mostrar_cola()
    cola.eliminar()
    cola.mostrar_cola()
    cola.eliminar()
    cola.mostrar_cola()
    cola.insertar(2)
    cola.mostrar_cola()
    cola.insertar(3)
    cola.mostrar_cola()
    