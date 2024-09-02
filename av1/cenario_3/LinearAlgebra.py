from typing import Union, List


class LinearAlgebra:
    
    def tranpose(element):
        transposeList = []
        indexValue = 0
        
        if len(element) ==  0 :
            return "Lista vazia"
        
        if isinstance(element[0], (int,float)):
            indexValue = len(element) - 1
            for i in range(len(element)):
                transposeList.append(element[indexValue])
            return transposeList
        
        elif isinstance(element[0], list):
            transposeList = []
            rows = len(element)
            cols = len(element[0])
            
            for j in range(cols):
                new_row = []
                for i in range(rows):
                    new_row.append(element[i][j])
                transposeList.append(new_row)
                
            return transposeList
        
        else:
            return "Elemento não é uma lista ou um número"
    
    
    
    def sum(a,b):
        sumList = []        
        
        # Verifica se as listas estão vazias
        if len(a) == 0 or len(b) == 0:
            return "Lista vazia"
        
        # Sum de lista
        elif isinstance(a[0], (int,float)) and isinstance(b[0], (int, float)):
            if len(a) != len(b):
                return "Listas de tamanhos diferentes"
            for i in range(len(a)):
                sumList.append(a[i] + b[i])
            return sumList
        
        # sum entre matrizes
        elif isinstance(a[0], list) and isinstance(b[0], list):
            if len(a) == len(b):
                listAux = []
                for i in range(len(a)):
                    
                    if len(a[i]) != len(b[i]):
                        return "Matrizes de tamanhos diferentes"
            
                    if  (len(a) == 0 and len(b) == 0) or (len(a[i]) == 0 and len(b[i]) == 0):
                        return "Matrizes vazia"          

                    for j in range(len(a[i])):
                        sumList.append(a[i][j] + b[i][j])
                    
                return sumList
            else:
                return 'As matrizes estão erradas'
            
            
    # A consertar
    
    
    # def times(a, b) :
    #     timesList = []
        
    #     if isinstance(a, (int, float)) and isinstance(b, (int, float)):
    #         return a * b
        
    #     if isinstance(a, (int, float)):
    #         if len(b) == 0:
    #             return "Lista vazia"
            
    #         if isinstance(b[0], list):  # Se 'b' é uma matriz
    #             for row in b:
    #                 timesList.append([a * element for element in row])
    #         else:  # Se 'b' é um vetor
    #             timesList = [a * element for element in b]
            
    #         return timesList
        
    #     if isinstance(b, (int, float)):
    #         if len(a) == 0:
    #             return "Lista vazia"
            
    #         if isinstance(a[0], list):  # Se 'a' é uma matriz
    #             for row in a:
    #                 timesList.append([b * element for element in row])
    #         else:  # Se 'a' é um vetor
    #             timesList = [b * element for element in a]
            
    #         return timesList
        
    #     if isinstance(a, list) and isinstance(b, list):
    #         if len(a) != len(b):
    #             return "Listas de tamanhos diferentes"
            
    #         if isinstance(a[0], list) and isinstance(b[0], list):  # Matrizes
    #             if len(a) != len(b) or any(len(row) != len(b_row) for row, b_row in zip(a, b)):
    #                 return "Matrizes de tamanhos diferentes"
    #             return [[a[i][j] * b[i][j] for j in range(len(a[i]))] for i in range(len(a))]
            
    #         elif all(isinstance(x, (int, float)) for x in a) and all(isinstance(x, (int, float)) for x in b):  # Vetores
    #             if len(a) != len(b):
    #                 return "Vetores de tamanhos diferentes"
    #             return [a[i] * b[i] for i in range(len(a))]

    #     return "Tipos incompatíveis"
    