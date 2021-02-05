import struct
import os

class CamposFijos():

    def __init__(self, archivo, len_provincia, len_casos_m, len_casos_f, len_etario_0_20, len_etario_20_40,
    len_etario_40_60, len_etario_60_200, len_promedio_infectados):
        self._archivo = archivo
        formato = "%ds%ds%ds%ds%ds%ds%ds%ds" % (len_provincia, len_casos_m, len_casos_f, len_etario_0_20,
         len_etario_20_40,len_etario_40_60,len_etario_60_200, len_promedio_infectados)
        self._formato = formato
        self._len_registro = struct.calcsize(formato)
        try:
            tam_archivo = os.path.getsize(archivo)
            self._cant_registros = tam_archivo / self._len_registro
        except FileNotFoundError:
            self._cant_registros = 0
    
    def guardar_provincia(self, nombre, casos_m, casos_f, edad_0_20, edad_20_40, edad_40_60, edad_60_200,
     promedio_infectados):
        with open(self._archivo, "ab") as datos:
            datos.write(struct.pack(self._formato, nombre.encode(), casos_m.encode(), casos_f.encode(), edad_0_20.encode(),
            edad_20_40.encode(), edad_40_60.encode(), edad_60_200.encode(), promedio_infectados.encode()))
            self._cant_registros += 1

    def __iter__(self):
        return CamposFijosIterator(self)
      
class CamposFijosIterator:
    
    def __init__(self, campos_fijos):
        self.campos_fijos = campos_fijos
        self.index = 0
    def __next__(self):
        if self.index < self.campos_fijos._cant_registros:
            with open(self.campos_fijos._archivo, "rb") as datos:
                posicion = self.index*self.campos_fijos._len_registro
                datos.seek(posicion)
                registro = datos.read(self.campos_fijos._len_registro)
                self.index += 1
                if len(registro) == self.campos_fijos._len_registro:
                    (b_provincia, b_casos_m, b_casos_f, b_edad_0_20, b_edad_20_40, b_edad_40_60, b_edad_60_200,
                    b_promedio) = struct.unpack(self.campos_fijos._formato, registro)

                    provincia, casos_m, casos_f, edad_0_20, edad_20_40, edad_40_60, edad_60_200,promedio = (
                    b_provincia.decode(), b_casos_m.decode(), b_casos_f.decode(), b_edad_0_20.decode(),
                    b_edad_20_40.decode(), b_edad_40_60.decode(), b_edad_60_200.decode(), b_promedio.decode())

                else:
                    provincia, casos_m, casos_f, edad_0_20, edad_20_40, edad_40_60, edad_60_200, promedio = "","","","","","","",""
        else:
            raise StopIteration
        return provincia, casos_m, casos_f, edad_0_20, edad_20_40, edad_40_60, edad_60_200, promedio
