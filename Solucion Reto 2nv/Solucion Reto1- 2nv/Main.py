# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:15:23 2021

@author: Andres
"""
import extraccion_info_pok as eip

#Url de donde se extrae la información
url_txt = r"https://pokeapi.co/api/v2/pokemon/"

#Listado de elementos del arreglo
lista_pok = ['spearow', 'fearow', 'ekans', 'arbok', 'pikachu', 'raichu', 'sandshrew', 'sandslash', 'nidorina']

#Descripcion generica(lorem ipsum) para todos los pokemones
desc_gen = ("Lorem  ipsum  dolor sit  amet,  consectetur adipisicing  elit, sed  do eiusmod tempor incididunt  ut labore  et dolore magna aliqua. Ut  enim  ad  minim  veniam, quis  nostrud exercitation  ullamco laboris  nisi  ut  aliquip  ex  ea  commodo  consequat.  Duis  aute irure dolor  in  reprehenderit  in  voluptate  velit  esse  cillum  dolore eu fugiat nulla pariatur. Excepteur  sint  occaecat cupidatat non  proident, sunt  in  culpa qui  officia deserunt  mollit anim id  est  laborum.")


abil_pok = eip.info_pok(lista_pok, url_txt)
