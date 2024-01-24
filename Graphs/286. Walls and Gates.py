class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        visited = set()
        q = collections.deque()

        def addRooms(r, c):
            if (r < 0 or r >= ROWS or
                c < 0 or c >= COLS or 
                (r, c) in visited or 
                rooms[r][c] == -1):
                return
            rooms[r][c] = dist
            visited.add((r, c))
            q.append([r, c])

        # Add all the gates to the Queue
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        dist = 1 # initially all the rooms adjacent to all the gates will be at a distance of 1
        # do a simultaneous BFS until queue is empty
        while q:
            print(q)
            for i in range(len(q)): # takes snapshot of len(q), later on even if q changes, this won't
                r, c = q.popleft()
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1 # for next round, distance of all rooms from prev all gates = prev dist + 1

        