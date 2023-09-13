from nodo import Nodo

class Lista_link_cont():
	"""docstring for Lista"""
	__cant=0
	__comienzo=None
	def __init__(self):
		self.__comienzo = None
		self.__cant=0
	def insertar(self,objeto):
		nuevo=Nodo(objeto)
		if self.__comienzo==None or objeto<=self.__comienzo.objeto():
			nuevo.setSiguiente(self.__comienzo)
			self.__comienzo=nuevo
		else:
			aux=self.__comienzo
			anterior=self.__comienzo
			flag=False
			while aux!=None and not flag:
				if aux.objeto()<objeto:
					anterior=aux#aca quede
					aux=aux.getSiguiente()
				else: flag=True
			anterior.setSiguiente(nuevo)
			nuevo.setSiguiente(aux)
		self.__cant+=1
	def suprimir(self,posicion):
		if not (posicion>=1 and posicion<=self.__cant):
			print("fuera de rango")
			return
		if posicion==1:
			aux=self.__comienzo
			self.__comienzo = self.__comienzo.getSiguiente()
		else:
			i=1
			aux=self.__comienzo
			ant=None
			while i<posicion:
				ant=aux
				i+=1
				aux=aux.getSiguiente()
			ant.setSiguiente(aux.getSiguiente())
		self.__cant-=1
		del aux
	def recuperar(self,posicion):
		i=1
		nodo=self.__comienzo
		while nodo!=None and i<posicion:
			i+=1
			nodo=nodo.getSiguiente()
		if nodo!=None:
			print(nodo.objeto())
			return nodo.objeto()
		else:
			print("No existe esa posicion")
	def buscar(self,el):
		i=1
		aux=self.__comienzo
		while i<=self.__cant and aux.objeto()!=el:
			aux=aux.getSiguiente()
			i+=1
		print(f"posicion de {el}: {i}")
		return i
	def mostrar(self):
		i=0
		aux=self.__comienzo
		while i<self.__cant and aux!=None:
			print(f"elemento: {aux.objeto()}")
			aux=aux.getSiguiente()
			i+=1
	

if __name__=="__main__":
	lista=Lista_link_cont()
	lista.insertar("molina marcos")
	lista.insertar("gimenez santiago")
	lista.insertar("garro guillermo")
	lista.insertar("b")
	lista.insertar("a")
	lista.insertar("d")
	lista.insertar("a")
	lista.mostrar()
	a=lista.buscar("gimenez santiago")
	print(a)
	lista.suprimir(a)
	lista.mostrar()

