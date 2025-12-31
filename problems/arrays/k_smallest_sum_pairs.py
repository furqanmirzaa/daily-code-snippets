class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_gold_collected = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(r: int, c: int, current_path_gold: int):
            nonlocal max_gold_collected 

            max_gold_collected = max(max_gold_collected, current_path_gold)
            
            gold_at_current_cell = grid[r][c]
            grid[r][c] = 0 
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc 
                
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                    dfs(nr, nc, current_path_gold + grid[nr][nc])
            
            grid[r][c] = gold_at_current_cell
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    dfs(r, c, grid[r][c])
                    
        return max_gold_collected

"""
Complexity Analysis:

Let R be the number of rows and C be the number of columns in the grid.
Total number of cells N = R * C.

Time Complexity:
O(R * C * 3^(R*C)).
- The outer loops iterate R * C times, initiating a DFS from each cell.
- Each DFS explores paths in the grid. Since cells cannot be revisited
  in a single path, the maximum path length is R * C.
- At each step of the DFS, after visiting a cell, there are at most 3
  new valid directions to explore (excluding the direction from which
  the current cell was entered, and any previously visited cells in
  the current path).
- This leads to an exponential number of paths in the worst-case scenario.
- Given the constraints (R, C <= 15, so R*C <= 225), an exponential
  complexity like 3^(R*C) might seem too high. However, the grid structure
  and the effective pruning due to 0-gold cells (acting as barriers or
  already visited cells) make the practical average case performance
  much better, allowing this solution to pass within typical time limits.

Space Complexity:
O(R * C).
- This is primarily due to the recursion stack depth used by the DFS.
- In the worst case, a path could visit all R * C cells, leading to a
  recursion depth of R * C.
- The `directions` list uses constant space.
- The `grid` is modified in-place for visited tracking, so it does not
  add extra space beyond the input (excluding Python's internal list
  copying for arguments, which is not usually counted for "auxiliary space").
"""