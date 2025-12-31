import sys
import unittest

# Increase the recursion limit for deep DFS paths, as grid can be up to 15x15 (225 cells).
# Python's default recursion limit (often 1000) is usually sufficient, but for very long
# paths, it might need to be increased. Setting it to 1000 or 2500 is common for DSA problems.
sys.setrecursionlimit(2500) 

class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        """
        Calculates the maximum amount of gold a miner can collect from a grid.
        
        The miner can start at any cell with a positive amount of gold.
        From a cell, the miner can move to an adjacent cell (up, down, left, right)
        that also contains a positive amount of gold and has not been visited
        in the current collection path. The goal is to find the path that yields
        the maximum total gold.
        
        This problem is solved using a Depth-First Search (DFS) algorithm with
        backtracking. The core idea is to explore all possible paths starting
        from every cell that contains gold.
        
        Algorithm Steps:
        1. Initialize `max_gold_collected` to 0. This variable will store the
           overall maximum gold found across all possible starting points and paths.
        2. Define `rows` and `cols` from the dimensions of the input `grid`.
        3. Define `directions` for movement: `(dr, dc)` tuples representing
           (delta_row, delta_col) for up, down, left, right.
        4. Implement a nested helper function `dfs(r, c, current_path_gold)`:
           a. This function is responsible for exploring paths recursively.
           b. It takes the current row `r`, column `c`, and the `current_path_gold`
              accumulated up to this cell.
           c. Update `max_gold_collected` with the maximum between its current value
              and `current_path_gold`. This is because any point in a path could
              represent the end of a valid path (e.g., if there are no further moves).
           d. Store the gold value of `grid[r][c]` in a temporary variable (`gold_at_current_cell`).
           e. Mark the current cell as visited for the *current path* by setting
              `grid[r][c] = 0`. This prevents revisiting it within the same path. This
              is a crucial step for backtracking.
           f. Iterate through all `directions`:
              i. Calculate the coordinates of the `neighbor` cell (`nr`, `nc`).
              ii. Check if the `neighbor` is within grid boundaries (`0 <= nr < rows`
                  and `0 <= nc < cols`) and if it contains gold (`grid[nr][nc] > 0`).
                  The `grid[nr][nc] > 0` check implicitly handles two conditions:
                  the cell must have gold, and it must not have been visited in the
                  current path (since visited cells are temporarily set to 0).
              iii. If valid, recursively call `dfs(nr, nc, current_path_gold + grid[nr][nc])`.
           g. After exploring all paths from `(r, c)`, backtrack: restore the original
              gold value to `grid[r][c]` using `gold_at_current_cell`. This ensures
              that this cell can be part of other paths initiated from different
              starting points later in the outer loop.
        5. Iterate through every cell `(r, c)` in the `grid`:
           a. If `grid[r][c] > 0` (meaning it contains gold and can be a starting point),
              initiate a new DFS path starting from `(r, c)`.
              Call `dfs(r, c, grid[r][c])`, with `grid[r][c]` as the initial gold.
        6. Return the final `max_gold_collected`.
        
        Args:
            grid: A list of lists of integers representing the grid. Each `grid[i][j]`
                  is the amount of gold in cell `(i, j)`. Values are `0 <= grid[i][j] <= 100`.
                  Dimensions are `1 <= m, n <= 15` (where `m` is rows, `n` is columns).
                  
        Returns:
            The maximum amount of gold that can be collected.
        
        Complexity Analysis:
        Let R be the number of rows and C be the number of columns in the grid.
        Total number of cells N = R * C.
        
        Time Complexity:
        O(R * C * 3^(R*C)).
        - The outer loops iterate R * C times, potentially initiating a DFS from each cell.
        - Each DFS explores paths in the grid. Since cells cannot be revisited
          in a single path, the maximum path length is R * C. At each step of the DFS,
          after visiting a cell, there are at most 3 new valid directions to explore
          (excluding the direction from which the current cell was entered, and any
          previously visited cells in the current path). This leads to an exponential
          number of paths in the worst-case scenario.
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
          add extra auxiliary space beyond the input itself.
        """
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
            # A path can terminate at any point if there are no more valid moves, so
            # the max should be updated even if it's not the end of the grid.
            max_gold_collected = max(max_gold_collected, current_path_gold)
            
            # Store the current cell's gold value. This is crucial for backtracking
            # to restore the grid to its original state for subsequent DFS calls.
            gold_at_current_cell = grid[r][c]
            
            # Mark the current cell as visited for this specific DFS path by temporarily
            # setting its gold to 0. This prevents revisiting this cell.
            grid[r][c] = 0 
            
            # Explore all four adjacent directions.
            for dr, dc in directions:
                nr, nc = r + dr, c + dc # Calculate neighbor's coordinates.
                
                # Check if the neighbor cell is valid:
                # 1. It must be within the grid boundaries (0 <= nr < rows and 0 <= nc < cols).
                # 2. It must contain gold (grid[nr][nc] > 0). This check also implicitly
                #    ensures the cell has not been visited in the current path (as visited
                #    cells are temporarily set to 0).
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] > 0:
                    # Recursively call DFS for the neighbor, adding its gold to the current path total.
                    dfs(nr, nc, current_path_gold + grid[nr][nc])
            
            # Backtrack: Restore the gold value of the current cell.
            # This makes the cell available for other potential paths that start from
            # different initial cells in the outer loop or pass through this cell from
            # a different direction.
            grid[r][c] = gold_at_current_cell
            
        # Iterate through each cell in the grid to find all possible starting points.
        # The miner can start from any cell that has gold (grid[r][c] > 0).
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0: # If a cell has gold, it's a valid starting point.
                    # Initiate a DFS path from this cell.
                    # The initial 'current_path_gold' is just the gold in the starting cell.
                    dfs(r, c, grid[r][c])
                    
        return max_gold_collected

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        grid = [[0,6,0],[5,8,7],[0,9,0]]
        self.assertEqual(self.sol.getMaximumGold(grid), 24)
        # Expected path example: 9 -> 8 -> 7 (or 7 -> 8 -> 9), sum = 24.

    def test_example_2(self):
        grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
        self.assertEqual(self.sol.getMaximumGold(grid), 28)
        # Expected path example: 1->2->3->4->5->6->7 (sum = 28)

    def test_single_cell_grid(self):
        grid = [[7]]
        self.assertEqual(self.sol.getMaximumGold(grid), 7)

    def test_no_gold(self):
        grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.assertEqual(self.sol.getMaximumGold(grid), 0)

    def test_isolated_gold_cells(self):
        grid = [[1,0,10],[0,0,0],[100,0,1]]
        self.assertEqual(self.sol.getMaximumGold(grid), 100)
        # The maximum gold comes from collecting from the single cell with 100 gold.

    def test_simple_linear_path(self):
        grid = [[1,1,1]]
        self.assertEqual(self.sol.getMaximumGold(grid), 3)

    def test_forking_paths_complex(self):
        grid = [[1,2,3],[0,10,0],[4,5,6]]
        self.assertEqual(self.sol.getMaximumGold(grid), 26)
        # Path example: 3 -> 2 -> 10 -> 5 -> 6 (sum = 26)

    def test_path_hitting_boundary_in_small_grid(self):
        grid = [[1,2],[3,4]]
        self.assertEqual(self.sol.getMaximumGold(grid), 10)
        # Path example: 1 -> 3 -> 4 -> 2 (sum = 10)

    def test_all_zeros_except_one_path_segment(self):
        grid = [[0,0,0,0],
                [0,1,2,3],
                [0,0,0,0]]
        self.assertEqual(self.sol.getMaximumGold(grid), 6) # Path: 1->2->3

    def test_complex_grid_with_zeros_blocking(self):
        grid = [[1,1,1,1,1],
                [1,0,1,0,1],
                [1,1,1,1,1]]
        self.assertEqual(self.sol.getMaximumGold(grid), 8)
        # Path example: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (2,1) -> (2,0) -> (1,0) (sum = 8)

    def test_large_grid_single_path(self):
        grid = [[1,1,1,1,1],
                [0,0,0,0,1],
                [0,0,0,0,1],
                [0,0,0,0,1],
                [0,0,0,0,1]]
        self.assertEqual(self.sol.getMaximumGold(grid), 9)
        # Path example: (0,0) -> (0,1) -> (0,2) -> (0,3) -> (0,4) -> (1,4) -> (2,4) -> (3,4) -> (4,4)

    def test_disconnected_components(self):
        grid = [[1,0,0,0,2],
                [0,0,0,0,0],
                [3,0,0,0,4]]
        self.assertEqual(self.sol.getMaximumGold(grid), 4) # Max of {1, 2, 3, 4} (isolated cells)

if __name__ == '__main__':
    # Using unittest.main() to run tests.
    # argv=['first-arg-is-ignored'] and exit=False are used to allow
    # the script to run tests without trying to parse command-line arguments
    # and without exiting the program immediately after tests, which is useful
    # in some interactive environments or when integrating with other code.
    unittest.main(argv=['first-arg-is-ignored'], exit=False)