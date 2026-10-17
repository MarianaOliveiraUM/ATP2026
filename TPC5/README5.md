# TPC5

## Índice

- [Dados pessoais](#dados-pessoais)
- [Resumo](#resumo)
- [Lista de resultados](#lista-de-resultados)

---

## Dados pessoais

**Nome:** Mariana Veloso Oliveira  
**ID:** a115027 

<img src="foto5.jpg" alt="Foto do autor" width="100">

---

## Resumo
# TPC5: Aplicação para gestão de alunos

## Resumo

### Descrição

Este programa consiste numa aplicação em Python para a gestão de uma turma de alunos. 

Cada aluno é representado por um tuplo com três elementos: o nome, o ID e uma lista com as notas do TPC, do projeto e do teste. A turma é representada por uma lista que contém os vários alunos.

A aplicação utiliza uma variável interna chamada `turma`, onde ficam guardados os alunos da turma que está a ser utilizada. Desta forma, é possível realizar várias operações sobre a mesma turma sem ter de executar novamente o programa.

### Funcionamento do programa

Quando o programa começa, é apresentado um menu com as opções disponíveis:

- **(1) Criar uma turma** — cria uma nova turma vazia.
- **(2) Inserir um aluno na turma** — permite introduzir o nome, o ID e as notas de um aluno.
- **(3) Listar a turma** — apresenta os dados de todos os alunos da turma.
- **(4) Consultar um aluno por ID** — procura um aluno através do seu ID e apresenta os seus dados.
- **(8) Guardar a turma em ficheiro** — guarda os dados dos alunos num ficheiro de texto.
- **(9) Carregar uma turma dum ficheiro** — lê os dados guardados num ficheiro e recupera a turma.
- **(0) Sair da aplicação** — termina o programa.

Depois de executar a operação escolhida, o programa volta a apresentar o menu, permitindo ao utilizador continuar a trabalhar com a turma.

### Criação da turma

Na opção 1, utilizei a função `criarTurma()` para criar uma nova turma.

Inicialmente, a variável `turma` recebe uma lista vazia:

`turma = []`

Esta lista vai guardar os alunos que forem inseridos posteriormente. Depois, o programa apresenta uma mensagem a confirmar que a turma foi criada com sucesso.

No final, a função devolve a lista através de `return turma`, permitindo guardar a turma criada na variável `turma` principal do programa.

Sempre que esta opção é selecionada, é criada uma nova turma vazia, substituindo a turma que estava guardada anteriormente.

### Inserção de um aluno

Na opção 2, utilizei a função `inserirAluno(turma)` para adicionar um aluno à turma existente.

Primeiro, o programa pede ao utilizador o nome e o ID do aluno. De seguida, são chamadas três funções para ler as respetivas notas:

- `lerNotatpc()` — lê a nota do TPC.
- `lerNotaproj()` — lê a nota do projeto.
- `lerNotateste()` — lê a nota do teste.

Em cada uma destas funções, utilizei um ciclo `while` para verificar se a nota introduzida está entre 0 e 200, inclusive. Se o valor estiver fora deste intervalo, o programa pede novamente a nota até ser introduzido um valor válido.

Depois de recolher os dados, as três notas são guardadas numa lista:

`notas = [notaTPC, notaProj, notaTeste]`

De seguida, é criado o tuplo que representa o aluno:

`aluno = (nome, id, notas)`

Este tuplo é acrescentado à turma através de `turma.append(aluno)`.

No final, o programa apresenta uma mensagem a confirmar que o aluno foi inserido e devolve a turma atualizada.

### Listagem da turma

Na opção 3, utilizei a função `listarTurma(turma)` para apresentar os alunos existentes na turma.

Primeiro, o programa verifica se a turma está vazia através de `len(turma) == 0`. Se não existir nenhum aluno, é apresentada a mensagem:

`A turma está vazia!`

Caso contrário, o programa apresenta o título "Lista de Alunos:" e percorre a turma utilizando um ciclo `for`.

Para cada aluno, são obtidos o nome, o ID e a lista das notas. Estes dados são depois apresentados no monitor, permitindo consultar a informação de todos os alunos inseridos.

No final, a função devolve a turma.

### Consulta de um aluno por ID

Na opção 4, utilizei a função `idAluno(turma)` para procurar um aluno através do seu ID.

Primeiro, o programa pede ao utilizador que introduza o ID do aluno que pretende consultar.

Depois, utilizei a variável `i`, que começa em 0, para percorrer a turma através de um ciclo `while`. A variável `encontrado` começa com o valor `False` e serve para indicar se o aluno foi encontrado.

Em cada repetição, o programa compara o ID introduzido com o ID do aluno que se encontra na posição `i` da turma.

Se os IDs forem iguais, o aluno é guardado na variável `aluno_encontrado` e são apresentados o nome, o ID e as três notas. Nesse caso, a variável `encontrado` passa para `True`, fazendo com que a procura termine.

Se o ciclo terminar sem encontrar o aluno, o programa apresenta a mensagem:

`Aluno não encontrado.`

No final, a função devolve o aluno encontrado. Se não existir nenhum aluno com o ID indicado, devolve um tuplo vazio, que foi o valor inicial da variável `aluno_encontrado`.

### Guardar a turma em ficheiro

Na opção 8, utilizei a função `guardarTurma(turma)` para guardar os dados da turma num ficheiro de texto chamado `turma.txt`.

Para isso, o ficheiro é aberto no modo de escrita, através de:

`file = open("turma.txt", "w")`

Depois, o programa percorre a turma com um ciclo `for` e obtém o nome, o ID e as notas de cada aluno.

Os dados de cada aluno são escritos numa linha do ficheiro, separados pelo símbolo `#`. A informação guardada inclui o nome, o ID, a nota do TPC, a nota do projeto e a nota do teste.

Para escrever os dados, utilizei a instrução:

`file.write(f"{nome}#{id}#{notas[0]}#{notas[1]}#{notas[2]}\n")`

O símbolo `\n` permite que cada aluno fique registado numa linha diferente.

No final, o ficheiro é fechado através de `file.close()` e o programa apresenta uma mensagem a confirmar que a turma foi guardada com sucesso.

Como o ficheiro é aberto no modo `"w"`, os dados anteriores desse ficheiro são substituídos pelos dados da turma que está a ser guardada.

### Carregar uma turma de um ficheiro

Na opção 9, utilizei a função `carregarTurma()` para recuperar uma turma guardada anteriormente no ficheiro `turma.txt`.

Primeiro, é criada uma lista vazia para guardar os alunos que vão ser recuperados:

`turma = []`

Depois, o ficheiro é aberto no modo de leitura, através de:

`file = open("turma.txt", "r")`

O programa percorre o ficheiro linha a linha, utilizando um ciclo `for`. Em cada linha, os dados são separados através do método `split("#")`, utilizando o símbolo `#` como separador.

A partir da lista de dados obtida, são recuperados o nome e o ID do aluno, bem como as três notas.

Como as notas foram guardadas no ficheiro como texto, utilizo `float()` para voltar a convertê-las em números.

De seguida, é criada a lista com as notas e reconstruído o tuplo que representa o aluno:

`notas = [notaTPC, notaProj, notaTeste]`

`aluno = (nome, id, notas)`

Cada aluno recuperado é acrescentado à nova turma através de `turma.append(aluno)`.

No final, o ficheiro é fechado e a função devolve a turma reconstruída. Assim, os dados guardados podem voltar a ser utilizados pelo programa sem ser necessário introduzir novamente todos os alunos.

Quando o utilizador seleciona esta opção no menu, a turma carregada substitui a turma que estava anteriormente guardada na variável `turma`. O programa apresenta uma mensagem de confirmação e mostra os alunos recuperados através da função `listarTurma(turma)`.

### Menu e repetição do programa

A aplicação utiliza um ciclo `while` para manter o menu em funcionamento enquanto o utilizador não escolher a opção 0.

A variável `opcao` guarda a opção introduzida pelo utilizador. Dependendo do valor escolhido, o programa utiliza as condições `if`, `elif` e `else` para executar a operação correspondente.

Por exemplo, quando o utilizador escolhe a opção 2, o programa verifica se já foi criada uma turma. Se existir uma turma, é chamada a função `inserirAluno(turma)`. Caso contrário, é apresentada a mensagem:

`É necessário criar uma turma primeiro!`

Para controlar este funcionamento, utilizei as variáveis `turma_criada` e `turma_guardada`.

A variável `turma_criada` indica se já foi criada ou carregada uma turma. Desta forma, as opções de inserção, listagem, consulta e gravação só podem ser utilizadas depois de existir uma turma.

A variável `turma_guardada` é atualizada quando a turma é guardada ou carregada, e passa para `False` quando é criada uma nova turma. No código atual, esta variável não é utilizada para controlar nenhuma condição do menu, servindo apenas para registar esse estado.

Quando o utilizador escolhe a opção 0, o programa apresenta a mensagem:

`Aplicação encerrada.`

Se for introduzida uma opção que não existe no menu, o programa apresenta uma mensagem de erro e volta a pedir uma opção.


---

## Lista de resultados

- [Aplicação para gestão de alunos](TPC5.py)
- [Exemplo de turma de 5 alunos](turma.txt)