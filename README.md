# Matriz-ter-a-quintaCD

Este projeto tem como objetivo implementar uma representação de matrizes e vetores, bem como operações algébricas elementares, eliminação gaussiana e o algoritmo de Gauss-Jordan, utilizando uma das seguintes linguagens de programação: JavaScript, Java, C, C++, C#, Python, entre outras. O escopo do projeto inclui as seguintes implementações:

## Classe Matrix
A classe `Matrix` é responsável por representar uma matriz e suas operações. Ela inclui os seguintes métodos:

- **Construtor da classe Matrix:** 
  - Recebe como parâmetros a quantidade de linhas (`rows`), colunas (`cols`) e um array com os elementos da matriz (`elements`).
  - Exemplo de assinatura: `constructor(rows, cols, elements)`.
  
- **Método get:**
  - Retorna o valor armazenado em uma posição específica da matriz.
  - Exemplo de assinatura: `get(i, j)` onde `i` é o índice da linha e `j` é o índice da coluna.
  
- **Método set:**
  - Atribui um valor a uma posição específica da matriz.
  - Exemplo de assinatura: `set(i, j, value)` onde `i` é o índice da linha, `j` é o índice da coluna e `value` é o valor a ser armazenado.

## Classe Vector
A classe `Vector` representa um vetor e suas operações, com os seguintes métodos:

- **Construtor da classe Vector:** 
  - Recebe como parâmetros a dimensão do vetor (`dim`) e um array com os elementos do vetor (`elements`).
  - Exemplo de assinatura: `constructor(dim, elements)`.
  
- **Método get:**
  - Retorna o valor armazenado em uma posição específica do vetor.
  - Exemplo de assinatura: `get(i)` onde `i` é o índice do elemento.
  
- **Método set:**
  - Atribui um valor a uma posição específica do vetor.
  - Exemplo de assinatura: `set(i, value)` onde `i` é o índice do elemento e `value` é o valor a ser armazenado.

## Classe LinearAlgebra
A classe `LinearAlgebra` implementa operações algébricas e outros algoritmos, incluindo:

- **Método transpose:** 
  - Retorna a matriz ou vetor transposto.
  - Exemplo de assinatura: `transpose(a)` onde `a` é a matriz ou vetor a ser transposto.

- **Método sum:** 
  - Soma duas matrizes ou dois vetores.
  - Exemplo de assinatura: `sum(a, b)` onde `a` e `b` são as matrizes ou vetores a serem somados.

- **Método times:** 
  - Multiplica elemento a elemento duas matrizes ou vetores, ou um escalar com uma matriz.
  - Exemplo de assinatura: `times(a, b)` onde `a` pode ser um escalar, matriz ou vetor, e `b` é uma matriz ou vetor.

- **Método dot:** 
  - Realiza a multiplicação de duas matrizes.
  - Exemplo de assinatura: `dot(a, b)` onde `a` e `b` são as matrizes a serem multiplicadas.

- **Método gauss:** 
  - Realiza a eliminação gaussiana em uma matriz.
  - Exemplo de assinatura: `gauss(a)` onde `a` é a matriz a ser processada.

- **Método solve:** 
  - Resolve um sistema de equações lineares representado por uma matriz aumentada.
  - Exemplo de assinatura: `solve(a)` onde `a` é a matriz aumentada a ser resolvida.

## Tratamento de Erros
Todas as funções devem implementar o tratamento de erros. Fique à vontade para adicionar métodos adicionais que ajudem a organizar o código e melhorar as verificações de erro. Propostas de melhorias e ideias são bem-vindas!
