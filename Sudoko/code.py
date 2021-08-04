#Sudoku -------------------------------------------
board = [ [7,8,0,4,0,0,1,2,0],
          [6,0,0,0,7,5,0,0,9],
          [0,0,0,6,2,1,5,7,8],
          [0,0,7,0,4,0,2,6,0],
          [0,0,1,0,5,0,9,3,0],
          [9,0,4,0,6,0,0,0,5],
          [0,7,0,3,0,0,0,1,2],
          [1,2,0,0,0,7,4,0,3],
          [0,4,9,2,0,6,0,0,7],
          ]
def prboard(bo):
    for i in range(len(bo)):
        if i%3==0 and i!=0: print("- - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j%3==0 and j!=0: print("|",end=" ")
            print(bo[i][j],end=" ")
            if j%8==0 and j!=0: print()
        

def findempty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j]==0: return(i,j)
    return None

def isvalid(bo,num,pos):
    for i in range(len(bo)):
        if bo[pos[0]][i]==num: return False
    for i in range(len(bo[0])):
        if bo[i][pos[1]]==num: return False
    box_x = pos[0]//3
    box_y = pos[1]//3
    for i in range(box_x*3,box_x*3+3):
        for j in range(box_y*3,box_y*3+3):
            if bo[i][j]==num: return False
    return True
        
def solve(bo):
    find = findempty(bo)
    if not find: return True
    else: row,col = find
    for i in range(1,10):
        if isvalid(bo,i,(row,col)):
            bo[row][col]=i
            if solve(bo):
                return True
            bo[row][col] =0
    return False
    
prboard(board)
print()
solve(board)
prboard(board)
