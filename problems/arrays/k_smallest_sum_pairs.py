class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        """
        Calculates the maximum amount of gold a miner can collect.
        
        This problem is solved using Depth-First Search (DFS) with backtracking.
        Given the constraints (grid size up to 15x15) and the requirement to find
        the maximum sum along simple paths starting from any point, a DFS approach
        is generally considered optimal. Dynamic programming is not straightforward
        due to the complex 'visited' state required for each path.
        """
        rows = len(grid)
        cols = len(grid[0])
        max_gold_collected = 0 # Stores the overall maximum gold found.

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] # Possible movements (Right, Left, Down, Up)
        
        def dfs(r: int, c: int, current_path_gold: int):
            nonlocal max_gold_collected 

            max_gold_collected = max(max_gold_collected, current_path_gold)
            
            gold_at_current_cell = grid[r][c]
            grid[r][c] = 0 # Mark current cell as visited for this path
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc 
                
                # Check boundaries and if neighbor has gold (and not visited in current path)
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                    dfs(nr, nc, current_path_gold + grid[nr][nc])
            
            grid[r][c] = gold_at_current_cell # Backtrack: restore cell's gold
            
        # Iterate through each cell to find potential starting points for DFS
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    dfs(r, c, grid[r][c]) # Start DFS with current cell's gold
                    
        return max_gold_collected

"""
Complexity Analysis (same as Stage 3):
Time: O(R * C * 3^(R*C))
Space: O(R * C) for recursion stack.
"""