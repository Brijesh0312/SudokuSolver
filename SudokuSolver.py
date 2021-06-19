import numpy as np
puzzle=[[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9]]

print("Input Sudoku-:")
print(np.matrix(puzzle))

def possible(y,x,n):
    global puzzle
    for i in range(9):
        if(puzzle[y][i]==n):
            return False
    for i in range(9):
        if(puzzle[i][x]==n):
            return False
    x_box=(x//3)*3
    y_box=(y//3)*3
    for i in range(3):
        for j in range(3):
            if(puzzle[y_box+i][x_box+j]==n):
                return False
    return True

def solve():
    global puzzle
    for y in range(9):
        for x in range(9):
            if puzzle[y][x]==0:
                for n in range(1,10):
                    if(possible(y,x,n)):
                        puzzle[y][x]=n
                        solve()
                        puzzle[y][x]=0
                return

    print(np.matrix(puzzle))
print("Solved sudoku is-:")
solve()