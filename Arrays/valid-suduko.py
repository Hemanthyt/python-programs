from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        r=defaultdict(set)   
        c=defaultdict(set)   
        s=defaultdict(set)  
        for row in range(len(board)) :
            for col in range(len(board[0])):
                if board[row][col] == ".":
                    continue
                value = board[row][col]
                
                if value in r[row] and value in c[col] and s[row//3,col//3]:
                    return 0
                r[row].add(value)
                c[col].add(value)
                s[row//3,col//3].add(value)
            return 1
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == ".":
                    continue
                value = board[row][col] 

                if value in r[row] or value in c[col] or value in s[row//3,col//3]:
                    return False

                r[row].add(value)
                c[col].add(value)
                s[row//3,col//3].add(value)

        return True
s = Solution()
print(s.isValidSudoku(board = 
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]))