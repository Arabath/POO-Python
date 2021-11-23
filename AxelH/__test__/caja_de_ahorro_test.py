import unittest
from caja_de_ahorro import CajaDeAhorro

class TestCajaDeAhorro(unittest.TestCase):
    def setUp(self) -> None:
        self.cuenta = CajaDeAhorro()


    def test_depositarSaldoEnUnaCuenta(self):
        """ Se deposita un monto en una caja de ahorro """
        self.assertEqual(self.cuenta.saldo,0)


    def test_depositarSaldoEnUnaCuenta(self):
        """ Se deposita un monto en una caja de ahorro """
        self.assertEqual(self.cuenta.saldo, 0)

        self.cuenta.depositarMonto(100)
        self.cuenta.depositarMonto(1000)

        self.assertEqual(self.cuenta.saldo, 1100)

    def test_NoSePuedeExtraerUnMonto(self):
        """ El monto de la extracción supera el saldo """
        self.assertFalse(self.cuenta.puedeExtraer(100))

    def test_sePuedeExtraerUnMonto(self):
        """ Extracción en una caja de ahorro """
        self.cuenta.depositarMonto(100)

        self.assertTrue(self.cuenta.puedeExtraer(100))