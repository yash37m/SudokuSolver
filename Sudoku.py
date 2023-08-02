from collections import Counter

class Sudoku:
    # Checks if all the digits are appearing exactly one in a particular row.
    def isValidSudoku(self, board):
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

        return 
        
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
    
    sol = []
    def fillSudoku(self, board, pVal = 0):
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for val in range(pVal+1,10):
                        
                        if self.checkValid(i,j,val):
                            self.sol.append((i,j))
                            board[i][j] = val
                            break
                    pVal = 0

                    if board[i][j] == ".": 
                        print(self.sol,i,j)     
                        lastSol = self.sol.pop()
                        lastVal = board[lastSol[0]][lastSol[1]]
                        board[lastSol[0]][lastSol[1]] = "."
                        board = self.fillSudoku(board, lastVal)

        return board
    
if __name__=="__main__":
    S = Sudoku()
    board = [[5,3,".",".",7,".",".",".","."]
,[6,".",".",1,9,5,".",".","."]
,[".",9,8,".",".",".",".",6,"."]
,[8,".",".",".",6,".",".",".",3]
,[4,".",".",8,".",3,".",".",1]
,[7,".",".",".",2,".",".",".",6]
,[".",6,".",".",".",".",2,8,"."]
,[".",".",".",4,1,9,".",".",5]
,[".",".",".",".",8,".",".",7,9]]
    
# [['5', '3', 1, 2, '7', 3, 4, 5, 6], ['6', 2, 3, '1', '9', '5', 1, 7, 8], [4, '9', '8', 1, 5, 6, 2, '6', 3], ['8', 1, 2, 3, '6', 4, 5, 6, '3'], ['4', 3, 4, '8', 1, '3', 7, 2, '1'], ['7', 5, 6, 7, '2', 2, 3, 1, '6'], [1, '6', 5, 4, 2, 8, '2', '8', 7], [2, 4, 8, '4', '1', '9', 6, 3, '5'], [3, 6, 7, 5, '8', 1, 8, '7', '9']]

print(S.fillSudoku(board))

