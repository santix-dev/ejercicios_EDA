class Nodo_bin():
    __dato=None
    __izquierda=None
    __derecha=None
    def __init__(self,dato):
        self.__dato=dato
    def set_derecha(self,sig):
        self.__derecha=sig
    def set_izquierda(self,ant):
        self.__izquierda=ant
    def get_izquierda(self):
        return self.__izquierda
    def get_derecha(self):
        return self.__derecha
    def dato(self):
        return self.__dato
    def izquierda_isnull(self):
        return self.__izquierda==None
    def derecha_isnull(self):
        return self.__derecha==None
    def grado(self):
        if self.__derecha==None:
            if self.__izquierda==None:
                return 0
            return 1
        elif self.__izquierda==None:
            return 1
        return 2

if __name__=="__main__":
    a=Nodo_bin(7)
    a.set_izquierda(5)
    # a.set_derecha(5)
    print(a.grado())

    