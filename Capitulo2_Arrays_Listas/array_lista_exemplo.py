def buscaMenor(array):
    menor = array[0]
    menor_indice = 0

    for i in range(1, len(array)):
        if array[i] < menor: # Se o valor de indice atual for menor que o valor do indice 0, ele é o menor valor.
            menor = array[i]
            menor_indice = i # Armazena o indice do menor valor
    return menor_indice

def ordenacaoPorSelecao(array):
    novoArray = []

    for i in range(len(array)): 
        menor = buscaMenor(array) # Encontra o menor elementeo do array e adiciona ao novo array
        novoArray.append(array.pop(menor)) # Vai "diminuindo" o array. O pop exclui o valor do array original

    return novoArray

print(ordenacaoPorSelecao([5,3,6,2,10]))
