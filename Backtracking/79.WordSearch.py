class Solution:
    '''
    method: backtracking

    time: (all elements in the board) * time taken by each dfs on an element
            = (m.n) * 4^n (because for each element we explore 4 neighbors, 4.4.4... n times)
            = O(m.n.4^n)
    
    '''
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # base case 1
            if i == len(word):
                return True
            # base case 2
            if (r < 0 or c < 0 or 
               r >= ROWS or c >= COLS or
               board[r][c] != word[i] or
               (r, c) in path):
               return False
            
            # consider all combinations including current cell(r, c) to the path
            path.add((r, c))
            res = (dfs(r - 1, c, i + 1) or
                  dfs(r + 1, c, i + 1) or
                  dfs(r, c - 1, i + 1) or
                  dfs(r, c + 1, i + 1))
            path.remove((r, c)) # reset path to original state
            # if exploration in all 4 directions failed,
            # ie. we are at a deadend, return False 
            # (ie. no solution with current starting point (r, c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False