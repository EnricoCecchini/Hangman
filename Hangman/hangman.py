import numpy as np
import random

#Abre y lee las palabras del archivo de texto y las guarda en un arreglo
f = open('listaPalabras.txt', 'r')
listaPalabras = f.readlines()
f.close()

#Nombre de jugador
nombre = input("Como te llamas?\n")

#Elige una palabra random
palabra = random.choice(listaPalabras)

#Crea una palabra vacia donde aparecen las letras que se adivinan
palabraSinAdivinar = ["_"]
for i in range(len(palabra)):
    palabraSinAdivinar.append('_')

palabraSinAdivinar.pop(-1)
palabraSinAdivinar.pop(-1)

#Vidas de jugador
vidas = 10

#Despliega la palabra a adivinar
print(palabraSinAdivinar)

#Ciclo de juego
while(vidas > 0):

    letra = input(nombre + ", elige una letra\n")
    
    #Checa si la letra ingresada esta dentro de la palabra
    for i in range(len(palabra)): 
        if(letra == palabra[i]):
            palabraSinAdivinar[i] = letra
    if(letra not in palabra):
        vidas -= 1
     
    print("Vidas: ", vidas)
    
    #Une las letras de la palabra sin adivinar en un String para comparar
    guess = ''.join([str(elem) for elem in palabraSinAdivinar]) 
    
    #Despliega la palabra a adivinar
    print(palabraSinAdivinar)

    #Compara guess con la palabra que se debe adivinar, para determinar si se gano el juego o no
    if(guess == palabra.strip()):
         print("Ganaste! La palabra era:", palabra)
         break
    elif(vidas == 0):
        print("Perdiste! La palabra era:", palabra)

