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
    
    # sol = []
    # def fillSudoku(self, board, pVal = 0):
        # for i in range(9):
        #     for j in range(9):
                # if board[i][j] == ".":
        #             for val in range(pVal+1,10):
                        
        #                 if self.checkValid(i,j,val):
        #                     self.sol.append((i,j))
        #                     board[i][j] = val
        #                     break
        #             pVal = 0

        #             if board[i][j] == ".": 
        #                 print(self.sol,i,j)     
        #                 lastSol = self.sol.pop()
        #                 lastVal = board[lastSol[0]][lastSol[1]]
        #                 board[lastSol[0]][lastSol[1]] = "."
        #                 board = self.fillSudoku(board, lastVal)

        # return board

    def traverseBoard(self, board):
        # r1,r2,r3,r4,r5,r6,r7,r8,r9={},{},{},{},{},{},{},{},{}
        # c1,c2,c3,c4,c5,c6,c7,c8,c9={},{},{},{},{},{},{},{},{}
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
                    
    
    def checkunique(self, dict, index):
        row = index[0]
        col = index[1]
        # print(dict)
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
                    if[1] in range(mC, mC + 3):
                        matValues += dict[i]
            # print(mR,mC,matValues,Val)
            matValues.remove(Val)
            if Val not in matValues:
                return Val

        return 0
    
    def fillBoard(self,board):
        solSet = self.traverseBoard(board)
        
        while(len(solSet) >= 1):

            for key in solSet:
                if len(solSet[key]) == 1:
                    board[key[0]][key[1]] = solSet[key][0]
                    del board[key]
                    continue

                value = self.checkunique(solSet, key)
                if value != 0:
                    board[key[0]][key[1]] = value
                    del board[key]
                    continue

            solSet = self.traverseBoard(board)
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

    print(S.traverseBoard(board))
    print(S.fillBoard(board))

