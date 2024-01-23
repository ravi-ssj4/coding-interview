class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        res = 0

        def bfs(r, c):
            q = collections.deque([[r, c]])
            while q:
                r, c = q.popleft()
                
                if (r < 0 or r >= ROWS or 
                    c < 0 or c >= COLS or 
                    (r, c) in visited or 
                    grid[r][c] == "0"):
                    continue

                visited.add((r, c))
                
                directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
                for dr, dc in directions:
                    newR = r + dr
                    newC = c + dc
                    q.append([newR, newC])

                    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1
                    bfs(r, c) # visit the entire island
        return res

    '''
    method 2: via iterative DFS
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set() # will contain elements of the form (r, c)
        ROWS, COLS = len(grid), len(grid[0])

        def bfs(r, c):
            stack = []
            visited.add((r, c))
            stack.append((r, c))

            while stack:
                row, col = stack.pop()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    nr = row + dr
                    nc = col + dc
                    if (nr in range(ROWS) and
                        nc in range(COLS) and
                        grid[nr][nc] == "1" and
                        (nr, nc) not in visited):
                        stack.append((nr, nc))
                        visited.add((nr, nc))
            

        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
        return islands


    '''
    method 3: via recursive DFS
    '''
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or grid[r][c] == "0"
                or (r, c) in visit
            ):
                return

            visit.add((r, c))
            
            # directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            # for dr, dc in directions:
            #     dfs(r + dr, c + dc)

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands