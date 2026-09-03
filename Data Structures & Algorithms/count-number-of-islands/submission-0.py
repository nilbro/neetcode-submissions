class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        from collections import deque

        rows = len(grid)
        cols = len(grid[0])

        q = deque()

        seen = set()
        islands = 0

        def bfs(r, c):
            directions = [
                    [-1, 0], 
                    [1, 0], 
                    [0, -1], 
                    [0, 1]
                ]
            q.append((r,c))
            while q:
                r, c = q.pop()
                for dr, dc in directions:
                    R = r+dr
                    C = c+dc

                    if R in range(rows) and C in range(cols) and grid[R][C] == "1" and (R,C) not in seen:

                        q.append((R, C))
                        seen.add((R, C))
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in seen:
                    bfs(row, col)
                    seen.add((row,col))
                    islands += 1
        return islands
        