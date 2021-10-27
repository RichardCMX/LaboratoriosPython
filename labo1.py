#!/usr/bin/python3
# Este codigo es para imprimir una piramide inversa en la consola
char = str(input('Caracter -> '))
iter = int(input('Altura -> '))
base = ''
for x in range (iter):
    base += char

while iter > 0:
    print(base[:iter])
    iter -= 1
