# TPC1

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
### 1- Maze: nível 10
O personagem move-se em frente ao longo do caminho e vai verificando se pode virar à direita e de seguida à esquerda. Sempre que encontra uma possibilidade de virar, faz a mudança de direção. Se não puder virar, continua em frente. Quando encontra um obstáculo e não consegue avançar, verifica, neste caso, se pode virar primeiro à esquerda e, caso não seja possível, à direita. 
### 2- Turtle: nível 10
Para desenhar o barco, desenhei linha por linha e fui ajustando as medidas e os ângulos por tentativa e erro, até ficar semelhante ao da imagem proposta. Primeiro, mudei a grossura da linha para o traço ficar mais forte (set width to 3) e desenhei o mastro e a base do barco, virando a tartaruga nos cantos para fazer o formato inclinado. Posteriormente, levantei a caneta (pen up) para mover a tartaruga sem rabiscar e pousei-a (pen down) para desenhar as linhas que ficam no interior do barco. Por fim, subi a tartaruga para desenhar os dois triângulos grandes das velas e terminei com o triângulo pequeno da bandeira no topo.

Já para o sol, usei dois ciclos para facilitar. O primeiro repete 36 vezes o avanço de 4 unidades a virar 10° para a direita, até somar os 360° e fechar o círculo do meio. Depois, levantei a caneta (pen up) para afastar a tartaruga do centro sem fazer riscos e rodei 8 vezes um segundo ciclo para os raios. Em cada volta, ela avança sem desenhar para dar o espaço, baixa a caneta (pen down) para fazer o raio de 15 unidades, e volta para trás com a caneta levantada para virar 45° (360° ÷ 8) e passar ao raio seguinte de forma correta.

Quanto às nuvens, fui combinando vários ciclos pequenos de repetição para fazer os arcos de cada parte arredondada, fazendo uma linha em baixo para fechar o seu formato. Fui testando os ângulos e o número de passos em cada arco até conseguir a forma mais aproximada de cada nuvem.

Para a criação das ondas, utilizei uma estrutura de ciclos dentro de ciclos, um ciclo interno desenha o arco de um semicírculo e o ciclo externo repete essa forma 7 vezes para construir uma linha completa do mar. Para o meu desenho ficar ainda mais semelhante ao que era pretendido, optei por fazer um círculo preto em cada extremidade da onda. Depois, repeti o mesmo processo para a onda de baixo.

Por fim, para fazer o ponto, mudei a cor para branco e usei um ciclo de 360 repetições. Em cada passo, a tartaruga avança, levanta a caneta (pen up) para recuar a mesma distância e roda 1° com a caneta em baixo (pen down), preenchendo assim um pequeno círculo completo a toda a volta.

---

## Lista de resultados

- [Resultado final do exercício 1](resultadofinalexercício1.png)
- [Resolução do exercício 1](exercício1.png)
- [Resultado final do exercício 2](resultadofinalexercício2.png)
- [Resolução do exercício 2 (barco)](exercício2barco.png)
- [Resolução do exercício 2 (sol)](exercício2sol.png)
- [Resolução do exercício 2 (nuvens)](exercício2nuvens.png)
- [Resolução do exercício 2 (ondas)](exercício2ondas.png)
- [Resolução do exercício 2 (ponto)](exercício2ponto.png)
