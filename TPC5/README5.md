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

### Descrição

Este programa consiste numa aplicação em Python para gerir uma turma de alunos. 

Cada aluno é representado por um tuplo com o nome, o ID e uma lista com três notas: TPC, projeto e teste. A turma é representada por uma lista que contém os vários alunos.

O programa utiliza a variável `turma` para guardar os alunos com que está a trabalhar. Quando é criada uma nova turma ou carregada uma turma de um ficheiro, o conteúdo anterior desta variável é substituído.

### Funcionamento do programa

Quando o programa começa, é apresentado um menu com as seguintes opções:

- **(1) Criar uma turma** — cria uma turma vazia.
- **(2) Inserir um aluno na turma** — pede os dados do aluno e acrescenta-o à turma.
- **(3) Listar a turma** — apresenta os dados dos alunos.
- **(4) Consultar um aluno por ID** — procura um aluno através do seu ID.
- **(8) Guardar a turma em ficheiro** — guarda os dados no ficheiro `turma.txt`.
- **(9) Carregar uma turma dum ficheiro** — recupera os dados guardados.
- **(0) Sair da aplicação** — termina o programa.

### Criação da turma

Na opção 1, utilizei a função `criarTurma()`.

A variável `turma` começa por receber uma lista vazia, através de `turma = []`. Esta lista vai ser utilizada para guardar os alunos inseridos posteriormente.

No final, a função devolve a lista com `return turma`, permitindo que a turma criada fique guardada na variável `turma` principal do programa.

### Inserção de um aluno

Na opção 2, utilizei a função `inserirAluno(turma)`.

Primeiro, o programa pede o nome e o ID do aluno. Para ler as três notas, criei as funções `lerNotatpc()`, `lerNotaproj()` e `lerNotateste()`.

Em cada uma destas funções, a variável `nota` guarda o valor introduzido pelo utilizador. Um ciclo `while` verifica se a nota é inferior a 0 ou superior a 200. Se alguma destas condições se verificar, o programa pede novamente a nota.

Depois de obter os valores, criei a lista `notas = [notaTPC, notaProj, notaTeste]` e o tuplo `aluno = (nome, id, notas)`. Por fim, utilizei `turma.append(aluno)` para acrescentar o aluno à lista da turma.

### Listagem da turma

Na opção 3, utilizei a função `listarTurma(turma)`.

Comecei por verificar se a turma estava vazia, utilizando `len(turma) == 0`. Se não existirem alunos, o programa apresenta uma mensagem a indicar que a turma está vazia.

Caso contrário, utilizei um ciclo `for` para percorrer os alunos da turma. Em cada repetição, as posições do tuplo permitem obter o nome (`aluno[0]`), o ID (`aluno[1]`) e as notas (`aluno[2]`). Estes dados são depois apresentados através de `print()`.

### Consulta de um aluno por ID

Na opção 4, utilizei a função `idAluno(turma)`.

Depois de pedir o ID ao utilizador, utilizei a variável `i`, inicializada com 0, para percorrer a turma através de um ciclo `while`.

A variável `encontrado` começa com o valor `False` e passa para `True` quando o ID introduzido coincide com o ID de um dos alunos. Nesse caso, os dados do aluno são guardados na variável `aluno_encontrado` e apresentados no monitor.

O ciclo continua enquanto ainda existirem alunos por verificar e nenhum aluno tiver sido encontrado. Se a procura terminar sem encontrar o ID, o programa apresenta a mensagem "Aluno não encontrado.". Caso contrário, a função devolve o aluno encontrado. 

### Guardar a turma em ficheiro

Na opção 8, utilizei a função `guardarTurma(turma)` para guardar os dados no ficheiro `turma.txt`.

O ficheiro é aberto no modo de escrita, através de `open("turma.txt", "w")`. Depois, um ciclo `for` percorre a turma e, em cada repetição, as informações do aluno são separadas nas variáveis `nome`, `id` e `notas`.

Utilizei `file.write()` para escrever o nome, o ID e as três notas numa única linha, separando os valores com o símbolo `#`. O `\n` permite que o aluno seguinte seja escrito numa nova linha.

No final, utilizei `file.close()` para fechar o ficheiro e o programa apresenta uma mensagem a confirmar que a turma foi guardada. Como o ficheiro é aberto no modo `"w"`, os dados que já existiam nesse ficheiro são substituídos.

### Carregar uma turma de um ficheiro

Na opção 9, utilizei a função `carregarTurma()` para recuperar os alunos guardados anteriormente.

Primeiro, criei uma lista vazia com `turma = []` e abri o ficheiro no modo de leitura, através de `open("turma.txt", "r")`.

Depois, um ciclo `for` percorre cada linha do ficheiro. Utilizei `line.split("#")` para separar os dados, guardando-os na variável `dados`.

Através das posições desta lista, recupero o nome, o ID e as três notas. Como as notas foram guardadas no ficheiro como texto, utilizei `float()` para as converter novamente em números.

De seguida, criei a lista `notas` e reconstruí o tuplo `aluno`, acrescentando-o à turma com `turma.append(aluno)`.

No final, o ficheiro é fechado e a função devolve a turma reconstruída. No menu, a turma devolvida substitui a que estava anteriormente guardada na variável `turma`, sendo depois apresentada através da função `listarTurma(turma)`.

### Menu e repetição do programa

Para manter o menu em funcionamento, utilizei um ciclo `while` que se repete enquanto `opcao != "0"`.

A variável `opcao` guarda a escolha do utilizador. As condições `if`, `elif` e `else` permitem executar a função correspondente à opção escolhida.

Criei também a variável `turma_criada`, que começa com o valor `False` e passa para `True` quando é criada ou carregada uma turma. Antes de inserir, listar, consultar ou guardar alunos, o programa verifica esta variável. Se ainda não existir uma turma, apresenta uma mensagem a informar que é necessário criá-la primeiro.

A variável `turma_guardada` é atualizada quando a turma é guardada ou carregada e passa para `False` quando é criada uma nova turma. No código atual, esta variável não é utilizada nas condições do menu.

Quando o utilizador escolhe a opção 0, o programa apresenta a mensagem "Aplicação encerrada.". Se introduzir uma opção que não existe, recebe uma mensagem de erro e pode voltar a escolher.


---

## Lista de resultados

- [Aplicação para gestão de alunos](TPC5.py)
- [Exemplo de turma de 5 alunos](turma.txt)
