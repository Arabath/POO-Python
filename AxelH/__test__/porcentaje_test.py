import unittest
from porcentaje import Porcentaje

from exeption_porcentaje import ImposibleDividirPorCero
from porcentaje import Porcentaje

class TestPorcentaje(unittest.TestCase):
    def setUp(self) -> None:
        self.porcentaje = Porcentaje(45)

    def test_aplicarA(self):
        """ pass """
      
        resultado = self.porcentaje.aplicarA(100)

        self.assertEqual(resultado,45)

    def test_elDividendoNoPuedeSerCero(self):
        """ pass """

        porcentaje = Porcentaje(45)

        with self.assertRaises(ImposibleDividirPorCero):
            porcentaje.aplicarA(0)


if __name__ == "__main__":
    unittest.main()