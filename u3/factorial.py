from pila import Pila

class factorial:
    __numero=0
    __factorial=0
    __pila=None
    def __init__(self,num):
        self.__numero=num
        self.__pila=Pila(num)
        self.__pila.insertar(num)
        num-=1
        while num!=0:
            self.__pila.insertar(self.__pila.ultimo()*num)
            num-=1
        print(self.__pila.ultimo())


if __name__=="__main__":
    b=factorial(10)
        
