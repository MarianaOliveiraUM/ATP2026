# TPC4

## Índice

- [Dados pessoais](#dados-pessoais)
- [Resumo](#resumo)
- [Lista de resultados](#lista-de-resultados)

---

## Dados pessoais

**Nome:** Mariana Veloso Oliveira  
**ID:** a115027 

<img src="foto4.jpg" alt="Foto do autor" width="100">

---

## Resumo

### Descrição

Este programa consiste numa aplicação em Python para criar e trabalhar com listas de números. O programa apresenta um menu com várias opções que permitem ao utilizador criar uma lista de números aleatórios, introduzir uma lista manualmente e realizar diferentes operações com a lista guardada nesse momento.

A aplicação permite calcular a soma e a média dos elementos, descobrir o maior e o menor número, verificar se a lista está ordenada por ordem crescente ou decrescente e procurar um determinado elemento dentro da lista.

O programa utiliza uma variável interna chamada `lista`, onde fica guardada a lista que está a ser utilizada. Sempre que é criada uma nova lista através das opções 1 ou 2, a lista anterior é substituída pela nova.

### Funcionamento do programa

Quando o programa começa, é apresentado um menu com as opções disponíveis:

* **(1) Criar Lista** — cria uma lista com números aleatórios entre 1 e 100.
* **(2) Ler Lista** — permite ao utilizador introduzir os números da lista.
* **(3) Soma** — calcula a soma de todos os elementos da lista.
* **(4) Média** — calcula a média dos elementos da lista.
* **(5) Maior** — indica o maior elemento da lista.
* **(6) Menor** — indica o menor elemento da lista.
* **(7) Ordem crescente** — verifica se a lista está ordenada por ordem crescente.
* **(8) Ordem decrescente** — verifica se a lista está ordenada por ordem decrescente.
* **(9) Procura um elemento** — procura um número na lista e indica a sua posição.
* **(0) Sair** — termina o programa e mostra a lista que ficou guardada.

Depois de escolher uma opção, o programa realiza a operação correspondente e volta a apresentar o menu. Desta forma, é possível realizar várias operações sobre a mesma lista sem ter de executar novamente o programa.

### Criação da lista

Na opção 1, utilizei a função `criarLista()` para criar uma lista com números aleatórios.

Primeiro, o programa pergunta ao utilizador quantos números quer na lista. Depois, através de um ciclo `while`, são gerados números aleatórios entre 1 e 100 com:

`numero = random.randint(1, 100)`

Cada número gerado é acrescentado à lista através de `append()`.

No final, a função devolve a lista criada e esta fica guardada na variável `lista`.

### Leitura da lista

Na opção 2, utilizei a função `leLista()`.

Tal como na opção anterior, o utilizador começa por indicar quantos números quer introduzir. Depois, o programa utiliza um ciclo `while` para pedir cada número individualmente.

Cada número introduzido é acrescentado à lista através de: `lista.append(num)`

No final, a lista é devolvida e guardada na variável interna `lista`.

Se já existia uma lista, esta é substituída pela nova lista, tal como pedido no enunciado.

### Soma

Na opção 3, utilizei a função `somaLista(lista)`.

A variável `soma` começa com o valor 0. Depois, através de um ciclo `while`, o programa percorre todos os elementos da lista e vai adicionando cada um à soma.

No final, a função devolve o resultado.

### Média

Na opção 4, utilizei a função `mediaLista(lista)`.

Primeiro é calculada a soma de todos os elementos da lista. Depois, essa soma é dividida pelo número de elementos da lista, utilizando `len(lista)`.

A média é então devolvida pela função e apresentada no monitor.

### Maior elemento

Na opção 5, utilizei a função `maiorLista(lista)`.

Comecei por considerar que o primeiro elemento da lista era o maior:

`maior = lista[0]`

Depois, percorri a lista com um ciclo `while`. Sempre que encontrava um elemento maior do que o valor guardado em `maior`, esse valor era substituído.

No final, a função devolve o maior elemento da lista.

### Menor elemento

Na opção 6, utilizei a função `menorLista(lista)`.

O funcionamento é semelhante ao da função anterior. Inicialmente, considero o primeiro elemento como sendo o menor:

`menor = lista[0]`

Depois, o programa percorre os restantes elementos e, quando encontra um número menor, atualiza o valor da variável `menor`.

No final, é devolvido o menor elemento da lista.

### Ordem crescente

Na opção 7, utilizei a função `crescenteLista(lista)` para verificar se a lista está ordenada por ordem crescente.

Para isso, o programa compara cada elemento com o elemento seguinte. Se encontrar um elemento maior do que o seguinte, significa que a lista não está ordenada por ordem crescente.

Utilizei a variável `res`, que começa com o valor `True`. Se for encontrada uma situação que não respeite a ordem crescente, `res` passa para `False`.

No final, a função devolve `True` ou `False`, e o programa apresenta uma mensagem a indicar se a lista está ou não ordenada por ordem crescente.

### Ordem decrescente

Na opção 8, utilizei a função `decrescenteLista(lista)`.

O funcionamento é semelhante ao da verificação da ordem crescente, mas neste caso o programa verifica se cada elemento é maior ou igual ao seguinte.

Se encontrar um elemento menor do que o elemento seguinte, a lista não está ordenada por ordem decrescente.

Tal como na função anterior, utilizei a variável `res` para guardar o resultado da verificação.

### Procura de um elemento

Na opção 9, utilizei a função `procura(lista, elemento)`.

Primeiro, a variável `posicao` começa com o valor `-1`. Este valor é utilizado para representar o caso em que o elemento procurado não existe na lista.

Depois, o programa percorre a lista através de um ciclo `while`. Quando encontra o elemento procurado, guarda a sua posição na variável `posicao`.

As posições da lista começam em `0`, por isso, por exemplo, o primeiro elemento está na posição 0 e o segundo está na posição 1.

No final, a função devolve a posição encontrada. Se o elemento não existir, devolve `-1`.

### Menu e repetição do programa

A aplicação utiliza um ciclo `while` para manter o menu a funcionar.

A variável `opcao` guarda o número escolhido pelo utilizador. Dependendo do valor introduzido, o programa entra numa das condições `if` ou `elif` e executa a operação correspondente.

Por exemplo, se o utilizador escolher a opção 3, é chamada a função:

`somaLista(lista)`

Depois de executar a operação, o programa volta ao início do ciclo e apresenta novamente o menu.

Também foi feita uma verificação para confirmar se existe uma lista antes de realizar as operações 3 a 9. Se ainda não tiver sido criada nenhuma lista, o programa apresenta a mensagem:

`Não existe nenhuma lista.`

Quando o utilizador escolhe a opção 0, é apresentada uma mensagem a indicar que o programa terminou e é mostrada a lista que ficou guardada naquele momento.

## Estruturas utilizadas

Neste programa utilizei principalmente as seguintes estruturas e comandos:

* `def` para criar as diferentes funções;
* `if`, `elif` e `else` para tomar decisões;
* `while` para repetir operações e manter o menu em funcionamento;
* `input()` para receber informações do utilizador;
* `print()` para apresentar informações no monitor;
* variáveis para guardar valores;
* listas para guardar os números;
* `append()` para adicionar elementos às listas;
* `len()` para saber o número de elementos de uma lista;
* `return` para devolver os resultados das funções;
* `random.randint()` para gerar números aleatórios.

---

## Lista de resultados

- [Aplicação para manipulação de listas de inteiros](TPC4.py)
