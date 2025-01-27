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
 """

import config as cf
from App import model
import datetime
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    archive = model.newArchive()
    return archive
# Funciones para la carga de datos
def loadData(archive, ovnisfile):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    ovnisfile = cf.data_dir + ovnisfile
    input_file = csv.DictReader(open(ovnisfile, encoding="utf-8"),
                                delimiter=",")
    for ovni in input_file:
        model.addOvni(archive, ovni)
    return archive
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo
def getOvnisInCity(archive, City):
    """
    Retorna el total de avistamientos en una ciudad
    """
    Ciudad = (str(City)).lower
    return model.getOvnisInCity(archive, Ciudad)

def durationRangeCount(archive, wSecMin, wSecMax):
    """
    Retorna los avistamientos con una duración en segundos contenida en el rango
    """
    return model.durationRangeCount(archive, wSecMin, wSecMax)


def dateRangeSights(archive, minDate, maxDate):
    """
    Retorna los avistamientos en un rango de fechas
    """
    return model.dateRangeSights(archive, minDate, maxDate)
#---#3
def getSightByRangeHM(archive, limiteinf,limitesup):
    """
    Retorna los avistamientos en un rango de tiempo en el día
    """
    return model.getSightByRangeHM(archive, limiteinf,limitesup)
#---#5
def getHowSightInZone(archive, limiteinfLat, limitesupLat,
                    limiteinfLon, limitesupLon):
    """
    Retorna los avistamientos en un zona geográfica
    """
    return model.getHowSightInZone(archive, limiteinfLat, limitesupLat,
                    limiteinfLon, limitesupLon)
#---#6BONO
def getSightInZone(archive, limiteinfLat, limitesupLat,
                    limiteinfLon, limitesupLon):
    """
    Permite visualizar los avistamientos de una zona geográfica
    """
    return model.getSightInZone(archive, limiteinfLat, limitesupLat,
                    limiteinfLon, limitesupLon)

def example():
    """
    Ejemplo de libreria
    """
    return model.example()