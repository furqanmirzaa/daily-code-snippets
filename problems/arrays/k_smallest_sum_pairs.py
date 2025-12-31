class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        max_gold_collected = 0 # Stores the overall maximum gold found.

        # Define possible directions for movement: (delta_row, delta_col)
        # (0, 1) -> Right, (0, -1) -> Left, (1, 0) -> Down, (-1, 0) -> Up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def dfs(r: int, c: int, current_path_gold: int):
            # 'nonlocal' is used here to modify the 'max_gold_collected' variable
            # which is defined in the enclosing scope of 'getMaximumGold'.
            nonlocal max_gold_collected 

            # Update the global maximum with the gold collected in the current path.
            # A path can terminate at any point if there are no more valid moves.
            max_gold_collected = max(max_gold_collected, current_path_gold)
            
            # Store the current cell's gold value. This is necessary for backtracking.
            gold_at_current_cell = grid[r][c]
            
            # Mark the current cell as visited by temporarily setting its gold to 0.
            # This ensures that this cell is not revisited within the current DFS path.
            grid[r][c] = 0 
            
            # Explore all four adjacent directions (Up, Down, Left, Right).
            for dr, dc in directions:
                nr, nc = r + dr, c + dc # Calculate neighbor's coordinates.
                
                # Check if the neighbor cell is valid:
                # 1. It must be within the grid boundaries.
                # 2. It must contain gold (grid[nr][nc] > 0). This also implies
                #    it has not been visited in the current path.
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                    # Recursively call DFS for the neighbor, adding its gold to the path total.
                    dfs(nr, nc, current_path_gold + grid[nr][nc])
            
            # Backtrack: Restore the gold value of the current cell.
            # This is essential so that this cell can be part of other paths
            # initiated from different starting points in the outer loop.
            grid[r][c] = gold_at_current_cell
            
        # Iterate through each cell in the grid to find all possible starting points.
        # The miner can start from any cell that has gold (grid[r][c] > 0).
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0: # Check if the cell contains gold.
                    # Initiate a DFS path from this cell.
                    # The initial 'current_path_gold' is just the gold in the starting cell.
                    dfs(r, c, grid[r][c])
                    
        return max_gold_collected