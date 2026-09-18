class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            # if we are out of bounds or we hit a 0, this is the base case
            if (r < 0 or r >= rows) or (c < 0 or c >= cols) or (grid[r][c] == "0"):
                # then we stop the recursion
                return
            # if we see a value with 1 we make it 0 so we don't repeat it
            grid[r][c] = "0"

            # if not explore top, left, bottom, right
            dfs(r+1, c)
            dfs(r, c-1)
            dfs(r-1, c)
            dfs(r, c+1)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        return islands

            

            