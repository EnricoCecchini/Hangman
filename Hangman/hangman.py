import numpy as np
import random

f = open('listaPalabras.txt', 'r')
listaPalabras = f.readlines()
f.close()

nombre = input("Como te llamas?\n")

palabra = random.choice(listaPalabras)

palabraSinAdivinar = ["_"]

for i in range(len(palabra)):
    palabraSinAdivinar.append('_')

palabraSinAdivinar.pop(-1)
palabraSinAdivinar.pop(-1)

vidas = 10

while(vidas > 0):

    print(palabraSinAdivinar)

    letra = input(nombre + ", elige una letra\n")

    for i in range(len(palabra)): 
        if(letra == palabra[i]):
            palabraSinAdivinar[i] = letra
    if(letra not in palabra):
        vidas -= 1
     
    print("Vidas: ", vidas)

    guess = ''.join([str(elem) for elem in palabraSinAdivinar]) 

    if(guess == palabra.strip()):
         print("Ganaste! La palabra era:", palabra)
         break
    elif(vidas == 0):
        print("Perdiste! La palabra era:", palabra)

