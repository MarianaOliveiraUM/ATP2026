# TPC2

## Índice

- [Dados pessoais](#dados-pessoais)
- [Resumo](#resumo)
- [Lista de resultados](#lista-de-resultados)

---

## Dados pessoais

**Nome:** Mariana Veloso Oliveira  
**ID:** a115027 

<img src="foto1.jpg" alt="Foto do autor" width="100">
---

## Resumo

### Descrição

Este programa consiste no jogo **Corrida para o 100**. O total começa em 0 e, em cada jogada, o utilizador ou o computador acrescenta um número entre 1 e 10. O objetivo é chegar exatamente ao número 100.

O jogo tem duas modalidades diferentes: numa delas o computador joga primeiro e utiliza uma estratégia que lhe permite ganhar sempre; na outra, o utilizador joga primeiro e o computador utiliza uma estratégia que pode permitir-lhe ganhar, dependendo da primeira jogada do utilizador. No final de cada partida, é possível jogar novamente.

### Funcionamento do programa

Quando o programa começa, o utilizador pode escolher uma das duas modalidades:

* **Modalidade 1:** o computador joga primeiro e começa por acrescentar 1. Depois, utiliza a estratégia `11 - jogada_utilizador`.

* **Modalidade 2:** o utilizador joga primeiro. Na primeira jogada do computador é utilizada a estratégia `12 - jogada_utilizador` e, nas jogadas seguintes, `11 - jogada_utilizador`.

Em ambas as modalidades, o programa verifica se o número introduzido pelo utilizador está entre 1 e 10 e continua o jogo até alguém atingir o 100.

#### Modalidade 1

Na primeira modalidade, o computador começa sempre por acrescentar 1: `jogada = 1`.

Após cada jogada do utilizador, o computador calcula a sua jogada através de: `jogada = 11 - jogada_utilizador`.

Desta forma, entre a jogada do utilizador e a do computador são acrescentados sempre 11. Assim, o computador consegue manter os totais 1, 12, 23, 34,... até chegar ao 100, garantindo a vitória.

Para repetir as jogadas utilizei um ciclo `while`, controlado pela variável `acertou`.

#### Modalidade 2

Na segunda modalidade, o utilizador joga primeiro e o computador utiliza uma estratégia diferente na sua primeira jogada: `jogada = 12 - jogada_utilizador`.
Por exemplo, se o utilizador começar por acrescentar 5, o computador acrescenta 7, ficando o total em 12.

Depois da primeira jogada, o computador passa a utilizar: `jogada = 11 - jogada_utilizador`.

Existe ainda um caso especial quando o utilizador começa por 1. Nesse caso, 12 - 1 daria 11, o que não é permitido, pois cada jogada só pode ser entre 1 e 10. Por isso, o computador acrescenta 10. Nesta situação, o computador pode ganhar ou perder dependendo das jogadas seguintes.

Para saber se está na primeira jogada do computador, utilizei a variável `primeira_jogada`.

### Validação das jogadas

Para garantir que o utilizador apenas introduz valores entre 1 e 10, utilizei um ciclo `while`: `while jogada_utilizador < 1 or jogada_utilizador > 10:`. Desta forma, se for introduzido um valor inválido, o programa pede novamente uma jogada.

### Repetição do jogo

Depois de terminar uma partida, o programa pergunta: `"Quer jogar novamente? (Sim/Não): "`.

A variável `jogar` começa com o valor `"Sim"` e o ciclo `while` permite repetir o jogo enquanto o utilizador responder `"Sim"`. Quando responder `"Não"`, o programa termina e apresenta a mensagem `"Obrigado por jogar!"`.

### Estruturas utilizadas

Neste programa utilizei as estruturas abordadas nas aulas:

* `def` para criar a função `corrida()`;
* `if`, `elif` e `else` para tomar as decisões;
* `while` para repetir as jogadas, validar os valores e permitir jogar novamente;
* `input()` para receber as escolhas e jogadas do utilizador;
* `print()` para apresentar mensagens;
* variáveis para guardar o total, as jogadas e o estado do jogo;
* operações aritméticas para calcular as jogadas do computador através das estratégias `11 - jogada_utilizador` e `12 - jogada_utilizador`.

---

## Lista de resultados

- [Jogo "Corrida para o 100"](TPC3.py)

