"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
import operator
from tabulate import tabulate
from App import model #SE DEBE BORRAR, SOLO ES PARA EL EJEMPLO #TODO
from App import controller
assert config

from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import map as m



"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________


route = 'UFOS//UFOS-utf8-large.csv'
cont = None


def getOvnisInCity(archive, City):

    answer = controller.getOvnisInCity(archive, City)

    data1 = answer[0]
    data2 = answer[1]
    numCities = answer[2]
    numSight = answer[3]
    wCiudad = answer[4]

    orderedData1 = dict(sorted(data1.items(), key=operator.itemgetter(1), reverse=True))
    dataKeys1 = list(orderedData1.keys())
    dataValues1 = list(orderedData1.values())
    finalDataList1 = [
        [dataKeys1[0], dataValues1[0]], 
        [dataKeys1[1], dataValues1[1]],
        [dataKeys1[2], dataValues1[2]],
        [dataKeys1[3], dataValues1[3]],
        [dataKeys1[4], dataValues1[4]]]

    orderedData2 = sorted(data2, key=lambda sight: sight["datetime"])
    dataKeys2 = list(orderedData2.keys())
    headLiners2 = [dataKeys2[0], dataKeys2[1]. dataKeys2[2], dataKeys2[3], dataKeys2[4], dataKeys2[5]]

    sight1 = orderedData2[0].values()
    sight2 = orderedData2[1].values()
    sight3 = orderedData2[2].values()
    sightL3 = orderedData2[-3].values()
    sightL2 = orderedData2[-2].values()
    sightL1 = orderedData2[-1].values()

    finalDataList2 = [
        [sight1[0], sight1[1], sight1[2], sight1[3], sight1[4], sight1[5]], 
        [sight2[0], sight2[1], sight2[2], sight2[3], sight2[4], sight2[5]],
        [sight3[0], sight3[1], sight3[2], sight3[3], sight3[4], sight3[5]],
        [sightL3[0], sightL3[1], sightL3[2], sightL3[3], sightL3[4], sightL3[5]],
        [sightL2[0], sightL2[1], sightL2[2], sightL2[3], sightL2[4], sightL2[5]],
        [sightL1[0], sightL1[1], sightL1[2], sightL1[3], sightL1[4], sightL1[5]]]

    print("There are " + str(numCities) + " differenet cities with UFO sightings...")
    print("The TOP 5 cities with most UFO sighting are: ")
    print(tabulate(finalDataList1, headers = ["city", "count"], tablefmt = "pretty") + "\n")

    print("There are " + str(numSight) + " sightings at the: " + wCiudad + " city.")
    print("The first 3 and last 3 UFO sightinfgs in the city are: ")
    print(tabulate(finalDataList2, headers = headLiners2, tablefmt = "pretty") + "\n")

    print('Avistamientos cargados: ' + str(lt.size(archive["VideoList"])))
    print('Altura del arbol: ' + str(om.height(archive['DateIndex'])))
    print('Elementos en el arbol: ' + str(om.size(archive['DateIndex'])))
    print('Menor Llave: ' + str(om.minKey(archive['DateIndex'])))
    print('Mayor Llave: ' + str(om.maxKey(archive['DateIndex'])))

