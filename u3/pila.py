import numpy as np
class Pila():
    __arreglo=[]
    __tope=0
    __tamanio=0
    def __init__(self,tamanio):
        self.__arreglo = np.empty(tamanio,dtype=int)
        self.__tamanio = tamanio
        self.__tope = 0
    def es_vacio(self):
        return self.__tope==0
    def es_llena(self):
        return self.__tope==self.__tamanio
    def insertar(self,objeto):
        if not self.es_llena():
            self.__arreglo[self.__tope]=objeto
            self.__tope+=1
    def suprimir(self):
        if not self.es_vacio():
            self.__arreglo[self.__tope-1]=0
            self.__tope-=1
    def ultimo(self):
        return self.__arreglo[self.__tope-1]
    def mostrar(self):
        for i in range(self.__tope-1,-1,-1):
            print(f"|   {self.__arreglo[i]}   |")
    def mostrar_completo(self):
        # if self.es_vacio():
        #     print("La pila esta vacia")
        # else:
        cadena=""
        for i in range(self.__tope-1,-1,-1):
            cadena+=f"\n|   {self.__arreglo[i]}   |"
        return cadena
    def cerear(self):
        if self.es_vacio():
            for i in range(self.__tamanio):
                self.insertar(0)
        self.__tope=0
    def pop(self):
        obj=self.ultimo()
        self.suprimir()
        return obj
    def fila(self,fila):
        return f"|  {self.__arreglo[fila]}  |"

if __name__=="__main__":
    pila=Pila(3)
    print(pila.es_llena(),pila.es_vacio())
    pila.insertar(3)
    print(pila.es_llena(),pila.es_vacio())
    pila.insertar(2)
    print(pila.es_llena(),pila.es_vacio())
    pila.insertar(1)
    print(pila.es_llena(),pila.es_vacio())
    pila.mostrar()
   
    # pila.mostrar2()
    # pila.mostrar2()
