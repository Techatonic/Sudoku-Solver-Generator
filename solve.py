import numpy as np
import copy

solutionsFound = 0


def ValidGrid(sudoku):
    for row in sudoku:
        newrow = list(filter(lambda x: x!= -1, row))
        if len(newrow) != len(set(newrow)):
            return False
    for col in range(len(sudoku)):
        column = [sudoku[i][col] for i in range(len(sudoku))]
        newcol = list(filter(lambda x: x!=-1, column))
        if len(newcol) != len(set(newcol)):
            return False
    
    for x in range(3):
        for y in range(3):
            values = []
            for i in range(3*x, 3*x+3):
                for j in range(3*y, 3*y+3):
                    values.append(sudoku[i][j])
            newvalues = list(filter(lambda x: x!=-1, values))
            if len(newvalues) != len(set(newvalues)):
                return False
    return True


def Solve(sudoku, stackLevel=0):
    global solutionsFound
    if stackLevel == 0:
        solutionsFound = 0
    nextEmpty = None
    for row in range(len(sudoku)):
        for col in range(len(sudoku)):
            if sudoku[row][col] == -1:
                nextEmpty = [row, col]
                break
        if nextEmpty!= None:
            break
    
    if nextEmpty == None:
        #print(np.matrix(sudoku))
        solutionsFound += 1
        return solutionsFound

    for attempt in range(1, 10):
        sudoku[nextEmpty[0]][nextEmpty[1]] = attempt
        
        if not ValidGrid(sudoku):
            continue
        
        
        Solve(copy.deepcopy(sudoku), stackLevel+1)    
    
    return solutionsFound
