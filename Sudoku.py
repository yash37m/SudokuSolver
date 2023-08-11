from collections import Counter

class Sudoku:

    #checks if the given value is allowable the position given.
    def checkValid(self,row,col,val):
            if val not in board[row]:                           #check for possiblity in row
                for rows in range(9):
                    if val == board[rows][col]:                 #check for possiblity in column
                        return False
                
                for mR in range((row//3)*3, (row//3)*3 + 3):    #check for possiblity in matrix
                    for mC in range((col//3)*3, (col//3)*3 + 3):
                        if board[mR][mC] == val:
                            return False
                return True
            return False
    
    # Iterates over blank spaces and creates a list of all the values that are valid at the position.
    def traverseBoard(self, board):
        solSet = {}
        for i in range(9):
            for j in range(9):
                if board [i][j] == ".":
                    for val in range(1,10):
                        if self.checkValid(i,j,val):
                            if (i,j) in solSet.keys():
                                solSet[(i,j)].append(val)
                            else:
                                solSet[(i,j)] = [val]
        return solSet
                    
    # Checks if a value is unique in whole row, column or matrix.
    def checkunique(self, dict, index):
        row = index[0]
        col = index[1]
        for Val in dict[index]:

            #checks for uniqueness in row.
            rowValues = []
            for i in list(dict.keys()):
                if i[0] == row:
                    rowValues += dict[i]
            rowValues.remove(Val)
            if Val not in rowValues:
                return Val
            
            #checks for uniqueness in Column.
            colValues = []
            for i in list(dict.keys()):
                if i[1] == col:
                    colValues += dict[i]
            colValues.remove(Val)
            if Val not in colValues:
                return Val
            
            #checks for uniqueness in Matrix.
            mR, mC = (row//3)*3, (col//3)*3
            matValues = []
            for i in list(dict.keys()):
                if i[0] in range(mR, mR + 3):
                    if i[1] in range(mC, mC + 3):
                        matValues += dict[i]
            matValues.remove(Val)
            if Val not in matValues:
                return Val

        return 0
    
    # Fills board by iterating over blank values and using the created methods.
    def fillBoard(self,board):
        solSet = self.traverseBoard(board)
        
        while(len(solSet) >= 1):

            for key in list(solSet.keys()):
                if len(solSet[key]) == 1:
                    board[key[0]][key[1]] = solSet[key][0]
                    del solSet[key]
                    break

                value = self.checkunique(solSet, key)
                if value != 0:
                    board[key[0]][key[1]] = value
                    del solSet[key]
                    break

            solSet = self.traverseBoard(board)
        return board
    
    #Validates the Sudoku Board.
    def isValidSudoku(self, board):
        # Checks if all the digits are appearing exactly one in a particular row.
        for i in board:
            counted = Counter(i)
            for i in counted:
                if i != ".":
                    if counted[i] > 1:
                        return False
        
        # Checks if all the digits are appearing exactly one in a particular column.
        for c in range(9):
            counted = {}
            for r in range(9):
                if board[r][c] in counted and board[r][c] !=".":
                    return False
                else:
                    counted[board[r][c]] = 1
        
        # Checks if all the digits are appearing exactly one in a particular inner 3*3 matrix.
        for r in range(0,9,3):
            for c in range(0,9,3):
                mat = [
                    board[r][c],board[r][c+1],board[r][c+2],
                    board[r+1][c],board[r+1][c+1],board[r+1][c+2],
                    board[r+2][c],board[r+2][c+1],board[r+2][c+2]
                ]
                counted = Counter(mat)
                for i in counted:
                    if i != ".":
                        if counted[i] > 1:
                            return False

        return True
    
if __name__=="__main__":
    S = Sudoku()
    board = [
    [".", 8, 5,".", 7, ".", 2, 6,"."],
    [1, ".", ".", 6, ".", 4, ".", ".", 7],
    [3, ".", ".", ".", ".", ".", ".", ".", 4],
    [".", 4, ".", 3, 5, 2, ".", 9, "."],
    [5, ".", ".", 9, ".", 7, ".",".",2],
    [".", 3, ".", 8, 1, 6, ".", 4,"."],
    [7, ".", ".", ".", ".", ".", ".", ".", 6],
    [9, ".", ".", 5, ".", 8, ".", ".", 1],
    [".", 6, 3, ".", 2, ".", 4, 5, "."]]
    
    print("The given board is: ",S.isValidSudoku(board))
    ans = S.fillBoard(board)
    print(ans)
    print("The provided solution is: ",S.isValidSudoku(ans))
