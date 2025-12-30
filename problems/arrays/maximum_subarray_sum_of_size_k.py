class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Given an integer array `nums`, find the subarray with the largest sum, and return its sum.
        A subarray is a contiguous non-empty sequence of elements within an array.

        This implementation uses Kadane's Algorithm, an efficient dynamic programming approach.
        """
        
        max_current = nums[0]  # Max sum of a subarray ending at current position
        max_global = nums[0]   # Overall maximum sum found so far across all subarrays

        for i in range(1, len(nums)):
            num = nums[i]
            max_current = max(num, max_current + num)
            max_global = max(max_global, max_current)
            
        return max_global

# --- Test Cases and Edge Cases ---
if __name__ == "__main__":
    solver = Solution()

    # Each test case is a tuple: (input_nums, expected_output, description)
    test_cases = [
        # Basic Functionality Tests
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, "Example from problem description"),
        ([1, 2, 3, 4, 5], 15, "All positive numbers"),
        ([1, -2, 3, -1, 2], 4, "Mixed positive and negative, max subarray in middle"),
        
        # Edge Cases
        ([5], 5, "Single positive element array"),
        ([-10], -10, "Single negative element array"),
        ([-2, -1, -3], -1, "All negative numbers (max is the least negative)"),
        ([0], 0, "Single zero element array"),
        ([0, 0, 0], 0, "Array of zeros"),
        ([1, -1, 1, -1, 1], 1, "Alternating positive/negative, max is a single element"),
        ([7, -3, 10, -4, 2, 1, -9, 8], 14, "Complex mixed array with peak sum"), # Subarray [7, -3, 10] = 14
        ([2, -3, 4, -1, -2, 1, 5, -3], 7, "Array with max subarray across multiple segments"), # Subarray [4, -1, -2, 1, 5] = 7
        ([-5, -1, -2, -3, -4], -1, "Another all negative, max is largest negative"),
    ]

    print("Running test cases and edge cases...")
    all_passed = True
    for i, (nums, expected, description) in enumerate(test_cases):
        result = solver.maxSubArray(nums)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test {i+1} [{description}]: nums={nums}, Expected={expected}, Got={result} -- {status}")
        if result != expected:
            all_passed = False
    
    if all_passed:
        print("\nAll 🚀 test cases and edge cases passed successfully!")
    else:
        print("\nSome ❌ test cases failed.")
