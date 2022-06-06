import unittest
from Entidades.Banco import Banco


class test_claseBanco(unittest.TestCase):

    def test_creacion_banco(self):
        banco1=Banco('Banco de Credito del Peru','Peru')
        self.assertEqual(banco1.nombre,'Banco de Credito del Peru')

    def test_numeroClientesBancoVacio(self):
        banco1=Banco('INTERBANK','Peru')
        self.assertEqual(banco1.numeroClientes,0)

    def test_dineroInvertidoBancoVacio(self):
        banco1=Banco('PICHINCHA','Peru')
        dineroInvertidoSupuesto=0
        self.assertEqual(dineroInvertidoSupuesto,banco1.dineroInvertidoTotal())

if __name__=='__main__':
    unittest.main()

