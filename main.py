import numpy as np
import copy
import time

puzzle = [
    [ 2, -1, -1,  3,  6, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1,  3, -1],
    [-1, -1,  3,  2,  4, -1, -1,  9, -1],
    [-1,  2,  7, -1, -1, -1, -1,  1, -1],
    [-1,  3,  1,  6, -1, -1,  9, -1, -1],
    [ 6, -1,  9,  8,  1, -1,  2, -1,  7],
    [ 9,  6,  2,  4, -1, -1,  3, -1, -1],
    [ 1, -1,  5, -1,  3, -1,  4,  2, -1],
    [ 3,  7,  4, -1,  8,  2,  5,  6, -1]
]

sortedLine = [i for i in range(1, 10)]

#print(np.matrix(puzzle), "\n")



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


def Solve(sudoku, stackLevel):
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
        return True

    for attempt in range(1, 10):
        sudoku[nextEmpty[0]][nextEmpty[1]] = attempt
        
        if not ValidGrid(sudoku):
            continue
        
        
        finished = Solve(copy.deepcopy(sudoku), stackLevel+1)
        if finished:
            return True
    
    
    return False


startTime = time.time()
Solve(puzzle, 0)
print("Time Taken: ", time.time()-startTime)



# Backtracking - 0.02 seconds