"""
    Ejercicio 2:
        Modelar el objeto fecha en donde tendra:
            - un dia 
            - un mes 
            - un anio 
        
        y debera poder compararse con otra fecha:
            - (==, <, <=, >=, >)
            - esta entre "una_fecha" y "otra_fecha"

        Realizar los test necesarios que validen 
        el comportamiento.  
"""


# class Fecha_ob(object):
#     __Dia = 0
#     __Mes = 0
#     __Anio = 0

#     @property
#     def fechaDia(self): return self.__Dia

#     @fechaDia.setter
#     def fechaDia(self, num_dia): 
#         self.__Dia = num_dia

#     @property
#     def fechaMes(self): return self.__Mes

#     @fechaMes.setter
#     def fechaMes(self, num_mes): 
#         self.__Mes = num_mes

#     @property
#     def fechaAnio(self): return self.__Anio

#     @fechaAnio.setter
#     def fechaAnio(self, num_anio): 
#         self.__Anio = num_anio


class Fecha_obj(object):
    __Fecha = [0, 1, 2]

    @property
    def fechaDia(self): return self.__Fecha


    @fechaDia.Setter
    def setDia(self, num_dia: int):
        self.__Fecha[0]= num_dia
    
    @property
    def fechaMes(self): return self.__Fecha
      
    @fechaMes.setter
    def fechaMes(self, num_mes: int):
        self.__Fecha[1]= num_mes

    @property
    def fechaAnio(self): return self.__Fecha
    
    @fechaAnio.setter
    def fechaAnio(self, num_anio: int):
        self.__Fecha[2]= num_anio

    def configurarFecha(self, una_fecha: list) -> None:
        self.Fecha = una_fecha




if __name__ == "__main__":
    inFecha = Fecha_obj()
    print(inFecha.Fecha)
