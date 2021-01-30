# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:13:22 2021

@author: Andres
"""

#Importacion de las librerias
import requests
import json
import numpy as np


"""
Funcion utilizada para extraer la informacion de los pokemones usando el nombre y la url
Entradas
    lista_pok: Lista que contiene los nombres de los pokemones que uds asasasas
    url_txt: url de la cual se va a extraer la informacion
Salidas:
    abil_pok: Arreglo que contiene la informacion de los pokemos
"""

def info_pok(lista_pok, url_txt):
    
    nombre_pok = np.array(lista_pok)
    
    #Lista vacia para ir agregando la informacion necesaria de los pokemones
    abil_pok = []
    
    '''
    Iteraciones para extraer la informacion de todos los pokemones que estan en 
    la lista anteriomente creada
    '''
    
    for pokemon in nombre_pok:
        
        try:
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
            print('Inforacion del pokemon ' + pokemon +' fue extraida exitosamente.')
        
        except:
            dic_pok = {'nombre_pokemon': str(pokemon), 'habilidades':['El pokemon no fue encontrado en la url']}
            print('Inforacion del pokemon ' + pokemon + ' no fue encontrada.')
            
        #Agregar la informacion a la lista de los pokemones (esta lista es iterable)
        abil_pok.append(dic_pok)
            
    return abil_pok


