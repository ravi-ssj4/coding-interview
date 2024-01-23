class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        # 1. capture the un-surrounded Os by marking them
        def dfs(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                board[r][c] != "O"):
                return
            
            board[r][c] = "T"

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r == 0 or 
                    c == 0 or 
                    r == ROWS - 1 or 
                    c == COLS - 1):
                    dfs(r, c)
        # 2. change all the remaining Os to Xs
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

        # 3. Un-capture the un-surrounded Os by reversing the marked ones to Os
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "T":
                    board[r][c] = "O"