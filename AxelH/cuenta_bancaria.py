""" Definición de la superclase abstracta CuentaBancaria """

from abc import  ABC, abstractmethod

class CuentaBancaria(ABC):
    """ 
    """

    def __init__(self, titular:str, saldo:float) -> None:
        self.__titular = titular
        self.__saldo = saldo

    @property
    def titular(self): return self.__titular

    @property
    def saldo(self): return self.__saldo

    # ---- Método público ---- #

    def depositar(self, un_monto: float) -> None: self.__saldo += un_monto

    # ---- Métodos abstractos ---- #
    @abstractmethod
    def puedeExtraer(self, un_monto: int) ->  bool:
        """ 
        """
        raise NotImplementedError

    @abstractmethod
    def extraer(self, un_monto:int) -> bool:
        """
        """
        raise NotImplementedError
        
           
        