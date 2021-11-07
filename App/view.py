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


route = 'UFOS//UFOS-utf8-small.csv'
cont = None
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
        total = controller.getOvnisInCity(archive, City)
        print(total)
        print("Altura del arbol: " + str(om.height(archive['DateIndex'])))
        print('Elementos en el arbol: ' + str(om.size(archive['DateIndex'])))

    elif int(inputs[0]) == 4:
        print("\nREQ2-Buscando avistamientos por duración: ")
        wSecMin = input("Ingresar límite inferior de tiempo(segundos): ")
        wSecMax = input("Ingresar límite superior de tiempo(segundos): ")
        maxSight = controller.durationRangeCount(archive, wSecMin,
                                                      wSecMax)
        print(maxSight)
    
    elif int(inputs[0]) == 5:
        print("\nREQ3-Consultar avistamientos por Hora/Minutos del día: ")
        limiteinf = input("Ingresar límite inferior en tiempo Horas/Minutos(HH:MM): ")
        limitesup = input("Ingresar límite superior en tiempo Horas/Minutos(HH:MM): ")
        SightHM = controller.getSightByRangeHM(cont, limiteinf,
                                                      limitesup)
        print(SightHM)
    
    elif int(inputs[0]) == 6:
        print("\nREQ4-Consultar avistamientos en rango de fechas: ")
        minDate = input("Ingresar límite inferior de fechas(AAAA-MM-DD): ")
        maxDate = input("Ingresar límite superior de fechas(AAAA-MM-DD): ")
        SightDates = controller.dateRangeSights(cont, minDate,
                                                      maxDate)
        print(SightDates)
    
    elif int(inputs[0]) == 7:
        print("\nREQ5-Consultar avistamientos en una zona geográfica: ")
        print("\nIngresar rangos de latitud: ")
        limiteinfLat = round(int(input("Ingresar límite inferior de latitud: ")), 2)
        limitesupLat = round(int(input("Ingresar límite superior de latitud: ")), 2)
        
        print("\nIngresar rangos de longitud: ")
        limiteinfLon = round(int(input("Ingresar límite inferior de longitud: ")), 2)
        limitesupLon = round(int(input("Ingresar límite superior de longitud: ")), 2)

        SightZone = controller.getHowSightInZone(cont, limiteinfLat, limitesupLat,
                                                      limiteinfLon, limitesupLon)
        print(SightZone)
    
    elif int(inputs[0]) == 8:
        print("\nREQ6BONO-Visualizar avistamientos en una zona geográfica: ")
        print("\nIngresar rangos de latitud: ")
        limiteinfLat = round(int(input("Ingresar límite inferior de latitud: ")), 2)
        limitesupLat = round(int(input("Ingresar límite superior de latitud: ")), 2)
        
        print("\nIngresar rangos de longitud: ")
        limiteinfLon = round(int(input("Ingresar límite inferior de longitud: ")), 2)
        limitesupLon = round(int(input("Ingresar límite superior de longitud: ")), 2)

        WatchSightZone = controller.getSightInZone(cont, limiteinfLat, limitesupLat,
                                                      limiteinfLon, limitesupLon)
        print(WatchSightZone)

    else:
        sys.exit(0)

sys.exit(0)
