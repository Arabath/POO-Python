from excepciones import ImposibleRealizarExtraccion

class CuentaCorriente(object):

    def __init__(self, titular:str, saldo:float, descubiertoMaximo:float) -> None:
        self.__titular = titular
        self.__saldo = saldo
        self.__descubiertoMaximo = descubiertoMaximo

    @property
    def titular(self): return self.__titular

    @property
    def saldo(self): return self.__saldo

    @property
    def descubiertoMaximo(self): return self.__descubiertoMaximo

    # ---- Métodos de la clase ---- #
    def depositar(self, un_monto: float) -> None: self.__saldo += un_monto

    def puedeExtraer(self, un_monto: float) -> bool:
        """ Devuelve True si se puede realizar una extracción"""
        return un_monto <= self.saldo + self.descubiertoMaximo

    def extraer(self, un_monto: float):
        """ Extrae un monto de la cuenta sino arroja la excepción: 
            -> ImposibleRealizarExtraccion('Imposible realizar la extracción.')
        """
        if self.puedeExtraer(un_monto):
            self.__saldo -= un_monto
        else:
            raise ImposibleRealizarExtraccion('Imposible realizar la extracción.')

if __name__ == "__main__":
    pass

cuenta = CuentaCorriente('Axel', 1200, 2)
cuenta.depositar(1200)
cuenta.extraer(1500)


print(cuenta.saldo)
