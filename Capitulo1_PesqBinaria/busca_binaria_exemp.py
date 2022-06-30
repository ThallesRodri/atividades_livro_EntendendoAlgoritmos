# Exemplo de algoritmo que faz uma busca binária de uma lista de números.
# Retirado do livro 'Entendendo Algoritmos' - Aditya Bhargava.
# Mais informações no arquivo ReadMe
# Data: 24/06/2022

def pesquisa_binaria(lista,item):
    baixo = 0
    alto = len(lista)
    contador = 0
    while baixo <= alto:
        meio = (baixo+alto) // 2
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio-1
        else:
            baixo = meio + 1
        contador += 1
    print('Tentativas: ', contador) # Numero de tentativas até achar o item
    return None

minha_lista = [1,3,5,7,9]

print (pesquisa_binaria(minha_lista, 7))
print (pesquisa_binaria(minha_lista, -1))
