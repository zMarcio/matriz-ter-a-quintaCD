class buildingMatriz:
    def __init__(self,rows,cols,elements):
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
        
    
    def get(self):
        return self.matriz




if __name__ == "__main__":
    build = buildingMatriz(2,2,[12,34,56,78])
    build.buildMatriz()
    print(build.get())