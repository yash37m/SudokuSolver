class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in board:
            counted = Counter(i)
            for i in counted:
                if i != ".":
                    if counted[i] > 1:
                        return False
        
        for c in range(9):
            counted = {}
            for r in range(9):
                if board[r][c] in counted and board[r][c] !=".":
                    return False
                else:
                    counted[board[r][c]] = 1
        
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
