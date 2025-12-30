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

# --- Test Cases ---
if __name__ == "__main__":
    solver = Solution()

    print("Running basic test cases...")

    # Test Case 1: Example from problem description
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected1 = 6 # Subarray [4, -1, 2, 1] has sum 6
    result1 = solver.maxSubArray(nums1)
    print(f"Test 1: nums={nums1}, Expected={expected1}, Got={result1}")
    assert result1 == expected1, f"Test 1 FAILED: Expected {expected1}, Got {result1}"

    # Test Case 2: All positive numbers
    nums2 = [1, 2, 3, 4, 5]
    expected2 = 15 # Subarray [1, 2, 3, 4, 5] has sum 15
    result2 = solver.maxSubArray(nums2)
    print(f"Test 2: nums={nums2}, Expected={expected2}, Got={result2}")
    assert result2 == expected2, f"Test 2 FAILED: Expected {expected2}, Got {result2}"

    # Test Case 3: Mixed positive and negative numbers, max subarray in middle
    nums3 = [1, -2, 3, -1, 2]
    expected3 = 4 # Subarray [3, -1, 2] has sum 4
    result3 = solver.maxSubArray(nums3)
    print(f"Test 3: nums={nums3}, Expected={expected3}, Got={result3}")
    assert result3 == expected3, f"Test 3 FAILED: Expected {expected3}, Got {result3}"

    print("\nAll basic test cases passed successfully!")
