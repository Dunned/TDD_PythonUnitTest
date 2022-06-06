import random

class Cuenta():
    def __init__(self):
        self.__numeroCuenta=random.randrange(10000,99999)
        self.__dinero = 0

    @property
    def numeroCuenta(self):
        return self.__numeroCuenta

    @property
    def dinero(self):
        return self.__dinero

    @dinero.setter
    def dinero(self,dinero):
        self.__dinero=dinero

    def __str__(self):
        return f'#CUENTA : {self.numeroCuenta} , dinero almacenado de : {self.dinero}'



