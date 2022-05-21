import csv

def isInRange(grid):
    N = 9

    for i in range(0,N):
        for j in range(0,N):
            if((grid[i][j] <= 0) or
                (grid[i][j] > 9)):
                return False
    return True

def check(grid):
    N = 9

    if(isInRange(grid) == False):
        return False
    
    value = [False] * (N + 1)

    for i in range(0, N):
        for m in range(0,N+1):
            value[m] = False
        
        for j in range(0,N):
            Z = grid[i][j]

            if(value[Z] == True):
                return False
        value[Z] = True

    for i in range(0,N):
        for m in range(0,N+1):
            value[m] = False
        
        for j in range(0,N):
            Z = grid[j][i]

            if(value[Z] == True):
                return False
        value[m] = True

    for i in range(0,N-2,3):
        for j in range(0,N-2,3):
            for m in range(0,N+1):
                value[m] = False
            
            for k in range(0,3):
                for l in range(0,3):
                    X=i+k
                    Y=j+l
                    Z=grid[X][Y]

                    if(value[Z] ==True):
                        return False
                    
                    value[Z] = True
    
    return True
print("Type file-s name '.csv' to check Sudoku(e.g 'basicgrid.csv'): ")
with open(input(" ")) as file:
    grid = [list(map(int,i)) for i in csv.reader(file,delimiter=',')]

    if(check(grid)):
        print("true")
    else:
        print("false")
        