def durationRangeCount(archive, wSecMin, wSecMax):
    answer = controller.durationRangeCount(archive, wSecMin, wSecMax)
    data1 = answer[0]
    data2 = answer[1]
    count = answer[2]

    orderedData1 = dict(sorted(data1.items(), key=operator.itemgetter(0), reverse=True))
    dataKeys1 = list(orderedData1.keys())
    dataValues1 = list(orderedData1.values())
    finalDataList1 = [
        [dataKeys1[0], dataValues1[0]], 
        [dataKeys1[1], dataValues1[1]],
        [dataKeys1[2], dataValues1[2]],
        [dataKeys1[3], dataValues1[3]],
        [dataKeys1[4], dataValues1[4]]]

    orderedData2 = sorted(data2, key=lambda sight: sight["datetime"])
    dataKeys2 = list(orderedData2.keys())
    headLiners2 = [dataKeys2[0], dataKeys2[1]. dataKeys2[2], dataKeys2[3], dataKeys2[4], dataKeys2[5]]

    sight1 = orderedData2[0].values()
    sight2 = orderedData2[1].values()
    sight3 = orderedData2[2].values()
    sightL3 = orderedData2[-3].values()
    sightL2 = orderedData2[-2].values()
    sightL1 = orderedData2[-1].values()

    finalDataList2 = [
        [sight1[0], sight1[1], sight1[2], sight1[3], sight1[4], sight1[5]], 
        [sight2[0], sight2[1], sight2[2], sight2[3], sight2[4], sight2[5]],
        [sight3[0], sight3[1], sight3[2], sight3[3], sight3[4], sight3[5]],
        [sightL3[0], sightL3[1], sightL3[2], sightL3[3], sightL3[4], sightL3[5]],
        [sightL2[0], sightL2[1], sightL2[2], sightL2[3], sightL2[4], sightL2[5]],
        [sightL1[0], sightL1[1], sightL1[2], sightL1[3], sightL1[4], sightL1[5]]]

    print("There are " + str(len(data1)) + " different UFO sightings durations...")
    print("The TOP 5 durations with longest UFO sightings are: ")
    print(tabulate(finalDataList1, headers = ["duration (seconds)", "count"], tablefmt = "pretty") + "\n")

    print("There are " + str(count) + " sightings between: " + str(wSecMin) + " and " + str(wSecMax) + "duration.")
    print("The first 3 and last 3 UFO sightings in the duration time are:")
    print(tabulate(finalDataList2, headers = headLiners2, tablefmt = "pretty") + "\n")

def getSightByRangeHM(archive, limiteinf, limitesup):
    answer = controller.getSightByRangeHM(archive, limiteinf, limitesup)
    data1 = answer[0]
    data2 = answer[1]
    count = answer[2]

    orderedData1 = dict(sorted(data1.items(), key=operator.itemgetter(0), reverse=True))
    dataKeys1 = list(orderedData1.keys())
    dataValues1 = list(orderedData1.values())
    finalDataList1 = [
        [dataKeys1[0], dataValues1[0]], 
        [dataKeys1[1], dataValues1[1]],
        [dataKeys1[2], dataValues1[2]],
        [dataKeys1[3], dataValues1[3]],
        [dataKeys1[4], dataValues1[4]]]

    orderedData2 = sorted(data2, key=lambda sight: sight["datetime"])
    dataKeys2 = list(orderedData2.keys())
    headLiners2 = [dataKeys2[0], dataKeys2[1]. dataKeys2[2], dataKeys2[3], dataKeys2[4], dataKeys2[5]]

    sight1 = orderedData2[0].values()
    sight2 = orderedData2[1].values()
    sight3 = orderedData2[2].values()
    sightL3 = orderedData2[-3].values()
    sightL2 = orderedData2[-2].values()
    sightL1 = orderedData2[-1].values()

    finalDataList2 = [
        [sight1[0], sight1[1], sight1[2], sight1[3], sight1[4], sight1[5]], 
        [sight2[0], sight2[1], sight2[2], sight2[3], sight2[4], sight2[5]],
        [sight3[0], sight3[1], sight3[2], sight3[3], sight3[4], sight3[5]],
        [sightL3[0], sightL3[1], sightL3[2], sightL3[3], sightL3[4], sightL3[5]],
        [sightL2[0], sightL2[1], sightL2[2], sightL2[3], sightL2[4], sightL2[5]],
        [sightL1[0], sightL1[1], sightL1[2], sightL1[3], sightL1[4], sightL1[5]]]

    print("There are " + str(len(data1)) + " different UFO times [hh-mm-ss]...")
    print("The 5 latest times for UFO sightings are:")
    print(tabulate(finalDataList1, headers = ["time", "count"], tablefmt = "pretty") + "\n")

    print("There are " + str(count) + " sightings between: " + str(limiteinf) + " and " + str(limitesup))
    print("The first 3 and last 3 UFO sightings in this time are: ")
    print(tabulate(finalDataList2, headers = headLiners2, tablefmt = "pretty") + "\n")
    
