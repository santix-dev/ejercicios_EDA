class Nodo(object):
	__objeto = None
	__siguiente = None
	def __init__(self, objeto):
		self.__objeto = objeto
		self.__siguiente = None
	def setSiguiente(self,siguiente):
		self.__siguiente=siguiente
	def getSiguiente(self):
		return self.__siguiente
	def objeto(self):
		return self.__objeto
		