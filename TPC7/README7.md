# TPC7

## Índice

- [Dados pessoais](#dados-pessoais)
- [Resumo](#resumo)
- [Lista de resultados](#lista-de-resultados)

---

## Dados pessoais

**Nome:** Mariana Veloso Oliveira  
**ID:** a115027 

<img src="foto7.jpg" alt="Foto do autor" width="100">

---

## Resumo

### Descrição

Neste trabalho resolvi vários exercícios em Python, relacionados com listas, strings, números e dicionários.

O trabalho está dividido em três partes. Na primeira, trabalhei com listas em compreensão. Na segunda, criei funções para realizar algumas operações com strings e números. Por fim, na terceira parte, trabalhei com uma lista de dicionários que representa uma rede social.

### Funcionamento do programa

**TPC1 – Listas em compreensão**

Nesta primeira parte, comecei por resolver três exercícios utilizando listas em compreensão.

- **Alínea a):** Criei uma lista com os elementos que não aparecem nas duas listas ao mesmo tempo. Para isso, fui verificar quais os elementos de cada lista que não existiam na outra.
- **Alínea b):** A partir de um texto, criei uma lista apenas com as palavras que tinham mais de três letras. Utilizei `split()` para separar as palavras e `len()` para verificar o seu comprimento.
- **Alínea c):** Criei uma lista de tuplos em que cada elemento contém o número da posição e o valor correspondente da lista inicial. Para percorrer a lista utilizei `range()` e `len()`.

**TPC2 – Funções**

Nesta parte, resolvi quatro exercícios, cada um com uma função diferente.

**Alínea a) – `strCount()`**

Esta função permite contar quantas vezes uma determinada substring aparece numa string, sem contar ocorrências sobrepostas.

Para fazer esta comparação, utilizei dois ciclos `while`. Quando encontro a substring, aumento o contador e avanço a posição de acordo com o seu comprimento. Caso não encontre, avanço apenas uma posição.

**Alínea b) – `produtoM3()`**

Esta função recebe uma lista de números e calcula o produto dos três menores elementos.

Primeiro, utilizei `sorted()` para ordenar os números por ordem crescente. Depois, multipliquei os três primeiros elementos e devolvi o resultado com `return`.

**Alínea c) – `reduxInt()`**

Nesta alínea, criei uma função que soma os algarismos de um número até ficar apenas com um algarismo.

Utilizei um ciclo `while` para repetir o processo enquanto o número tivesse dois ou mais algarismos. Dentro desse ciclo, utilizei `for` para percorrer os algarismos e calcular a sua soma.

**Alínea d) – `myIndexOf()`**

Esta função procura uma string dentro de outra e devolve a posição onde aparece pela primeira vez.

Para isso, utilizei um ciclo while e uma variável resultado, que começa com o valor -1. O ciclo repete-se enquanto a segunda string ainda couber na primeira a partir da posição atual e enquanto não tiver encontrado nenhuma ocorrência. Em cada posição, comparo um pedaço da primeira string, com o mesmo tamanho da segunda, com a própria segunda string. Se forem iguais, guardo a posição em resultado e o ciclo termina. Caso contrário, avanço uma posição. No fim, a função devolve a posição encontrada ou -1 se não encontrar.

**TPC3 – A Rede Social**

Na última parte do trabalho, comecei por criar uma lista chamada `MyFaceBook`, onde cada elemento é um dicionário que representa uma publicação.

Cada publicação tem um identificador (`id`), o conteúdo, o autor, a data de criação e uma lista de comentários. Os comentários também estão organizados em dicionários, com o respetivo texto e autor.

Para manipular e consultar esta informação, foram desenvolvidas as seguintes funções:
- quantosPost() – indica o número total de publicações existentes na rede social, utilizando len().
- postsAutor() – devolve uma lista com todas as publicações de um determinado autor.
- autores() – devolve a lista de autores das publicações, sem repetições e ordenada alfabeticamente.
- insPost() – permite acrescentar uma nova publicação à rede social. O novo identificador é calculado a partir dos identificadores já existentes.
- remPost() – remove uma publicação da rede social através do seu identificador.
- postsPorAutor() – calcula a distribuição do número de publicações por autor, utilizando um dicionário para guardar os resultados.
- comentadoPor() – devolve a lista de publicações que foram comentadas por um determinado autor, percorrendo também a lista de comentários de cada publicação.

### Estruturas utilizadas

Ao longo deste trabalho utilizei vários conteúdos que foram abordados nas aulas, nomeadamente:

- `def` para criar as funções;
- `if`, `elif` e `else` para fazer comparações e tomar decisões;
- `for` e `while` para percorrer elementos e repetir instruções;
- `return` para devolver os resultados das funções;
- listas, tuplos e dicionários para guardar e organizar informação;
- `len()` para obter o comprimento de listas e strings;
- `sorted()` para ordenar elementos;
- `append()` para adicionar elementos a uma lista;
- `split()` para separar as palavras de um texto.

---

## Lista de resultados

- [TPC7 – Teste de aferição](TPC7.ipynb)
