import unittest

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

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        grid = [[0,6,0],[5,8,7],[0,9,0]]
        self.assertEqual(self.sol.getMaximumGold(grid), 24)

    def test_example_2(self):
        grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
        self.assertEqual(self.sol.getMaximumGold(grid), 28)

    def test_single_cell_grid(self):
        grid = [[7]]
        self.assertEqual(self.sol.getMaximumGold(grid), 7)

    def test_no_gold(self):
        grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.assertEqual(self.sol.getMaximumGold(grid), 0)

    def test_isolated_gold_cells(self):
        grid = [[1,0,10],[0,0,0],[100,0,1]]
        self.assertEqual(self.sol.getMaximumGold(grid), 100)

    def test_simple_linear_path(self):
        grid = [[1,1,1]]
        self.assertEqual(self.sol.getMaximumGold(grid), 3)

    def test_forking_paths_complex(self):
        grid = [[1,2,3],[0,10,0],[4,5,6]]
        self.assertEqual(self.sol.getMaximumGold(grid), 26)

    def test_path_hitting_boundary_in_small_grid(self):
        grid = [[1,2],[3,4]]
        self.assertEqual(self.sol.getMaximumGold(grid), 10) # Path example: 1 -> 3 -> 4 -> 2

    def test_all_zeros_except_one_path_segment(self):
        grid = [[0,0,0,0],
                [0,1,2,3],
                [0,0,0,0]]
        self.assertEqual(self.sol.getMaximumGold(grid), 6) # Path: 1->2->3

    def test_complex_grid_with_zeros_blocking(self):
        grid = [[1,1,1,1,1],
                [1,0,1,0,1],
                [1,1,1,1,1]]
        self.assertEqual(self.sol.getMaximumGold(grid), 8) # Path example: (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (2,1) -> (2,0) -> (1,0)

    def test_large_grid_single_path(self):
        grid = [[1,1,1,1,1],
                [0,0,0,0,1],
                [0,0,0,0,1],
                [0,0,0,0,1],
                [0,0,0,0,1]]
        self.assertEqual(self.sol.getMaximumGold(grid), 9) # Path: (0,0) -> (0,1) -> (0,2) -> (0,3) -> (0,4) -> (1,4) -> (2,4) -> (3,4) -> (4,4)

    def test_disconnected_components(self):
        grid = [[1,0,0,0,2],
                [0,0,0,0,0],
                [3,0,0,0,4]]
        self.assertEqual(self.sol.getMaximumGold(grid), 4) # Max of {1, 2, 3, 4}

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)