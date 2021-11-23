"""
    Ejercicio 3:
        Modelar la clase Robot con las siguientes caracteristicas:
            - Un robot posee una bateria en la cual almacena su energia.
              La carga de la bateria de encuentra en el rango de 0 a 100.
            - Un robot puede:
                # caminar(metros): le consume 1 unidad cada 10 metros.
                # cargarBateria(una_carga): le agrega una determinada cantidad
                  de unidades, pero no puede superar las 100 unidades de la bateria.
                # disparar(un_objetivo): le consume el 10% de la bateria que posea. 

    Realizar los test necesarios que validen 
    el comportamiento.         
"""

class Robot(object):
    """
        Clase robot 

        Métodos:
            -> Batería: Almacena su energía (0 a 100)
            -> Caminar: Consume 1 unidad cada 10 metros
            -> Cargar Batería: No puede exceder las 100 unidades de energía.
            -> Disparar: Consume 10% de la batería.    
    """

    def __init__(self, unidades_bateria:int) -> None:
        self.__bateria = unidades_bateria

    @property
    def bateria(self): return self.__bateria

    def caminar(self, una_distancia: int) -> None:
        """ dada una distancia le consume una unidad de bateria cada 10 mts """
        unidades_bateria = una_distancia / 10
        if self.bateria >= unidades_bateria:
            self.__bateria -= unidades_bateria 
        else:
            raise ValueError("Unidades de bateria insuficiente")


    def cargaBateria(self, unidades_carga) -> None:
        """ Cargando bateria, no puede exceder 100 unidades de energía """
        if unidades_carga + self.bateria <= 100 :
            self.__bateria += unidades_carga
        else:
            self.__bateria = 100    

    def dispararObjetivo(self,  un_objetivo):
        """ pass """ 
        self.__bateria -= self.bateria * 0.1

    
robot = Robot(100)
robot.caminar(10)
print(robot.bateria())
