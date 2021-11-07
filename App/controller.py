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

