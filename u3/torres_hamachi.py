from pila import Pila
        
class juego:
    __fichas=0
    __torre1=None
    __torre2=None
    __torre3=None
    def __init__(self,fichas):
        self.__fichas=fichas
        self.__torre1=Pila(fichas)
        self.__torre2=Pila(fichas)
        self.__torre3=Pila(fichas)
        self.__movimientos=0
        assert self.__torre1 is not self.__torre2, "las torres son iguales"
        for i in range(fichas,0,-1):
            self.__torre1.insertar(i)
        self.__torre2.cerear()
        self.__torre3.cerear()
        # self.__torre1.mostrar()
        self.jugar()
    def cambiar(self,torres):
        a=False
        if torres==12:
            #torre 1 a torre 2
            if self.__torre1.es_vacio():
                print("Torre 1 no tiene ninguna ficha")
            else:
                if self.__torre2.es_vacio() or self.__torre1.ultimo()<self.__torre2.ultimo():
                    self.__torre2.insertar(self.__torre1.pop())
                    a=True
                    a=True
                else:
                    print("Movimiento no valido")
        elif torres==13:
            if self.__torre1.es_vacio():
                print("Torre 1 no tiene ninguna ficha")
            else:
                if self.__torre3.es_vacio() or self.__torre1.ultimo()<self.__torre3.ultimo():
                    self.__torre3.insertar(self.__torre1.pop())
                    a=True
                else:
                    print("Movimiento no valido")
        elif torres==21:
            if self.__torre2.es_vacio():
                print("Torre 2 no tiene ninguna ficha")
            else:
                if self.__torre1.es_vacio() or self.__torre2.ultimo()<self.__torre1.ultimo():
                    self.__torre1.insertar(self.__torre2.pop())
                    a=True
                else:
                    print("Movimiento no valido")
        elif torres==23:
            if self.__torre2.es_vacio():
                print("Torre 2 no tiene ninguna ficha")
            else:
                if self.__torre3.es_vacio() or self.__torre2.ultimo()<self.__torre3.ultimo():
                    self.__torre3.insertar(self.__torre2.pop())
                    a=True
                else:
                    print("Movimiento no valido")
        elif torres==31:
            if self.__torre3.es_vacio():
                print("Torre 3 no tiene ninguna ficha")
            else:
                if self.__torre1.es_vacio() or self.__torre3.ultimo()<self.__torre1.ultimo():
                    self.__torre1.insertar(self.__torre3.pop())
                    a=True
                else:
                    print("Movimiento no valido")
        elif torres==32:
            if self.__torre3.es_vacio():
                print("Torre 3 no tiene ninguna ficha")
            else:
                if self.__torre2.es_vacio() or self.__torre3.ultimo()<self.__torre2.ultimo():
                    self.__torre2.insertar(self.__torre3.pop())
                    a=True
                else:
                    print("Movimiento no valido, la ficha a colocar es mas grande que la que quedaria debajo")
        else:
            print("""Ingrese los numeros de la siguiente forma:
            12 -> mueve ficha de torre 1 a torre 2
            13 -> mueve ficha de torre 1 a torre 3
            32 -> mueve ficha de torre 3 a torre 2
            etc""")
        if a:
            self.__movimientos+=1
        return
    def mostrar_torres(self):
        for i in range(self.__fichas-1,-1,-1):
            print(f"""{self.__torre1.fila(i)}{self.__torre2.fila(i)}{self.__torre3.fila(i)}""")
    def jugar(self):
        while  not self.__torre3.es_llena():
            self.mostrar_torres()
            a=int(input("Ingrese jugada: "))
            self.cambiar(a)
        self.mostrar_torres()
        print("Ha vencido al sistema!!!!")
        print("Movimientos realizados: ",self.__movimientos)
        print("Movimientos minimos: ",2**self.__fichas-1)
        




if __name__=="__main__":
    a=int(input("Ingrese fichas a jugar: "))
    j=juego(a)