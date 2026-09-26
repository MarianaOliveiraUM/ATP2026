# TPC2

## Índice

- [Dados pessoais](#dados-pessoais)
- [Resumo](#resumo)
- [Lista de resultados](#lista-de-resultados)

---

## Dados pessoais

**Nome:** Mariana Veloso Oliveira  
**ID:** a115027 

<img src="foto.jpg" alt="Foto do autor" width="100">

---

## Resumo

### Descrição

Este programa consiste num jogo de adivinhar um número entre 0 e 100, inclusive. O jogo tem duas modalidades diferentes: numa delas o computador escolhe o número e o utilizador tenta adivinhar, e na outra o utilizador pensa num número e o computador tenta descobri-lo. No final de cada jogo é apresentado o número de tentativas que foram necessárias para descobrir o número. Também é possível jogar novamente depois de terminar uma partida.

### Funcionamento do programa

Quando o programa começa, é apresentado um menu onde o utilizador pode escolher uma das duas modalidades:

* **Modalidade 1:** o computador escolhe um número aleatório entre 0 e 100 e o utilizador tenta adivinhar.
* **Modalidade 2:** o utilizador pensa num número entre 0 e 100 e o computador tenta adivinhar através das respostas dadas pelo utilizador.

Depois de escolher uma modalidade, o jogo continua até o número ser descoberto.

#### Modalidade 1

Na primeira modalidade, utilizei o comando "random" para permitir que o computador escolha um número aleatório: "numero = random.randint(0, 100)".
O utilizador vai introduzindo números e, depois de cada tentativa, o programa verifica se acertou.

Se o número introduzido for igual ao número pensado, aparece a mensagem "Acertou!". Mas se for menor, o programa indica que "O número que pensei é Maior" e se for maior, indica que "O número que pensei é Menor".

Para controlar a repetição das tentativas utilizei um ciclo "while", que continua enquanto a variável "acertou" tiver o valor "False".

Também foi criada uma variável chamada "tentativas", que começa em 0 e aumenta uma unidade sempre que o utilizador faz uma tentativa.

#### Modalidade 2

Na segunda modalidade, o utilizador pensa num número e o computador tenta adivinhá-lo. 

Comecei por definir: "menor = 0" e "maior = 100". Estas duas variáveis representam os limites entre os quais o número pode estar.

O computador calcula o seu palpite através de: "numero = (menor + maior) // 2". Desta forma, começa por escolher o número que está aproximadamente a meio do intervalo.

Depois, o utilizador responde com "Acertou","Maior" ou "Menor".
Se a resposta for "Maior", significa que o número pensado é maior que o palpite. Por isso, o limite inferior passa a ser: "menor = numero + 1". Se a resposta for "Menor", o limite superior passa a ser: "maior = numero - 1". Desta forma, o intervalo vai ficando cada vez mais pequeno até o computador encontrar o número.

Tal como na primeira modalidade, utilizei a variável "tentativas" para contar o número de palpites feitos pelo computador.

#### Repetição do jogo

Depois de terminar uma partida, o programa pergunta: "jogar = input("Quer jogar novamente? (Sim/Não): ")"

A variável "jogar" começa com o valor "Sim" e existe um "while" exterior que permite repetir o jogo enquanto o utilizador responder "Sim". Quando o utilizador responde "Não", o ciclo termina e aparece a mensagem: "Obrigado por jogar!"

### Estruturas utilizadas

Neste programa utilizei principalmente as estruturas que foram abordadas nas aulas:

* `def` para criar a função `"adivinha()"`;
* `if`, `elif` e `else` para tomar decisões;
* `while` para repetir as tentativas e permitir jogar várias vezes;
* `input()` para receber informações do utilizador;
* `print()` para apresentar mensagens;
* variáveis para guardar os valores necessários ao funcionamento do jogo;

Como queria que o computador gerasse um número aleatório na primeira modalidade, recorri a uma pequena pesquisa para perceber como poderia fazer isso, tendo optado por utilizar o `random.randint()`.

---

## Lista de resultados

- [Jogo "Adivinha o número"](TPC2.py)