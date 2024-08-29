from av1.cenario_1.matriz import Matriz
from av1.cenario_2.vector import Vector


# Testes de Matriz caminho feliz

matriz = Matriz(2, 2, [1, 2, 3, 4])
print(matriz.getIndiceMatriz(1, 1))
matriz.setIndiceMatriz(1, 1, 9)
print(matriz.getIndiceMatriz(1, 1))
print(matriz.getMatriz())

# Testes de Matriz caminho infeliz

matriz = Matriz(2, 2, [1, 2, 3, 4])
print(matriz.getIndiceMatriz(3, 3)) # Índice fora da matriz
print(matriz.setIndiceMatriz(3, 3, 9)) # Índice fora da matriz
print(matriz.getMatriz())


# Testes de Vetor caminho feliz

vetor = Vector(3, [1, 2, 3])
print(vetor.getIndexVector(1))
vetor.setIndexVector(1, 9)
print(vetor.getIndexVector(1))

# Testes de Vetor caminho infeliz

vetor = Vector(3, [1, 2])
print(vetor.getIndexVector(11)) # Índice fora do vetor
print(vetor.setIndexVector(10, 9)) # Índice fora do vetor