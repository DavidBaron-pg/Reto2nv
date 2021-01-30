# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 17:14:22 2021

@author: Andres
"""

# -*- coding: utf-8 -*-
"""
Modulo Tkinder

@author: Andres
"""
# Importacion del paquete tkinder

import tkinter
from tkinter import *
import extraccion_info_pok as eip
from tkinter import messagebox as tkMessageBox
from functools import partial

"""
#Creacion de la funcion
def act_buton(nombre_pok, abil_pok, abil_frame):

    abil = ["\u2022 " + x + " \n" for x in abil_pok]
    abil_text = 'Las habilidades del pokemon ' + nombre_pok + ' son las siguientes: \n' +  ''.join(abil)
    
    abil_Label = Label(abil_frame, text= abil_text, bg="yellow", font=("Roboto", 16), wraplength=int(width_a))
    abil_Label.place(x = 30, y = 0)
"""    

#Creacion funcion que contiene el texto a mostrar al presionar el boton
def abil_message(lista):
   nombre_pok, abil_pok = lista[0], lista[1]
   abil = ["\u2022 " + x + " \n" for x in abil_pok]
   abil_text = 'Las habilidades del pokemon ' + nombre_pok + ' son las siguientes: \n' +  ''.join(abil)
   tkMessageBox.showinfo('Habilidades del pokemon', abil_text)
   
print('Obteniendo la informacion de los pokemones...')

desc_gen = ("Lorem  ipsum  dolor sit  amet,  consectetur adipisicing  elit, sed  do eiusmod tempor incididunt  ut labore  et dolore magna aliqua. Ut  enim  ad  minim  veniam, quis  nostrud exercitation  ullamco laboris  nisi  ut  aliquip  ex  ea  commodo  consequat.  Duis  aute irure dolor  in  reprehenderit  in  voluptate  velit  esse  cillum  dolore eu fugiat nulla pariatur. Excepteur  sint  occaecat cupidatat non  proident, sunt  in  culpa qui  officia deserunt  mollit anim id  est  laborum.") 
url_txt = r"https://pokeapi.co/api/v2/pokemon/"
abilid_pokemon = eip.info_pok(lista_pok, url_txt)

lista_pok = [x['nombre_pokemon'] for x in abilid_pokemon]
pok_abilidades = [x['habilidades'] for x in abilid_pokemon]
print('Informacion de los pokemones obtenida !')

# Creacion de una ventana(raiz)
ventana = Tk()

#Asigna un titulo a la ventana
ventana.title("" )

#Establece que no se puede cambiar el tamaño(Ancho y alto)
"""ventana.resizable(0 , 0)"""

#Asignar el tamaño de la pantalla  a variable width_s y  height_s
#Ancho
width_s ="1920"
#Alto
height_s="1080"

#Establecer el tamaño de la ventana/
ventana.config(width = width_s, height= height_s)

#Asigna la ventana a tamaño completo de la pantalla
ventana.attributes("-fullscreen", True)

# Seleccionar imagen para establecer el icono de la ventana
ventana.iconbitmap("poke.ico")

# Cambiar el color de fondo
ventana.config(bg="white")

#Agregar imagen de fondo para la raiz
imagen = PhotoImage(file ="all_pok.png" )  
fondo = Label(ventana, image = imagen).place(x=0, y=0)

# Creacion de etiqueta, color fondo, color texto , fuente, tamaño, fuente y ubicacion del texto de la etiqueta
etiqueta1 = Label(ventana, text="LISTA DE POKEMONES", relief = "groove" , bd=10, fg="black", bg="white", font=("Roboto", 25)).pack(anchor=CENTER)

# Creacion de etiqueta 2, color fondo, color texto , fuente, tamaño, fuente y ubicacion del texto de la etiqueta
etiqueta2 = Label(ventana, text="AQUI PUEDES VER TUS POKEMONES", relief = "groove" , bd=10, fg="black", bg="white", font=("Roboto", 15)).pack(anchor=CENTER)   #place(x=520, y=120, width=500, height=40)

"""
Creacion de  frame
"""
width_c = int(width_s)/len(lista_pok)
height_c = "400"

#Se crea un for para iterar los elementos a lo largo de "lista_pok" 
for i in range(len(lista_pok)):
    
    miFrame = Frame()
    #Empaquetar frame- Aqui se le puede dar posicion
    miFrame.pack(side=LEFT )
 
    #Añadir tipo de borde y tamaño borde
    miFrame.config(relief = "groove" , bd=10  )
    
    #Cambiar color fondo MiFrame
    miFrame.config(bg = 'yellow')
    
    #Establecer el tamaño del frame
    miFrame.config(width =width_c, height=height_c)
    
    #Creacion label para el nombre pokemon
    miLabel = Label(miFrame, text= lista_pok[i].upper(), fg="black", bg="yellow", font=("Roboto", 15))
    miLabel.place(x=width_c/ 3 , y=30 , anchor="center")
    
    #Creacion label para la descripcion generica
    desc_Label = Label(miFrame, text= desc_gen, bg="yellow", wraplength=180)
    desc_Label.place(x=0, y=80)
    
    #Creacion del label para el boton, asi como su configuracion del texto, y el tamaño y posicion del boton
    bot_Label = Label(miFrame, text= "HABILIDADES", wraplength=200)
    bot_Label.place(x=50, y=340)
    
    #Creacion del boton y la acion que realiza al presionarse
    boton = Button(bot_Label, text='HABILIDADES',state = 'active', command = partial(abil_message,[lista_pok[i], pok_abilidades[i]]))
    boton.pack()
   
#Se llama la funcion mainloop para que el programa no termine
ventana.mainloop()
