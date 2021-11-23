import unittest
from robot import Robot

class TestRobbot(unittest.TestCase):
    def setUp(self):
        self.robot = Robot(10)

    def test_elRobotPuedeCaminarUnaDistancia(self): 
        """ Al caminar una distancia el robot decrementa sus unidades de bateria """
        self.assertEqual(self.robot.bateria,10)

        self.robot.caminar(10)

        self.assertEqual(self.robot.bateria,9)

    def test_elRobotNoPuedeCaminarCuandoLaBateriaNoEsSuficiente(self): 
        """ No se puede caminar una distancia cuando la bateria no es suficiente """
        self.assertEqual(self.robot.bateria,10)

        with self.assertRaisesRegex(ValueError, 'Unidades de bateria insuficiente'):
            self.robot.caminar(101)
        self.assertEqual(self.robot.bateria,10)
        
    def test_cargaDeBateria(self): 
        """ No puede superar las 100 energías de carga """        
        self.assertEqual(self.robot.bateria, 10)

        self.robot.cargaBateria(10)

        self.assertEqual(self.robot.bateria, 20)

    def test_laCargaNoPuedeExcederLasCienUnidades(self): 
        """ pass """
        self.assertEqual(self.robot.bateria, 10)

        self.robot.cargaBateria(91)
        
        self.assertEqual(self.robot.bateria, 100)

    def test_elRobotDisparaAunObjetivo(self): 
        """ pass """
        self.assertEqual(self.robot.bateria, 10)

        self.robot.dispararObjetivo("soy un objetivo")

        self.assertEqual(self.robot.bateria,9)



if __name__ == '__main__':
    unittest.main()

