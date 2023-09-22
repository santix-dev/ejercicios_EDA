from nodo_binario import Nodo_bin
class Arbol():
    __raiz=None
    def __init__(self):
        self.__raiz=None
    def insertar(self,dato,raiz=None):
        if raiz==None: raiz=self.__raiz
        if self.__raiz==None:
            neuvo=Nodo_bin(dato)
            self.__raiz=neuvo
        else:
            if dato==raiz.dato():
                print("Elemento ya existente")
            else:    
                if dato<raiz.dato():
                    if not raiz.izquierda_isnull():
                        return self.insertar(dato,raiz.get_izquierda())
                    raiz.set_izquierda(Nodo_bin(dato))
                else:
                    if not raiz.derecha_isnull():
                        return self.insertar(dato,raiz.get_derecha())
                    raiz.set_derecha(Nodo_bin(dato))
                    
    def mostrar(self,raiz=None):
        if raiz==None: raiz=self.__raiz
        if not raiz.izquierda_isnull():
            self.mostrar(raiz.get_izquierda())
            print(raiz.dato())
        else:
            print(raiz.dato())
        if not raiz.derecha_isnull():
            self.mostrar(raiz.get_derecha())
            return
    def altura(self,raiz=None,nivel=1,izquierda=0,derecha=0):
        if raiz==None: raiz=self.__raiz
        if not raiz.izquierda_isnull():
            izquierda=self.altura(raiz.get_izquierda(),nivel+1,izquierda+1,derecha)
        if not raiz.derecha_isnull():
            derecha=self.altura(raiz.get_derecha(),nivel+1,izquierda,derecha+1)
        nivel=derecha if derecha>izquierda else izquierda
        return nivel
        # if not raiz.izquierda_isnull() or not raiz.derecha_isnull():
        #     nivel+=1
        # if not raiz.izquierda_isnull():
        #     nivel = self.altura(raiz.get_izquierda(),nivel)
        #     if mayor<nivel: mayor = nivel
        #     if not raiz.derecha_isnull():
        #         nivel = self.altura(raiz.get_derecha(),nivel)
        #         if mayor<nivel: mayor = nivel
        # else:
        #     if not raiz.derecha_isnull():
        #         nivel = self.altura(raiz.get_derecha(),nivel)
        #         if mayor<nivel: mayor = nivel
        # return nivel
    def buscar(self,dato,raiz=None):
        if raiz==None: raiz=self.__raiz
        while raiz!=None:
            if raiz.dato()==dato:
                return True
            else:    
                if raiz.dato()<dato:
                    raiz=raiz.get_derecha()
                else:
                    raiz=raiz.get_izquierda()
        return False
    def nivel(self,dato):
        raiz=self.__raiz
        i=1
        while raiz!=None:
            if raiz.dato()==dato:
                return i
            else:    
                if raiz.dato()<dato:
                    raiz=raiz.get_derecha()
                    i+=1
                else:
                    raiz=raiz.get_izquierda()
                    i+=1
        return -1
    def hijo(self,clave,valor,raiz=None):
        if raiz==None: raiz=self.__raiz
        flag=False
        while raiz!=None:
            if raiz.dato()==clave:
                if not raiz.derecha_isnull():
                    print("a")
                    flag = raiz.get_derecha().dato()==valor
                if not raiz.izquierda_isnull():
                    flag = raiz.get_izquierda().dato()==valor
                raiz=None
            else:    
                if raiz.dato()<clave:
                    raiz=raiz.get_derecha()
                else:
                    raiz=raiz.get_izquierda()
        return flag
    def padre(self,clave,valor):
        return self.hijo(valor,clave)
    def suprimir(self,clave):
        pass

if __name__=="__main__":
    a=Arbol()
    a.insertar(10)
    a.insertar(12)
    a.insertar(11)
    a.insertar(6)
    a.insertar(5)
    a.insertar(4)
    a.insertar(8)
    a.insertar(3)
    # a.insertar(13)
    # a.insertar(14)
    a.mostrar()
    print(a.altura())
    print(a.buscar(7))
    print(a.nivel(12))
    print(a.hijo(4,5))
    print(a.padre(5,4))




