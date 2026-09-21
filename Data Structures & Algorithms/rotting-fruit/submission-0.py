from collections import deque

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
EMPTY = 0
FRESH = 1
ROTTEN = 2

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        queue = deque() # for holding rotten
        fresh = 0

        # first pass
        for r in range(rows):
            for c in range(cols):
                cur = grid[r][c]
                if cur == FRESH:
                    fresh += 1
                elif cur == ROTTEN:
                    queue.append((r, c)) # we will use to rotting adjacent cells

        if fresh == 0:
            return 0

        minutes = 0

        # now start rotting every minutes
        while queue and fresh > 0:
            minutes += 1

            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in DIRS:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0<= nc < cols and grid[nr][nc] == FRESH:
                        grid[nr][nc] = ROTTEN
                        fresh -= 1
                        queue.append((nr, nc))

       
        return minutes if fresh == 0 else -1
        