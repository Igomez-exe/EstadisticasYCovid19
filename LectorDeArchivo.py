import csv 
import operator 
from CamposFijos import CamposFijos
from CamposVariables import CamposVariables

class LeerArchivo():

    def __init__(self):
        self.estadisticas = {}
        self.promedio_de_infectado = {}
        self.tablas_campos_fijos = CamposFijos("campos_fijos.v1", 25,10 ,10, 10, 10, 10, 10, 10)
        self.tablas_campos_variables = CamposVariables("campos_variables.v1")

    def recorrer_archivo(self):
        """

        Acá tendría que ir el csv que se obtiene del link, o mismo, el que se encuentra en esta carpeta

        """
        with open("Covid19Casos.csv") as fd:
            reader = csv.reader(fd)
            for linea in reader:
                self.utilizar_valores_correctos(linea)
                
        self.promediar(self.promedio_de_infectado, self.estadisticas)
        self.ordenar_provincias()
        self.guardar_en_campos_longitud_fija()
        self.guardar_en_campos_longitud_variable()

    def utilizar_valores_correctos(self,lista):
        lista_con_valores_corretos = lista
        lista_correcta = lista_con_valores_corretos[1:3] + lista_con_valores_corretos[5:6] + lista_con_valores_corretos[19:20]
        self.guardar_datos_en_diccionario(lista_correcta)
    
    #el orden de la lista adentro del diccionario es el siguiente, primero casos masculinos, luego
    #casos femeninos, luego el rango etario(primero de 0-20, 20-40, 40-60 y por ultimo 60+), luego
    #promedio de edad de los infectados.

    def guardar_datos_en_diccionario(self, lista_con_valores):
        if lista_con_valores[2] not in self.estadisticas and lista_con_valores[3] != 'Caso Descartado':
            if lista_con_valores[0] == 'M':
                self.estadisticas[lista_con_valores[2]] = [1,0,0,0,0,0,0]
                self.acomodar_etario(lista_con_valores)
                self.guardar_datos_para_promediar(lista_con_valores)
                
                
            elif lista_con_valores[0] == 'F':
                self.estadisticas[lista_con_valores[2]] = [0,1,0,0,0,0,0]
                self.acomodar_etario(lista_con_valores)
                self.guardar_datos_para_promediar(lista_con_valores)
                

        elif lista_con_valores[2] in self.estadisticas :
            if lista_con_valores[0] == 'M':
                self.estadisticas[lista_con_valores[2]][0] += 1
                self.acomodar_etario(lista_con_valores)
                self.guardar_datos_para_promediar(lista_con_valores)
            
            elif lista_con_valores[0] == 'F':
                self.estadisticas[lista_con_valores[2]][1] += 1
                self.acomodar_etario(lista_con_valores) 
                self.guardar_datos_para_promediar(lista_con_valores)
                   

    #al leer el archivo me di cuenta que algunas personas no tenian la edad en entero sino que 
    #aparecia '', por lo que se sumarian al rango etario de 0 a 20

    def acomodar_etario(self,lista_con_valores):

        if lista_con_valores[1] == '':
            self.estadisticas[lista_con_valores[2]][2] += 1
        elif int(lista_con_valores[1]) in range(0,21):
            self.estadisticas[lista_con_valores[2]][2] += 1
        elif int(lista_con_valores[1]) in range(20,41):
            self.estadisticas[lista_con_valores[2]][3] += 1
        elif int(lista_con_valores[1]) in range(40,61):
            self.estadisticas[lista_con_valores[2]][4] += 1
        elif int(lista_con_valores[1]) in range(60,200):
            self.estadisticas[lista_con_valores[2]][5] += 1
    
    def guardar_datos_para_promediar(self,lista):

        if lista[2] not in self.promedio_de_infectado and lista[1] != '':
            self.promedio_de_infectado[lista[2]] = [lista[1],1]
        elif lista[2] in self.promedio_de_infectado and lista[1] != '':
            self.promedio_de_infectado[lista[2]] = [int(self.promedio_de_infectado[lista[2]][0]) + int(lista[1]),
             int(self.promedio_de_infectado[lista[2]][1]) + 1 ]

    def promediar(self, diccionario_uno, diccionario_dos):
        for key in diccionario_uno:
            valor = int(diccionario_uno[key][0]) / int(diccionario_uno[key][1])
            diccionario_dos[key][6] = int(valor)
    
    def guardar_en_campos_longitud_fija(self):
        for x in self.estadisticas:
            self.tablas_campos_fijos.guardar_provincia(x, str(self.estadisticas[x][0]),str(self.estadisticas[x][1]),
            str(self.estadisticas[x][2]),str(self.estadisticas[x][3]),str(self.estadisticas[x][4]),
            str(self.estadisticas[x][5]),str(self.estadisticas[x][6]))
    
    def guardar_en_campos_longitud_variable(self):
        for x in self.estadisticas:
            self.tablas_campos_variables.guardar_provincia(x,str(self.estadisticas[x][0]),str(self.estadisticas[x][1]),
            str(self.estadisticas[x][2]),str(self.estadisticas[x][3]),str(self.estadisticas[x][4]),
            str(self.estadisticas[x][5]),str(self.estadisticas[x][6]))

    def ordenar_provincias(self):
        self.estadisticas = dict(sorted(self.estadisticas.items(), key = lambda x:x[1][0]+x[1][1], reverse= True))


if __name__ == "__main__":
    prueba  = LeerArchivo()
    prueba.recorrer_archivo()