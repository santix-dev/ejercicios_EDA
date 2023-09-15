class Nodo_bin():
    __dato=None
    __ant=None
    __sig=None
    def __init__(self,dato):
        self.__dato=dato
    def set_siguiente(self,sig):
        self.__sig=sig
    def set_anterior(self,ant):
        self.__ant=ant
    def get_anterior(self):
        return self.__ant
    def get_siguiente(self):
        return self.__sig
    def dato(self):
        return self.__dato
    
    