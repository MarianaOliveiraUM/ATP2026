# TPC6

## Índice

- [Dados pessoais](#dados-pessoais)
- [Resumo](#resumo)
- [Lista de resultados](#lista-de-resultados)

---

## Dados pessoais

**Nome:** Mariana Veloso Oliveira  
**ID:** a115027 

<img src="foto6.jpg" alt="Foto do autor" width="120">

---

## Resumo

### Descrição

Este programa consiste numa aplicação para criar e trabalhar com tabelas meteorológicas. Cada registo contém uma data, a temperatura mínima, a temperatura máxima e a precipitação de um determinado dia.

A tabela é guardada na variável `tabMeteo`, que contém uma lista de registos. Cada registo é constituído por um tuplo com a data e os restantes valores meteorológicos.

### Funcionamento do programa

Quando o programa começa, é apresentado um menu com as seguintes opções:

- **(1) Criar uma tabela meteorológica** — permite introduzir os dados de vários dias.
- **(2) Mostrar a tabela** — apresenta os dados meteorológicos guardados.
- **(3) Calcular as temperaturas médias** — calcula a média entre a temperatura mínima e a máxima de cada dia.
- **(4) Calcular a temperatura mínima mais baixa** — identifica o valor mínimo de temperatura registado na tabela.
- **(5) Calcular as amplitudes térmicas** — calcula a diferença entre a temperatura máxima e a mínima de cada dia.
- **(6) Encontrar o dia com maior precipitação** — identifica a data e o valor máximo de precipitação.
- **(7) Mostrar os dias com precipitação acima de um limite** — apresenta os dias em que a precipitação é superior ao limite introduzido.
- **(8) Calcular o maior período consecutivo abaixo de um limite** — determina o maior número de dias consecutivos com precipitação inferior ao valor indicado.
- **(9) Desenhar os gráficos** — representa graficamente as temperaturas e a precipitação.
- **(10) Guardar a tabela num ficheiro** — guarda os registos meteorológicos num ficheiro de texto.
- **(11) Carregar uma tabela de um ficheiro** — permite selecionar um ficheiro com dados meteorológicos guardados.
- **(0) Sair** — termina a aplicação.

O programa utiliza um ciclo `while` para voltar a apresentar o menu após cada operação. As condições `if`, `elif` e `else` permitem executar a funcionalidade correspondente à opção escolhida.

### Criação e apresentação da tabela

Para criar uma tabela, utilizei a função `criarTabela()`. O programa pergunta quantos dias o utilizador pretende inserir e, para cada dia, pergunta o ano, o mês, o dia, as temperaturas mínima e máxima e a precipitação.

Utilizei ciclos `while` para verificar se o mês está entre 1 e 12 e se o dia está entre 1 e 31. Cada registo é acrescentado à lista através de `append()`.

Para apresentar os dados, criei as funções `mostrarData(data)` e `mostrarTabela(tabMeteo)`. A primeira transforma a data guardada num tuplo no formato dia/mês/ano, enquanto a segunda percorre a tabela e apresenta os valores meteorológicos de cada dia.

### Cálculos meteorológicos

Para realizar os cálculos pedidos no enunciado, criei funções independentes, que recebem a tabela meteorológica e devolvem os resultados.

Na função `medias(tabMeteo)`, calculei a média de cada dia através da soma das temperaturas mínima e máxima, dividida por dois. Na função `minMin(tabMeteo)`, percorri a tabela para encontrar a temperatura mínima mais baixa.

Na função `amplTerm(tabMeteo)`, calculei a amplitude térmica de cada dia, subtraindo a temperatura mínima à máxima. Na função `maxChuva(tabMeteo)`, procurei o dia com maior precipitação, guardando a respetiva data e o valor.

A função `diasChuvosos(tabMeteo, p)` permite identificar os dias em que a precipitação é superior a um limite introduzido pelo utilizador. Por sua vez, `maxPeriodoCalor(tabMeteo, p)` calcula o maior número de dias consecutivos com precipitação abaixo desse limite, utilizando as variáveis `atual` e `maior` para contar os dias consecutivos e guardar o máximo encontrado.

Nas opções do menu, os resultados devolvidos pelas funções são apresentados através de `print()`. Antes de realizar as operações, o programa também verifica se a tabela contém registos, apresentando uma mensagem caso esteja vazia.

### Gráficos

Para desenhar os gráficos, utilizei a biblioteca `matplotlib.pyplot`, importada através de `import matplotlib.pyplot as plt`.

Na função `grafTabMeteo(t)`, criei listas para guardar as datas, as temperaturas mínimas, as temperaturas máximas e os valores de precipitação. Depois, utilizei `plt.plot()` para representar os dados em gráficos, com as datas no eixo horizontal e os valores meteorológicos no eixo vertical.

Os gráficos incluem legendas, identificação dos eixos e rotação das datas, para facilitar a leitura dos resultados.

### Guardar e carregar ficheiros

Para guardar os dados, criei a função `guardaTabMeteo(t, fnome)`. Esta função abre um ficheiro em modo de escrita e guarda cada registo numa linha, separando os valores pelo símbolo `|`. A data é escrita no formato ano-mês-dia, com os seus componentes separados por hífenes.

Para recuperar os dados, criei a função `carregaTabMeteo(fnome)`. Esta função abre o ficheiro em modo de leitura, utiliza `split()` para separar os campos e converte os valores para os tipos adequados, reconstruindo a data como um tuplo e os restantes valores como números.

Na aplicação, o utilizador indica o nome do ficheiro a utilizar. A variável `ficheirosGuardados` permite registar os nomes dos ficheiros guardados durante a execução do programa.

### Estruturas utilizadas

Neste trabalho utilizei principalmente:

- `def` e `return` para criar funções e devolver resultados;
- `if`, `elif` e `else` para tomar decisões;
- `while` e `for` para repetir operações e percorrer os registos;
- `input()` e `print()` para interagir com o utilizador;
- listas e tuplos para organizar os dados meteorológicos;
- `append()` para adicionar elementos às listas;
- `len()` para verificar se existem registos;
- `open()`, `write()`, `split()` e `close()` para trabalhar com ficheiros;
- `matplotlib.pyplot` para construir os gráficos.


---

## Lista de resultados

- [Aplicação para tabelas metereológicas](TPC6.py)