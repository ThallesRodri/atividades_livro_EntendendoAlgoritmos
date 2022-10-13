# 1. O que é pesquisa binária?

Pesquisa binária é um modo de encontrar algo com o menor número de "chutes" possível. No livro "Entendendo algoritmos", de Aditya Y. Bhargava (2015) ao qual essa lista de exerícios e resumos se baseia, cita um exemplo diferenciando dois tipos de pesquisa: a simples e a binária.

Vamos supor que uma pessoa te pede para adivinhar um número entre 1 e 100, e ela te avisará se o valor que você chutou é muito alto ou muito baixo. Você pode tentar pela pesquisa simples, falando os números em sequência:

> Você: 1!
>
> Pessoa: Muito baixo!
>
> Você: 2!
>
> Pessoa: Muito baixo!

e assim por diante...

Agora tentando pela pesquisa binária, você começaria logo pela metade, então a cada chute, você corta metade das alternativas:

> Você: 50!
>
> Pessoa: Muito baixo!
>
> Você: 75!
>
> Pessoa: Muito alto!
>
> Você: 63!
>
> Pessoa: Muito alto!
>
> Você: 57!
>
> Pessoa: ACERTO, MIZERAVI!

Agora imagine esse conceito em qualquer busca em uma lista ordenada de qualquer coisa, podemos encontrar o que procuramos com poucos passos, economizando um bom tempo!

Para saber quantos passos serão necessários para chegar a um resultado usando a pesquisa binária, podemos usar a função logaritmo. Se você quer saber, por exemplo, quantos passos é preciso para adivinhar um número de 0 até 240.000, basta fazer log 2 de 240.000, o resultado será, na pior das hipóteses, 18 passos! Agora imagine fazer isso na pesquisa simples, na pior das hipoteses você levaria 240.000 passos para achar o resultado.

Resumindo, para achar algo mais rapidamente, divida as alternativas pela metade, até achar o que procura!

# 1.1 Algoritmos nesse repositório

Nesse repositório há dois algoritmos. O chamado "busca_binaria_exemplo.py" é o exemplo retirado do livro, onde simula uma pequena busca binária usando uma lista, somente para fins didáticos. O segunto algoritmo chamado "logaritmo.py" eu fiz por curiosidade, queria testar se eu conseguiria fazer um programa que calcula logaritmos de acordo com os desejos do usuário.

# 2. Conclusão

Isso foi o resumo do resumo do primeiro capitulo do livro, ele aborda muito mais coisas, como a explicação da notação Big O, o problema do caixeiro viajante e uma explicação bem mais aprofundada sobre pesquisa binária. Se você que está lendo tiver interesse, eu recomendo fortemente que adquire esse material, ele é ótimo!
