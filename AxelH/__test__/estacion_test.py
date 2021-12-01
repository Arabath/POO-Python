import unittest
from estacion import Estacion
from surtidor import Surtidor

class TestEstacionDeServicio(unittest.TestCase):
    def setUp(self) -> None:
        self.estacion = Estacion()
        self.surtidorUno = Surtidor(100)

    """ pass """
    def test_alInstanciarseNoTendraSurtidores(self):
        self.assertListEqual(self.estacion.surtidores, [])

    def test_seAgregaUnSurtidorALaEstacion(self):
        """ pass """
        self.assertListEqual(self.estacion.surtidores, [])
        self.assertEqual(self.estacion.cantidadDeSurtidores(), 0)

        self.estacion.agregarSurtidor(self.surtidorUno)

        self.assertEqual(self.estacion.cantidadDeSurtidores(), 1)
        self.assertListEqual(self.estacion.surtidores, [self.surtidorUno])

    def test_cantidadDeSurtidoresDeUnaEstacionVacia(self): 
        """ Cuantos surtidores posee la estacion. """
        self.assertEqual(self.estacion.cantidadDeSurtidores(), 0)

        for _ in range(3): self.estacion.agregarSurtidor(self.surtidorUno)

        self.assertEqual(self.estacion.cantidadDeSurtidores(),3)

    def test_cualesSurtidoresVacios(self):
        """ Cuales surtiodres vacios posee la estación """
        self.estacion.agregarSurtidor(self.surtidorUno)

        self.assertEqual(self.surtidorUno.carga,  0)
        self.assertEqual(self.estacion.cantidadDeSurtidores(), 1)
        self.assertListEqual(self.estacion.surtidoresVacios(), [self.surtidorUno])

        self.surtidorUno.cargar(50)

        self.assertEqual(self.surtidorUno.carga, 50)
        self.assertListEqual(self.estacion.surtidoresVacios(), [])       

    def test_saberCuantosSurtidoresVacios(self): 
        """ Cuantos surtidores vacios posee la estación """
        surtidorDos = Surtidor(100)
        self.estacion.agregarSurtidor(self.surtidorUno) 
        self.estacion.agregarSurtidor(surtidorDos)

        self.assertEqual(self.estacion.cantidadDeSurtidores(), 2)

        surtidorDos.cargar(100)

        self.assertEqual(self.estacion.cantidadSurtidoresVacios(), 1)
    
    def test_cantidadDeLitrosFaltantes(self): 
        """ Cuantos litros faltan para completar la carga total del surtidor """
        surtidorDos = Surtidor(100)
        
        self.estacion.agregarSurtidor(surtidorDos)
        surtidorDos.cargar(50)

        self.assertEqual(self.estacion.litrosFaltantes(), 50)
    
    def test_costoDeCargaLitrosFaltantes(self): 
        """ pass """
        self.surtidorUno.cargar(100)
        self.estacion.agregarSurtidor(self.surtidorUno)

        





if  __name__ == '__main__':
    unittest.main()

        

