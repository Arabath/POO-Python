import unittest
from cuentaCorriente import  CuentaCorriente
from excepciones import ImposibleRealizarExtraccion

class TestCuentaCorriente(unittest.TestCase):
    # ---- setup de la clase CuentaCorrientes ---- #
    def setUp(self) -> None:
        self.cuenta = CuentaCorriente('Juan', 0 , 500)

    def test_cuentaInicializaConElMontoEspecificado(self):
        """ Al crear la caja de ahorro se especifica el saldo inicial """
        cuenta = CuentaCorriente('Marcos', 100, 200)

        self.assertEqual(cuenta.saldo, 100)    
    
    def test_depositarSaldoEnUnaCuenta(self):
        """ Se deposita un monto en una cuenta corriente """
        self.assertEqual(self.cuenta.saldo, 0)

        self.cuenta.depositar(1200)

        self.assertEqual(self.cuenta.saldo, 1200)

    def test_depositarSaldoEnUnaCuentaConSaldo(self):
        """ Se deposita un monto en una cuenta corriente con saldo """
        self.cuenta.depositar(100)

        self.assertEqual(self.cuenta.saldo, 100)

        self.cuenta.depositar(100)

        self.assertEqual(self.cuenta.saldo, 200)

    