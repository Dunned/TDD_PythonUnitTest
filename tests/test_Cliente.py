import unittest

from Entidades.Banco import Banco
from Entidades.Cuenta import Cuenta
from Entidades.Cliente import Cliente


class test_claseCliente(unittest.TestCase):

    def test_CreacionCliente_nCuentas(self):
        c1 = Cliente(73954094, 'Eduardo Rafael', 'Jauregui Romero')
        numeroCuentas = c1.numeroDeCuentas()
        self.assertEqual(numeroCuentas, 0)

    def test_agregarCuenta_NoValida(self):
        c1 = Cliente(73954094, 'Eduardo Rafael', 'Jauregui Romero')
        cuenta1 = Cuenta()
        self.assertTrue(c1.agregarCuenta(Cuenta))

    def test_cuentaAgregadaConNumero(self):
        c1=Cliente(4095369,'Juan Pedro','Santos Borre')
        cuenta1=Cuenta()
        cuenta2=Cuenta()
        c1.agregarCuenta(cuenta1)
        c1.agregarCuenta(cuenta2)
        self.assertEqual(c1.numeroDeCuentas(),2)

    def test_tieneEsaCuenta(self):
        c1=Cliente(52367580,'Marcos Alfonso','Mejia Rodriguez')
        cuenta1=Cuenta()
        cuenta2=Cuenta()
        cuenta3=Cuenta()
        numeroCuentaCreada=cuenta3.numeroCuenta
        c1.agregarCuenta(cuenta1)
        c1.agregarCuenta(cuenta2)
        c1.agregarCuenta(cuenta3)
        agregado=c1.tieneEsaCuenta(numeroCuentaCreada)
        self.assertIsNotNone(agregado)

    def test_noTieneEsaCuenta(self):
        c1 = Cliente(52367580, 'Paolo Jose', 'Guerrero')
        cuenta1 = Cuenta()
        cuenta2 = Cuenta()
        cuenta3 = Cuenta()
        numeroCuentaCreada = cuenta3.numeroCuenta
        c1.agregarCuenta(cuenta1)
        c1.agregarCuenta(cuenta2)
        #c1.agregarCuenta(cuenta3) #NO AGREGADA
        agregado = c1.tieneEsaCuenta(numeroCuentaCreada)
        self.assertIsNone(agregado)

    def test_RealizarTransferencia(self):
        banco=Banco('BCP','Peru')
        cliente1=Cliente(73954094,'Eduardo','Jauregui')
        cliente2=Cliente(73954005,'Rafael','Romero')
        banco.agregarCliente(cliente1)
        banco.agregarCliente(cliente2)
        cuenta1=Cuenta()
        numeroCuenta1=cuenta1.numeroCuenta
        cuenta2=Cuenta()
        numeroCuenta2 = cuenta2.numeroCuenta
        cuenta1.dinero=500
        cliente1.agregarCuenta(cuenta1)
        cliente2.agregarCuenta(cuenta2)
        cliente1.realizarTransferencia(numeroCuenta1,numeroCuenta2,200,73954005,banco)
        self.assertEqual(cuenta1.dinero,300)

    def test_RealizarTransferenciaSinSaldo(self):
        banco=Banco('BCP','Peru')
        cliente1=Cliente(73954094,'Eduardo','Jauregui')
        cliente2=Cliente(73954005,'Rafael','Romero')
        banco.agregarCliente(cliente1)
        banco.agregarCliente(cliente2)
        cuenta1=Cuenta()
        numeroCuenta1=cuenta1.numeroCuenta
        cuenta2=Cuenta()
        numeroCuenta2 = cuenta2.numeroCuenta
        cuenta1.dinero=500
        cliente1.agregarCuenta(cuenta1)
        cliente2.agregarCuenta(cuenta2)
        self.assertFalse(cliente1.realizarTransferencia(numeroCuenta1,numeroCuenta2,1000,73954005,banco))



if __name__ == '__main__':
    unittest.main()
