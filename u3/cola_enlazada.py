from nodo import Nodo
class Cola_link():
    __cabeza=None
    __fin=None
    __cant=0
    def __init__(self):
        self.__cabeza=None
        self.__fin=None
    def insertar(self,objeto):
        nodo=Nodo(objeto)
        if self.__cabeza==None:
            self.__cabeza=nodo
            self.__fin=nodo
            self.__cant=1
        else:
            self.__fin.setSiguiente(nodo)
            self.__fin=nodo
            self.__cant+=1
    def eliminar(self):
        aux=self.__cabeza
        self.__cabeza=self.__cabeza.getSiguiente()
        self.__cant-=1
        return aux.objeto()
    def mostrar_cola(self):
        aux=self.__cabeza
        while aux!=None:
            print(aux.objeto())
            aux=aux.getSiguiente()
        print("======")
    def vacia(self):
        return self.__cabeza==None
    def cantidad(self):
        return self.__cant
    def primero(self):
        return self.__cabeza.objeto()
    def ultimo(self):
        return self.__fin.objeto()



if __name__=="__main__":
    cola=Cola_link()
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
    cola.eliminar()
    cola.mostrar_cola()
    cola.eliminar()
    cola.mostrar_cola()
    cola.insertar(2)
    cola.mostrar_cola()
    cola.insertar(3)
    cola.mostrar_cola()
    