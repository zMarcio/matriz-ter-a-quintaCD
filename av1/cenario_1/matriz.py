class Matriz:
    def __init__(self,rows,cols,elements):
        if rows * cols != len(elements):
            return print("Dimensão da matriz não corresponde ao número de elementos")
        self.numRows = rows 
        self.numCols = cols
        self.listElements = elements
        self.matriz = []
        self.i = 0
        
    def buildMatriz(self):
        for p1 in range(self.numRows):
            list = []
            for p2 in range(self.numCols):
                list.append(self.listElements[self.i])
                self.i += 1
            self.matriz.append(list) 
        return self.matriz
        
    
    def getMatriz(self):
        return self.matriz

    def getIndiceMatriz(self, i , j):
        if i < 0 or (i - 1) > self.numRows or j < 0 or (j - 1) > self.numCols:
            return print("Índice fora da matriz")
        return self.matriz[i][j]
    
    def setIndiceMatriz(self, i, j, value):
        if i < 0 or (i - 1) > self.numRows or j < 0 or (j - 1) > self.numCols:
            return print("Índice fora da matriz")
        self.matriz[i][j] = value
