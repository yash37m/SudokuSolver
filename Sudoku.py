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

        return True
    
if __name__=="__main__":
    S = Sudoku()
    board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

    print(S.isValidSudoku(board))
