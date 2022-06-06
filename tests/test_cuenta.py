import unittest

from Entidades.Cliente import Cliente
from Entidades.Cuenta import Cuenta


class test_cuenta(unittest.TestCase):

    def test_creacionCuenta(self):
        cuenta1=Cuenta()
        numeroCuenta=cuenta1.numeroCuenta
        dinero=cuenta1.dinero
        self.assertEqual(cuenta1.numeroCuenta,numeroCuenta)

    def test_creacionCuentaMontoInicial(self):
        cuenta1=Cuenta()
        numeroCuenta=cuenta1.numeroCuenta
        dinero=cuenta1.dinero
        self.assertEqual(dinero,0)


    def test_eliminarCuentaCliente(self):
        cliente=Cliente(73954094,'Jauregui','Eduardo')
        cuenta1=Cuenta()
        numeroCuenta=cuenta1.numeroCuenta
        cliente.agregarCuenta(cuenta1)
        cliente.eliminarCuenta(numeroCuenta)
        self.assertEqual(cliente.numeroDeCuentas(),0)

if __name__=='__main__':
    unittest.main()