def dateRangeSights(cont, minDate,maxDate):
    answer = controller.dateRangeSights(cont, minDate, maxDate)
    data1 = answer[0]
    data2 = answer[1]
    count = answer[2]
    count2 = answer[3]

    orderedData1 = dict(sorted(data1.items(), key=operator.itemgetter(0), reverse=False))
    dataKeys1 = list(orderedData1.keys())
    dataValues1 = list(orderedData1.values())
    finalDataList1 = [
        [dataKeys1[0], dataValues1[0]], 
        [dataKeys1[1], dataValues1[1]],
        [dataKeys1[2], dataValues1[2]],
        [dataKeys1[3], dataValues1[3]],
        [dataKeys1[4], dataValues1[4]]]

    orderedData2 = sorted(data2, key=lambda sight: sight["datetime"])
    dataKeys2 = list(orderedData2.keys())
    headLiners2 = [dataKeys2[0], dataKeys2[1]. dataKeys2[2], dataKeys2[3], dataKeys2[4], dataKeys2[5]]

    sight1 = orderedData2[0].values()
    sight2 = orderedData2[1].values()
    sight3 = orderedData2[2].values()
    sightL3 = orderedData2[-3].values()
    sightL2 = orderedData2[-2].values()
    sightL1 = orderedData2[-1].values()

    finalDataList2 = [
        [sight1[0], sight1[1], sight1[2], sight1[3], sight1[4], sight1[5]], 
        [sight2[0], sight2[1], sight2[2], sight2[3], sight2[4], sight2[5]],
        [sight3[0], sight3[1], sight3[2], sight3[3], sight3[4], sight3[5]],
        [sightL3[0], sightL3[1], sightL3[2], sightL3[3], sightL3[4], sightL3[5]],
        [sightL2[0], sightL2[1], sightL2[2], sightL2[3], sightL2[4], sightL2[5]],
        [sightL1[0], sightL1[1], sightL1[2], sightL1[3], sightL1[4], sightL1[5]]]

    print("There are " + str(count) + " different UFO sightings dates [YYYY-MM-DD]...")
    print("The oldest 5 dates for UFO sightings are:")
    print(tabulate(finalDataList1, headers = ["date", "count"], tablefmt = "pretty") + "\n")

    print("There are " + str(count2) + " sightings between: " + str(minDate) + " and " + str(maxDate))
    print("The first 3 and last 3 UFO sightings in this time are: ")
    print(tabulate(finalDataList2, headers = headLiners2, tablefmt = "pretty") + "\n")
    
def getSightInZone(cont, limiteinfLat, limitesupLat, limiteinfLon, limitesupLon):
    answer = controller.getSightInZone(cont, limiteinfLat, limitesupLat, limiteinfLon, limitesupLon)
    data = answer[0]
    numCat = answer[1]

    orderedData2 = sorted(data, key=lambda sight: sight["datetime"])
    dataKeys2 = list(orderedData2.keys())
    headLiners2 = [dataKeys2[0], dataKeys2[1]. dataKeys2[2], dataKeys2[3], dataKeys2[4], dataKeys2[5]]

    sight1 = orderedData2[0].values()
    sight2 = orderedData2[1].values()
    sight3 = orderedData2[2].values()
    sight4 = orderedData2[3].values()
    sight5 = orderedData2[4].values()
    sightL5 = orderedData2[-5].values()
    sightL4 = orderedData2[-4].values()
    sightL3 = orderedData2[-3].values()
    sightL2 = orderedData2[-2].values()
    sightL1 = orderedData2[-1].values()

    finalDataList2 = [
        [sight1[0], sight1[1], sight1[2], sight1[3], sight1[4], sight1[5]], 
        [sight2[0], sight2[1], sight2[2], sight2[3], sight2[4], sight2[5]],
        [sight3[0], sight3[1], sight3[2], sight3[3], sight3[4], sight3[5]],
        [sight4[0], sight4[1], sight4[2], sight4[3], sight4[4], sight4[5]],
        [sight5[0], sight5[1], sight5[2], sight5[3], sight5[4], sight5[5]],
        [sightL5[0], sightL5[1], sightL5[2], sightL5[3], sightL5[4], sightL5[5]],       
        [sightL4[0], sightL4[1], sightL4[2], sightL4[3], sightL4[4], sightL4[5]],
        [sightL3[0], sightL3[1], sightL3[2], sightL3[3], sightL3[4], sightL3[5]],
        [sightL2[0], sightL2[1], sightL2[2], sightL2[3], sightL2[4], sightL2[5]],
        [sightL1[0], sightL1[1], sightL1[2], sightL1[3], sightL1[4], sightL1[5]]]

    print("There are " + str(numCat) + " different UFO sightings in the current area")
    print("The first 5 and last 5 UFO sightings in this time are: ")
    print(tabulate(finalDataList2, headers = headLiners2, tablefmt = "pretty") + "\n")



# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    print("\n")
    print("*******************************************")
    print("Bienvenido")
    print("1- Inicializar Analizador")
    print("2- Cargar información de OVNIS")
    print("3- REQ1-Consultar OVNIS en una ciudad /--Ciudad--/")
    print("4- REQ2-Consultar avistamientos por duración /--Limite inferior y Límite superior--/")
    print("5- REQ3-Consultar avistamientos por Hora/Minutos del día /--Limite inferior HH:MM y Límite superior HH:MM--/")
    print("6- REQ4-Consultar avistamientos en rango de fechas /--Limite inferior AAAA-MM-DD y Límite superior AAAA-MM-DD--/")
    print("7- REQ5-Consultar avistamientos en una zona geográfica /--Long(Limite máx y min) Lat(Límite máx y min)--/")
    print("8- REQ6BONO-Visualizar avistamientos en una zona geográfica /--Long(Limite máx y min) Lat(Límite máx y min)--/")
    print("9- Example(folium)")
    print("0- Salir")
    print("*******************************************")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n>')

    if int(inputs[0]) == 1:
        print("\nInicializando....")
        # cont es el controlador que se usará de acá en adelante
        archive = controller.init()

    elif int(inputs[0]) == 2:
        print("\nCargando información de avistamientos....")
        controller.loadData(archive, route)    

    elif int(inputs[0]) == 3:
        print("\nREQ1-Buscando OVNIS en una ciudad: ")
        City = input("Ingrese la ciudad: ")
        total = getOvnisInCity(archive, City)
        print(total)
        print("Altura del arbol: " + str(om.height(archive['DateIndex'])))
        print('Elementos en el arbol: ' + str(om.size(archive['DateIndex'])))

    elif int(inputs[0]) == 4:
        print("\nREQ2-Buscando avistamientos por duración: ")
        wSecMin = input("Ingresar límite inferior de tiempo(segundos): ")
        wSecMax = input("Ingresar límite superior de tiempo(segundos): ")
        maxSight = durationRangeCount(archive, wSecMin, wSecMax)
        print(maxSight)
    
    elif int(inputs[0]) == 5:
        print("\nREQ3-Consultar avistamientos por Hora/Minutos del día: ")
        limiteinf = input("Ingresar límite inferior en tiempo Horas/Minutos(HH:MM): ")
        limitesup = input("Ingresar límite superior en tiempo Horas/Minutos(HH:MM): ")
        SightHM = getSightByRangeHM(cont, limiteinf, limitesup)
        print(SightHM)
    
    elif int(inputs[0]) == 6:
        print("\nREQ4-Consultar avistamientos en rango de fechas: ")
        minDate = input("Ingresar límite inferior de fechas(AAAA-MM-DD): ")
        maxDate = input("Ingresar límite superior de fechas(AAAA-MM-DD): ")
        SightDates = dateRangeSights(cont, minDate, maxDate)
        print(SightDates)
    
    elif int(inputs[0]) == 7:
        print("\nREQ5-Consultar avistamientos en una zona geográfica: ")
        print("\nIngresar rangos de latitud: ")
        limiteinfLat = round(int(input("Ingresar límite inferior de latitud: ")), 2)
        limitesupLat = round(int(input("Ingresar límite superior de latitud: ")), 2)

        
        print("\nIngresar rangos de longitud: ")
        limiteinfLon = round(int(input("Ingresar límite inferior de longitud: ")), 2)
        limitesupLon = round(int(input("Ingresar límite superior de longitud: ")), 2)

        SightZone = getSightInZone(cont, limiteinfLat, limitesupLat, limiteinfLon, limitesupLon)
        print(SightZone)
    
    elif int(inputs[0]) == 8:
        print("\nREQ6BONO-Visualizar avistamientos en una zona geográfica: ")
        print("\nIngresar rangos de latitud: ")
        limiteinfLat = round(int(input("Ingresar límite inferior de latitud: ")), 2)
        limitesupLat = round(int(input("Ingresar límite superior de latitud: ")), 2)
        
        print("\nIngresar rangos de longitud: ")
        limiteinfLon = round(int(input("Ingresar límite inferior de longitud: ")), 2)
        limitesupLon = round(int(input("Ingresar límite superior de longitud: ")), 2)

        WatchSightZone = getSightInZone(cont, limiteinfLat, limitesupLat, limiteinfLon, limitesupLon)
        print(WatchSightZone)

    elif int(inputs[0]) == 9:
        print("Prueba de ejemplo")
        ex = controller.example()
        print(ex)
    else:
        sys.exit(0)

sys.exit(0)
