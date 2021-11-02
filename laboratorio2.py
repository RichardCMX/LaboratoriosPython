#!/usr/bin/python3
"""
Este programa tiene la funcion de recopilar interactivamente nombres completos
para corregir la capitalizacion de los mismos y finalmente imprimir
los nombres corregidos.
"""

special_characters = '~!@#$%^&*()-+?_=,<>/:;.,|><1234567890\'\"\\'

names = []


def mayus_sorter(a):  # Funcion que arregla los nombres
    new_name = []
    for i in x:

        # Para cada palabra se usa la funcion capitalize para corregirla
        cap = i.capitalize()
        new_name.append(cap)

    # new_name se transforma en un solo string y se agrega a names
    corrected_name = ' '.join(new_name)
    names.append(corrected_name)


while(True):
    name = str(input('Introduzca un nombre completo o SALIR para salir: '))

    # Cuando se introduzca "SALIR" el programa se detiene
    if (name == 'SALIR'):
        break

    #  Convierte el nombre en una lista para identificar su tamanno
    x = name.split(' ')

    # Detecta si hay un caracter en la lista special_characters
    if any(c in special_characters for c in name):
        print('\nERROR \nTiene caracteres especiales.\n')
    else:
        if len(x) == 3:
            mayus_sorter(x)

        elif len(x) == 4:
            mayus_sorter(x)

        else:
            print('\nERROR \nEl nombre debe tener 3 o 4 componentes.\n')

for n in names:  # Por ultimo se imprime la lista de nombres corregida
    print(n)
