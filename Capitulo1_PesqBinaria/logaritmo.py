# Existe a função log() no python, mas criei só pra ver como seria se não existisse essa função para descobrir logaritmo

def calcularLog(numero, log):
    cont = 0
    resultado = int(numero) # log de 0 é 1

    while resultado > 1:
        resultado = int(resultado / log) # Divide o numero pela log até dar 1
            
        cont+=1 # Conta quantas vezesa divisão teve que ser feita para chegar a 0 ou 1, esse é o resultado logaritmo

    return cont

numero = int(input('Numero: '))
log = int(input('Logaritmo: '))

print("O log ", log, " de ", numero, " é igual a ", calcularLog(numero, log)) 
    
   
