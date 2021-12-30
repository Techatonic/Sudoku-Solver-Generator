import solve
import numpy as np
import random
import copy

blankGrid = [[-1 for i in range(9)] for j in range(9)]

def PrintSudoku(grid):
    for x in range(len(grid)):
        if x % 3 == 0:
                print("- "*13)
        for y in range(len(grid)):    
            if y % 3 == 0:
                print("|", end="")
            
            if grid[x][y] == -1:
                if y%3 == 0:
                    print(" ", end="")
                else:
                    print("   ", end="")
            else:
                if y%3 == 0:
                    print(grid[x][y], end="")
                else:
                    print(" ", grid[x][y], end="")

            if y == 8:
                print("|")
    print("- "*13)



def Generate(grid, currPos=[0,0]):
    currGrid = copy.deepcopy(grid)
    possibilities = [i for i in range(1, 10)]
    while len(possibilities) > 0:
        choice = random.choice(possibilities)
        currGrid[currPos[0]][currPos[1]] = choice
        if not solve.ValidGrid(currGrid):
            possibilities.remove(choice)
            continue
        
        nextPos = None

        if currPos[1] < 8:
            nextPos = [currPos[0], currPos[1]+1]
        elif currPos[0] < 8:
            nextPos = [currPos[0]+1, 0]
        else:
            return (True, currGrid)
        
        result = Generate(currGrid, nextPos)
        if result[0] == True:
            return result
        else:
            possibilities.remove(choice)
            continue
    
    return (False, [])


def RemoveCells(grid, possibilities = [[[i, j] for i in range(9)] for j in range(9)], depth=0):
    currGrid = copy.deepcopy(grid)

    while len(possibilities) > 0:
        choiceRow = random.choice(possibilities)
        choiceRowIndex = possibilities.index(choiceRow)
        choice = random.choice(choiceRow)
        currGrid[choice[0]][choice[1]] = -1
        solutionsFound = solve.Solve(copy.deepcopy(currGrid))
        
        if solutionsFound == 1:
            del possibilities[choiceRowIndex][choiceRow.index(choice)]
            if possibilities[choiceRowIndex] == []:
                del possibilities[choiceRowIndex]

            result = RemoveCells(currGrid, possibilities, depth+1)
            if result[0] == False:
                return (currGrid, 80-depth)
            else:
                return result
        
        return (False, 0)

    return (currGrid, 80-depth)
    


filledGrid = Generate(blankGrid)[1]

result = RemoveCells(filledGrid)
sudoku = result[0]
depth = result[1]

#print("\n\n\n", np.matrix(sudoku))
PrintSudoku(sudoku)
print("Number of cells given: ", depth)