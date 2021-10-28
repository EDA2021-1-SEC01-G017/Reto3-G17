﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
from tabulate import tabulate
import datetime
import operator

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos 

def newArchive():

    archive = {}

    archive["VideoList"] = lt.newList(datastructure = "SINGLED_LINKED")
    archive["DateIndex"] = om.newMap(omaptype = "RBT", comparefunction = compareDates)
    archive["City"] = mp.newMap(maptype= "PROBING", loadfactor = 0.5) 

    return archive

# Funciones para agregar informacion al catalogo

def addOvni(archive, video):

    lt.addLast(archive["VideoList"], video)


    #Atajo por datetime
    timeInfo = datetime.datetime.strptime(video["datetime"], '%Y-%m-%d %H:%M:%S')

    if om.contains(archive["DateIndex"], timeInfo) == False:
        initList1 = lt.newList(datastructure = "SINGLE_LINKED")
        lt.addLast(initList1, video)
        om.put(archive["DateIndex"], timeInfo, initList1)
    
    else:
        path1 = om.get(archive["DateIndex"], timeInfo)
        intList2 = me.getValue(path1)
        lt.addLast(intList2, video)

    #Atajo por ciudad
    if mp.contains(archive["City"], video["city"]) == False:
        intList3 = lt.newList(datastructure = "SINGLE_LINKED")
        lt.addLast(intList3, video)
        mp.put(archive["City"], video["city"], intList3)

    else:
        path2 = mp.get(archive["City"], video["city"])
        intList4 = me.getValue(path2)
        lt.addLast(intList4, video)

# Funciones para creacion de datos

# Funciones de consulta

def getOvnisInCity(archive, wCiudad):
    data1 = {}
    data2 = []
    
    #Diccionario de las ciudades con sus respectivas cantidades de avistamientos
    numCities = mp.size(archive["City"])

    ciudades = mp.keySet(archive["City"])     
    for ciudad in lt.iterator(ciudades):
        path1 = mp.get(archive["City"], ciudad)
        sightList1 = me.getValue(path1)
        data1[ciudad] = lt.size(sightList1)

    #Lista de todos los avistamientos de la ciudad seleccionada
    path2 = mp.get(archive["City"], wCiudad)
    sightList2 = me.getValue(path2)
    numSight = lt.size(sightList2)
 
    for sight in lt.iterator(sightList2):
        data2.append(sight)

    #Formatos de impresion
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

def a():        
    pass



# Funciones utilizadas para comparar elementos dentro de una list

def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1


# Funciones de ordenamiento

