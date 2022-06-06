import unittest
from Entidades.Banco import Banco


class test_claseBancoLimite(unittest.TestCase):

    def test_creacion_incorrectoNombre(self):
        with self.assertRaises(Exception) as exp:
            banco1 = Banco('166692FWrh', 'Peru')
        self.assertEqual(str(exp.exception), 'Coloque un nombre correcto')

    def test_creacion_incorrectoPais(self):
        with self.assertRaises(Exception) as exp:
            banco1 = Banco('BCP', '53535')
        self.assertEqual(str(exp.exception), 'Coloque un País correcto')


if __name__=='__main__':
    unittest.main()

