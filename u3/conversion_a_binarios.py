from pila import Pila
class binario:
    __pila=None
    __numero=None
    def __init__(self,numero):
        self.__pila=Pila(10)
        self.__numero=numero
        while numero//2>0:
            self.__pila.insertar(numero%2)
            numero=numero//2
        self.__pila.insertar(numero)
        self.mostrar()
    def mostrar(self):
        print("numero: ",self.__numero,"\nRepresentacion en binario: ")
        self.__pila.mostrar()        
if __name__=="__main__":
    a=binario(2)