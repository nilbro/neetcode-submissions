import collections

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # select each row
        for row in range(9):
            s = set()
            # select each element in each row
            for col in range(9):
                item = board[row][col]
                if item == '.':
                    continue
                if item in s:
                    return False
                s.add(item)
    

        # select each col
        for row in range(9):
            s = set()
            # select each element in each col
            for col in range(9):
                item = board[col][row]
                if item == '.':
                    continue
                if item in s:
                    return False
                s.add(item)
        
        def helper(R,C):
            s = set()
            for row in range(R, R+3):
                for col in range(C, C+3):
                    item = board[col][row]
                    if item == '.':
                        continue
                    if item in s:
                        return False
                    s.add(item)
            return True
        
        for row in range(0,9,3):
            for col in range(0,9,3):
                if helper(row, col):
                    continue
                else:
                    return False


        return True
 