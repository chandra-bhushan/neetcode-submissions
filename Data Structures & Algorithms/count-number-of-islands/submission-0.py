from collections import deque

DIRS = [(0,1), (1,0), (0,-1), (-1,0)]
LAND = "1"
WATER = "0"

class Solution:
    
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0    

        rows = len(grid)
        cols = len(grid[0])

        num_island = 0

        for r in range(rows):
            for c in range(cols):
                cur = grid[r][c]

                # only need to check if we find a land to make it a island
                if cur == LAND:
                    num_island += 1

                    queue = deque([(r, c)])

                    grid[r][c] = WATER # sink it so we don't count it agian or we can have seperate var visited set

                    while queue:
                        cr, cc = queue.popleft()

                        for dr, dc in DIRS:
                            nr, nc = cr + dr, cc + dc

                            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == LAND:
                                grid[nr][nc] = WATER
                                queue.append((nr, nc))

        return num_island



