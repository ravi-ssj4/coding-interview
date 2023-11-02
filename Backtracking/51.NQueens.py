class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        res = []
        board = [["."] * n for _ in range(n)]
        cols = set()
        posDiag = set()
        negDiag = set()

        def backtrack(r):
            # base case
            if r == n:
                boardCopy = ["".join(row) for row in board]
                res.append(boardCopy)
                return
            
            for c in range(n):
                if c in cols or (r - c) in posDiag or (r + c) in negDiag:
                    continue
                
                # add the queen to the position r, c
                board[r][c] = "Q"
                cols.add(c)
                posDiag.add((r - c))
                negDiag.add((r + c))
                
                # backtrack
                backtrack(r + 1)

                # remove the queen from the position r, c
                board[r][c] = "."
                cols.remove(c)
                posDiag.remove((r - c))
                negDiag.remove((r + c))

        backtrack(0)
    
        return res