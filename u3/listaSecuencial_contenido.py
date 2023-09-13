import numpy as np
import unittest
class Lista_secuencial_cont:
    __tamanio=0
    __ultimo=0
    __arreglo=None
    def __init__(self,tamanio):
        self.__tamanio=tamanio
        self.__arreglo=np.empty(tamanio,dtype=int)
        self.__ultimo=0
    def insertar(self,objeto):
        if self.llena():
            print("Lista llena")
            return
        if self.__ultimo==0:
            self.__arreglo[0]=objeto
        else:
            i=0
            flag=False
            while i<self.__ultimo and not flag:
                if objeto<self.__arreglo[i]:
                    flag=True
                else:
                    i+=1
            if i<self.__ultimo:
                for j in range(self.__ultimo,i,-1):
                    self.__arreglo[j]=self.__arreglo[j-1]
            self.__arreglo[i]=objeto
        self.__ultimo+=1
    def suprimir(self,posicion):
        if not (posicion>=1 and posicion<=self.__ultimo):
            print("fuera de rango")
            return
        if self.vacia():
            print("No se puede suprimir, lista vacia")
            return
        posicion-=1
        for i in range(posicion,self.__ultimo-1):
            self.__arreglo[i]=self.__arreglo[i+1]
        self.__ultimo-=1
    def buscar(self,elemento):
        i=0
        flag=False
        while i<self.__ultimo and not flag:# and self.__arreglo[i]<el:
            if self.__arreglo[i]==elemento:
                flag=True
            else:
                i+=1
        if flag:
            i+=1
        else:
            print("No se ecnontro el objeto")
            i=-1
        return i
    def recuperar(self,posicion):
        if not (posicion>=1 and posicion<=self.__ultimo):
            print("fuera de rango")
            return
        posicion-=1
        return self.__arreglo[posicion]
    def mostrar(self):
        for i in range(self.__ultimo):
            print(self.__arreglo[i])
    def llena(self):
        return self.__tamanio==self.__ultimo
    def vacia(self):
        return self.__ultimo==0
    def len(self):
        return self.__ultimo
    
class Test_lista_sec_cont(unittest.TestCase):
    def setUp(self):
        self.__a=Lista_secuencial_cont(10)
        self.__a.insertar(1)
        self.__a.insertar(2)
        self.__a.insertar(3)
        self.__a.insertar(4)
        self.__a.insertar(5)
        self.__a.insertar(6)
        self.__a.insertar(7)
        self.__a.insertar(8)
        self.__a.insertar(9)
        self.__a.insertar(10)
        self.__b=Lista_secuencial_cont(5)
        self.__b.insertar(1)
        self.__b.insertar(2)
        self.__b.insertar(3)
    def test_supr_inv(self):
        a=self.__b.len()
        self.__b.suprimir(4)
        self.assertEqual(self.__b.len(),a)
    def test_supr_val(self):
        a=self.__b.len()
        self.__b.suprimir(2)
        self.assertEqual(self.__b.len(),a-1)
    def test_ins_inv(self):
        l=self.__a.len()
        self.__a.insertar(11)
        self.assertEqual(self.__a.len(),l)
        self.assertEqual(-1,self.__a.buscar(11))
    def test_ins_val(self):
        self.assertEqual(-1,self.__b.buscar(11))
        l=self.__b.len()
        self.__b.insertar(11)
        self.assertEqual(self.__b.len(),l+1)
        self.assertEqual(self.__b.buscar(11),4)
    def test_buscar_recuperar(self):
        el=5
        pos=4
        self.assertEqual(self.__b.buscar(el),-1)
        self.__b.insertar(el)
        self.assertEqual(self.__b.buscar(el),pos)
        self.assertEqual(self.__b.recuperar(pos),el)
        self.assertEqual(self.__a.buscar(5),5)
        
 
if __name__=="__main__":
    # unittest.main()
    a=Lista_secuencial_cont(4)
    a.insertar(3)
    a.insertar(2)
    a.insertar(1)
    a.insertar(4)
    a.mostrar()