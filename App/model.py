"""
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
import folium   

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos 

def newArchive():

    archive = {}

    archive["VideoList"] = lt.newList(datastructure = "SINGLED_LINKED")
    archive["DateIndex"] = om.newMap(omaptype = "BST", comparefunction = compareDates)
    archive["Date"] = om.newMap(omaptype ="BST", comparefunction = compareDates)
    archive["City"] = mp.newMap(maptype = "PROBING", loadfactor = 0.5) 
    archive["h/m"] = om.newMap(omaptype ="BST")
    archive["DurSec"] = om.newMap(omaptype ="BST")
    archive["GeoSector"] = mp.newMap(maptype = "PROBING", loadfactor = 0.5)
    createGeoSect(archive)
    archive["GeoList"] = om.newMap(omaptype = "BST")
    for cuadrante in range (1,37):
        intList = lt.newList()
        om.put(archive["GeoList"], cuadrante, intList)

    return archive

# Funciones para agregar informacion al catalogo

def addOvni(archive, video):

    lt.addLast(archive["VideoList"], video)


    #Atajo para datetimeIn
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

    #Atajo para hora/min
    x = video["datetime"]
    hour = x[-8:]
    if om.contains(archive["h/m"], hour) == False:
        intlist11 = lt.newList(datastructure="SINGLE_LINKED")
        lt.addLast(intlist11, video)
        om.put(archive["h/m"], hour, intlist11)
    
    else:
        path11 = om.get(archive["h/m"], hour)
        intlist12 = me.getValue(path11)
        lt.addLast(intlist12, video)

    #Atajo para duracion
    if om.contains(archive["DurSec"], float(video["duration (seconds)"])) == False:
        initList5 = lt.newList(datastructure = "SINGLE_LINKED")
        lt.addLast(initList5, video)
        om.put(archive["DurSec"], float(video["duration (seconds)"]), initList5)
    
    else:
        path3 = om.get(archive["DurSec"], float(video["duration (seconds)"]))
        initList6 = me.getValue(path3)
        lt.addLast(initList6, video)

    #Atajo para fecha
    indDate = video["datetime"][:10]
    if om.contains(archive["Date"], indDate) == False:
        initList7 = lt.newList(datastructure = "SINGLE_LINKED")
        lt.addLast(initList7, video)
        om.put(archive["Date"], indDate, initList7)

    else:
        path4 = om.get(archive["Date"], indDate)
        initList8 = me.getValue(path4)
        lt.addLast(initList8, video)

    #Atajo a GeoList

    for sector in range (1, 37):
        path5 = mp.get(archive["GeoSector"], sector)
        intlist9 = me.getValue(path5)
        lonMin = lt.getElement(intlist9, 0)
        lonMax = lt.getElement(intlist9, 1)
        latMin = lt.getElement(intlist9, 2)
        latMax = lt.getElement(intlist9, 3)
        
        lonAct = float(video["longitude"])
        latAct = float(video["latitude"])

        if (lonAct >= lonMin) and (lonAct < lonMax):
            if (latAct >= latMin) and (latAct < latMax):
                path6 = om.get(archive["GeoList"], sector)
                intlist10 = me.getValue(path6)
                lt.addLast(intlist10, video)

# Funciones para creacion de datos

# Funciones de consulta
#---#1
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

    answer = (data1, data2, numCities, numSight, wCiudad)

    return answer

#---#2
def durationRangeCount(archive, wSecMin, wSecMax):   

    wTimeMin = float(wSecMin)
    wTimeMax = float(wSecMax)
    count = 0
    

    data1 = {}
    data2 = []

    durations = om.keySet(archive["DurSec"])   
    numberSec = lt.size(durations)

    for duration in lt.iterator(durations):

        path0 = om.get(archive["DurSec"], duration)
        intList0 = me.getValue(path0)
        listsize = lt.size(intList0)

        data1["duration"] = listsize
        
        if (duration >= wTimeMin) and (duration <= wTimeMax):
            count += 1
            path1 = om.get(archive["DurSec"], duration)
            vidList = me.getValue(path1)

            for video in lt.iterator(vidList):
                data2.append(video)

    answer = (data1, data2, count, numberSec)

    return answer
            

#---#3
def getSightByRangeHM(archive, limiteinf, limitesup):
    
    wTimeMax = int(limitesup)
    wTimeMin = int(limiteinf)
    maxDur = 0
    count = 0
    data1 = {}
    data2 = []
    datetime = archive["h/m"]
    durations = om.keyset(datetime)
    for duration in lt.iterator(durations):
        if (duration >= wTimeMin) and (duration <= wTimeMax):
            path1 = om.get(datetime, duration)
            vidList = me.getValue(path1)
            for video in lt.iterator(vidList):
                count += 1
                data2.append(video)
        
        path0 = mp.get(datetime, duration)
        intList0 = me.getValue(path0)
        hourSize = lt.size(intList0)
        data1[duration] = hourSize
            

    answer = (data1, data2, count)

    
    return answer

"""
Copia del 5 pero con añadido de "folium"
"""

def example():
    exampleList = [{"#":1, "location":[45.5244, -122.6699]},{"#":2, "location":[45.5244, -122.6699]},{"#":3, "location":[45.5244, -122.6699]}
    ,{"#":4, "location":[45.5244, -122.6699]},{"#":5, "location":[45.5244, -122.6699]},{"#":16, "location":[45.5244, -122.6699]}
    ,{"#":17, "location":[45.5244, -122.6699]},{"#":18, "location":[45.5244, -122.6699]},{"#":19, "location":[45.5244, -122.6699]},{"#":20, "location":[45.5244, -122.6699]}]
   
    lat = int(exampleList[0]["location"][0])
    lon = int(exampleList[0]["location"][1])
    print(lat, lon)
    i = 0
    size = int(lt.size(exampleList))
    while i < size:
        lat = int(exampleList[i]["location"][0])
        lon = int(exampleList[i]["location"][1])
        place = [lat, lon]
        m = folium.Map(location=place, tiles="Stamen Toner", zoom_start=13)
        folium.Circle(
            radius=100,
            location=place,
            popup="The Sight",
            color="#3186cc",
            fill=True,
            fill_color="#3186cc",
        ).add_to(m)
        print("Mapa número " + str(exampleList[i]["#"]) + "con ubicación " + str(place))
        print(m)
        i ++1

#---#4
def dateRangeSights(archive, minDate, maxDate):

    count2 = 0
    data1 = {}
    data2 = []

    dates = om.keySet(archive["Date"])
    for date in lt.iterator(dates):
        
        if (date >= minDate) and (date <= maxDate):
            
            path1 = om.get(archive["Date"], date)
            vidList = me.getValue(path1)

            for video in lt.iterator(vidList):
                data2.append(video)
                count2 += 1

        pair = om.get(archive["Date"], date)
        intList0 = me.getValue(pair)
        numVid = lt.size(intList0)

        data1[date] = numVid
    
    count = len(data1)

    answer = (data1, data2, count, count2)

    return answer

#---#5
def getSightInZone(archive, minLon, maxLon, minLat, maxLat):
    
    data = []
    typelist = []

    left = []
    right = []
    down = []
    up = []

    for sector1 in range (1, 37):
        path1 = mp.get(archive["GeoSector"], sector1)
        intlist1 = me.getValue(path1)
        lonMin = lt.getElement(intlist1, 0)
        
        if minLon >= lonMin:
            left.append(sector1)
    
    for sector2 in left:
        path2 = mp.get(archive["GeoSector"], sector2)
        intlist2 = me.getValue(path2)
        lonMax = lt.getElement(intlist2, 1)
        
        if maxLon < lonMax:
            right.append(sector2)
    
    for sector3 in right:
        path3 = mp.get(archive["GeoSector"], sector3)
        intlist3 = me.getValue(path3)
        latMin = lt.getElement(intlist3, 2)

        if minLat >= latMin:
            down.append(sector3)
    
    for sector4 in down:
        path4 = mp.get(archive["GeoSector"], sector4)
        intlist4 = me.getValue(path4)
        latMax = lt.getElement(intlist4, 3)

        if maxLat < latMax:
            up.append(sector4)
    
    for fsector in up:
        fpath = om.get(archive["GeoList"], fsector)
        fintList = me.getValue(fpath)
        for video in lt.iterator(fintList):
            if (video["longitude"] >= minLon) and (video["longitude"] <= maxLon):
                if (video["latitude"] >= minLat) and (video["latitude"] <= maxLat):
                    data.append(video)

    numSight = len(data)
    answer = (data, numSight)

    return answer


# Funciones utilizadas para comparar elementos dentro de una list
def createGeoSect (archive):
    indexlist = ["11", "12", "13", "14", "15", "16", 
                "21", "22", "23", "24", "25", "26",
                "31", "32", "33", "34", "35", "36",
                "41", "42", "43", "44", "45", "46",
                "51", "52", "53", "54", "55", "56",
                "61", "62", "63", "64", "65", "66"]

    count = 1
    for i in indexlist:
        intList = lt.newList(datastructure="ARRAY_LIST")
        lt.addLast(intList, "minLon")
        lt.addLast(intList, "maxLon")
        lt.addLast(intList, "minLat")
        lt.addLast(intList, "maxLat")
        
        
        if i[1] == "1":
            lt.changeInfo(intList, 0, -180.0) 
            lt.changeInfo(intList, 1, -150.0)
        elif i[1] == "2":
            lt.changeInfo(intList, 0, -150.0) 
            lt.changeInfo(intList, 1, -120.0)       
        elif i[1] == "3":
            lt.changeInfo(intList, 0, -120.0) 
            lt.changeInfo(intList, 1, -90.0)       
        elif i[1] == "4":
            lt.changeInfo(intList, 0, -90.0) 
            lt.changeInfo(intList, 1, -60.0)       
        elif i[1] == "5":
            lt.changeInfo(intList, 0, -60.0) 
            lt.changeInfo(intList, 1, -30.0)      
        else:
            lt.changeInfo(intList, 0, -30.0) 
            lt.changeInfo(intList, 1, 0.0)

        if i[0] == "1":
            lt.changeInfo(intList, 2, 0.0) 
            lt.changeInfo(intList, 3, 30.0)
        elif i[0] == "2":
            lt.changeInfo(intList, 2, 30.0) 
            lt.changeInfo(intList, 3, 60.0)
        elif i[0] == "3":
            lt.changeInfo(intList, 2, 60.0) 
            lt.changeInfo(intList, 3, 90.0)
        elif i[0] == "4":
            lt.changeInfo(intList, 2, 90.0) 
            lt.changeInfo(intList, 3, 120.0)
        elif i[0] == "5":
            lt.changeInfo(intList, 2, 120.0) 
            lt.changeInfo(intList, 3, 150.0)
        else:
            lt.changeInfo(intList, 2, 150.0) 
            lt.changeInfo(intList, 3, 180.0)
            
        mp.put(archive["GeoSector"], count, intList)
        count +=1

            

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

