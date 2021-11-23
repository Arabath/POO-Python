
"""
    Ejercicio 1:
        Modelar el objeto caja de ahorro:
            - un titular
            - un saldo
        
        y debera poder:
            - depositar un monto
            - extraer un monto
            - Puede extraer un monto?
            - en el caso de querer extraer un monto superior 
              al monto disponible arrojara una 
              excepcion ValueError("Imposible realizar extracción.")

        Realizar los test necesarios que validen 
        el comportamiento.  
"""

class CajaDeAhorro(object):
 #   def __init__(self, titular, saldo) -> None:
    __titular = ""
    __saldo = 0

    @property
    def titular(self): return self.__titular

    @titular.setter
    def titular(self, name_titular):
        self.__titular = name_titular
    
    @property
    def saldo(self): return self.__saldo

    @saldo.setter
    def saldo(self, cant_saldo):
        self.__saldo = cant_saldo

    def depositarMonto(self, un_monto: int ) -> None:
        """ Agrega un monto al saldo existente """
        self.saldo += un_monto

    def extraerUnMonto(self, un_monto: int ) -> None:
        """ Extrae un monto a un saldo existente """
        if self.puedeExtraer(un_monto):
            self.saldo -= un_monto
        else:
            raise ValueError("Imposible realizar extraccion.")
    
    def puedeExtraer(self, un_monto: int) -> bool:
        """ Responde True si puede realizar la extracción """
        return un_monto <= self.saldo  #mensaje de comparación
        
    
if __name__ == "__main__":
    cuenta = CajaDeAhorro()
    
    cuenta.depositarMonto(1000)
    cuenta.extraerUnMonto(50)
    print(cuenta.saldo)










    # caja.depositarMonto(5000)
    # print(caja.saldo)
    # caja.extraerUnMonto(2500)
    # print(caja.saldo)
    # caja.puedeExtraer(2500)
    # print(caja.saldo)
    # caja.titular('Mario')
    # print(caja.titular)



    # caja = CajaDeAhorro()
    # print(caja.saldo)

    # caja.depositarMonto(100)
    # # print(caja.saldo)

    # # caja.depositarMonto(100)
    # # print(caja.saldo)
    # try:
    #     caja.extraerUnMonto(200)
    # except ValueError as error:
    #     print(error)
        
    # # respuesta = caja.puedeExtraer(100)
    # # print(respuesta)

    # print(caja.saldo)


       
