import re

class Banco:

    def __init__(self, nombre: str, pais: str):
            valido=bool(re.search(r'\d', nombre))
            if valido:
                raise Exception('Coloque un nombre correcto')
            valido=bool(re.search(r'\d', pais))
            if valido:
                raise Exception('Coloque un País correcto')
            self.__nombre: str = nombre
            self.__clientes: list = []
            self.__numeroClientes: int = len(self.__clientes)
            self.__pais: str = pais

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property
    def numeroClientes(self):
        return self.__numeroClientes

    @numeroClientes.setter
    def numeroClientes(self, numeroClientes):
        self.__numeroClientes = numeroClientes

    @property
    def clientes(self):
        return self.__clientes

    @clientes.setter
    def clientes(self):
        return self.__clientes

    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, pais):
        self.__pais = pais

    def agregarCliente(self, cliente):
        self.clientes.append(cliente)

    def eliminarCliente(self, cliente):
        pass

    def tieneEseCliente(self,dni):
        indiceCliente=None
        i=0
        for cliente in self.__clientes:
            if cliente.dni==dni:
                indiceCliente=i
                break
            i=i+1
        return indiceCliente

    def dineroInvertidoTotal(self):
        total=0
        for cliente in self.__clientes:
            for cuentap in cliente.cuentas:
                total=total+cuentap.dinero

        return total



