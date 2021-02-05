import struct 

class CamposVariables:

    def __init__(self, archivo):
        self.archivo = archivo
        self._cant_registros = 0

    #cada len tiene +1 para al ver el archivo se pueda diferenciar los datos
    
    def guardar_provincia(self,nombre, casos_m, casos_f, edad_0_20, edad_20_40, edad_40_60, edad_60_200,
    promedio_infectados):
        formato = "%ds%ds%ds%ds%ds%ds%ds%ds" % (len(nombre)+1,len(str(casos_m))+1, len(str(casos_f))+1, len(str(edad_0_20))+1,
        len(str(edad_20_40))+1, len(str(edad_40_60))+1, len(str(edad_60_200))+1, len(str(promedio_infectados))+1)

        with open(self.archivo, "ab") as datos:
            datos.write(struct.pack(formato, nombre.encode(), casos_m.encode(), casos_f.encode(), edad_0_20.encode(),
            edad_20_40.encode(), edad_40_60.encode(), edad_60_200.encode(), promedio_infectados.encode()))
            self._cant_registros += 1