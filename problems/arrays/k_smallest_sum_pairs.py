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

    def test_no_gold(self):        # Grid with no gold cells
        grid = [[0,0,0],[0,0,0],[0,0,0]]
        self.assertEqual(self.sol.getMaximumGold(grid), 0)

    def test_isolated_gold_cells(self):
        grid = [[1,0,10],[0,0,0],[100,0,1]]
        self.assertEqual(self.sol.getMaximumGold(grid), 100) # Max is one isolated cell

    def test_simple_path(self):
        grid = [[1,1,1]]
        self.assertEqual(self.sol.getMaximumGold(grid), 3)

    def test_forking_paths(self):
        grid = [[1,2,3],[0,10,0],[4,5,6]]
        self.assertEqual(self.sol.getMaximumGold(grid), 26) # Path: 3->2->10->5->6

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)