# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 18:29:39 2021

@author: Andres
"""

import pandas as pd
import numpy as np


ruta = r'C:\Users\Andres\Desktop\Solucion Reto 2nv\Solucion Reto2.2nv\vehicles.csv\\'
nombre_archivo = r'vehicles.csv'
used_cards_dataset = pd.read_csv(ruta + nombre_archivo)

# =============================================================================
# 1
# =============================================================================
#Convertir el campo year en int
used_cards_dataset['year_int'] = used_cards_dataset['year'].astype(dtype = int, errors = 'ignore')
used_cards_dataset['year'] = used_cards_dataset['year_int']
used_cards_dataset = used_cards_dataset.drop('year_int', axis = 1)

# =============================================================================
# 2
# =============================================================================
numero_regiones = used_cards_dataset['region'].unique()
registros_por_region = used_cards_dataset.groupby('region').size()

# =============================================================================
# 3
# =============================================================================
used_cards_dataset_no_nulos = used_cards_dataset.dropna()
used_cards_dataset_no_nulos.to_csv(ruta + 'vehicles_no_null_reg.csv', sep = ';')

# =============================================================================
# 4
# =============================================================================
cond1 = used_cards_dataset['price'] >= 15000 
cond2 = used_cards_dataset['condition'] == 'good'
cond3 = used_cards_dataset['condition'] == 'excelent'
filtro_used_cards_dataset = used_cards_dataset[cond1 & (cond2 | cond3 )]

# =============================================================================
# 5
# =============================================================================
cond4 = used_cards_dataset['paint_color'] == 'blue'
cond5 = used_cards_dataset['manufacturer'] == 'chevrolet'
blue_chev_cars = used_cards_dataset[ cond4 & cond5 ]