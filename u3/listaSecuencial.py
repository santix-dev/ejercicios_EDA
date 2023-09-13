import numpy as np

class Lista_secuencial:
    __tamanio=0
    __ultimo=0
    __arreglo=None
    def __init__(self,tamanio):
        self.__tamanio=tamanio
        self.__arreglo=np.empty(tamanio)
        self.__ultimo=-1
    def insertar(self,objeto,posicion):
        if not (posicion>=1 and posicion<=self.__tamanio):
            print("fuera de rango")
            return
        if self.llena():
            print("Lista llena")
            return
        posicion-=1
        if self.__ultimo>=posicion:
            for i in range(self.__ultimo+1,posicion-1,-1):
                self.__arreglo[i]=self.__arreglo[i-1]
        self.__arreglo[posicion]=objeto
        self.__ultimo=self.__ultimo+1
    def suprimir(self,posicion):
        if not (posicion>=1 and posicion<=self.__tamanio):
            print("fuera de rango")
            return
        if self.vacia():
            print("No se puede suprimir, lista vacia")
            return
        posicion-=1
        for i in range(posicion,self.__ultimo):
            self.__arreglo[i]=self.__arreglo[i+1]
        self.__ultimo-=1
    def buscar(self,el):
        i=-1
        flag=False
        while i<self.__ultimo+1 and not flag:
            i+=1
            if self.__arreglo[i]==el:
                flag=True
        if flag:
            return i+1
        else:
            print("No se ecnontro el objeto")
        return None
    def recuperar(self,posicion):
        if not (posicion>=1 and posicion<=self.__ultimo):
            print("fuera de rango")
            return
        posicion-=1
        return self.__arreglo[posicion]
    def mostrar(self):
        for i in range(self.__ultimo+1):
            print(self.__arreglo[i])
    def llena(self):
        return self.__tamanio-1==self.__ultimo
    def vacia(self):
        return self.__ultimo==-1
if __name__=="__main__":
    a=Lista_secuencial(3)
    a.insertar(1,1)
    a.insertar(2,2)
    a.insertar(3,2)
    a.mostrar()
    a.insertar(3,3)
    a.insertar(3,2)
    a.insertar(3,4)
    a.insertar(3,0)
    a.suprimir(1)
    a.mostrar()
    print("======")
    a.insertar(1,3)
    a.mostrar()
    print("======")
    a.suprimir(1)
    a.mostrar()
    print("======")
    a.suprimir(1)
    a.mostrar()
    print("======")
    a.suprimir(1)
    a.mostrar()
    print("======")
    a.suprimir(1)
    a.mostrar()
    print("======")
