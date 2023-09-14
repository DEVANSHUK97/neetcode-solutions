# https://leetcode.com/problems/valid-sudoku/
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check for rows
        for i in range(9):
            row_dict = {}
            for j in range(9):
                if board[i][j] == ".":
                    continue
                row_dict[board[i][j]] = row_dict.get(board[i][j], 0)+1
                if row_dict[board[i][j]] > 1:
                    return False
        #check for cols
        for i in range(9):
            col_dict = {}
            for j in range(9):
                if board[j][i] == ".":
                    continue
                col_dict[board[j][i]] = col_dict.get(board[j][i], 0)+1
                if col_dict[board[j][i]] > 1:
                    return False
        #check for sub-square
        def check_subsquare(x,y):
            area_dict = {}
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if board[j][i] == ".":
                        continue
                    area_dict[board[j][i]] = area_dict.get(board[j][i], 0)+1
                    if area_dict[board[j][i]] > 1:
                        return False
            return True
        
        ans = True
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                ans = ans and check_subsquare(i,j)
        return ans
