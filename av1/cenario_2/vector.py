# Classe Vector

class Vector:
    def __init__(self,dim,elements):
        if dim != len(elements):
            return print("Dimensão do vetor não corresponde ao número de elementos")
        self.dim = dim
        self.elements = elements
        
    def getIndexVector(self,i):
        if i < 0 or (i - 1) > self.dim:
            return print("Índice fora do vetor")
        return self.elements[i]
    
    def setIndexVector(self, i, value):
        if i < 0 or (i - 1) > self.dim:
            return print("Índice fora do vetor")
        return self.elements[i].append(value)

