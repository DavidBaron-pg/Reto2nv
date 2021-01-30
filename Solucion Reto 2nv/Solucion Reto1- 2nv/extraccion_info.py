# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:11:39 2021

@author: Andres
"""

#Importacion de las librerias
import requests
import json
import numpy as np

#Url de donde se extrae la información
url_txt = r"https://pokeapi.co/api/v2/pokemon/"

#Arreglo que contiene los nombres de los pokemones
lista_pok = ['spearow','fearow','ekans','arbok','pikachu','raichu','sandshrew',\
              'sandslash','nidorina']
nombre_pok = np.array(lista_pok)

#Lista vacia para ir agregando la informacion necesaria de los pokemones
abil_pok = []

'''
Iteraciones para extraer la informacion de todos los pokemones que estan en 
la lista anteriomente creada
'''

for pokemon in nombre_pok:
    
    #Extraccion de la informacion del pokemon usando la url y convirtiendola en texto
    r = requests.get(url_txt + pokemon)
    texto = r.text
    
    #Transformacion del texto en un diccionario iterable
    texto = json.loads(texto)
    
    """
    Extraer unicamente el nombre de las habilidades del pokemon (se asume que 
    la demas informacion no se necesita, pero igual puede ser consultada si es necesaria)
    """
    abilities = [x['ability']['name'] for x in texto['abilities']]
    
    """
    Creacion del diccionario que contiene el nombre y las habilidades del pokemon
    """
    dic_pok = {'nombre_pokemon': str(pokemon), 'habilidades':abilities}
    
    #Agregar la informacion a la lista de los pokemones (esta lista es iterable)
    abil_pok.append(dic_pok)
    