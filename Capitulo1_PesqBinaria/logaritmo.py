# Existe a função log() no python, mas criei só pra ver como seria se não existisse essa função para 3 descobrir logaritmo
# Data: 23/06/2022

numero = int(input('Numero: '))
cont = 0
resultado = 1

while resultado < numero:
    if resultado < int(numero):
        resultado = resultado *2
        cont+=1
print(cont) 
    
   
