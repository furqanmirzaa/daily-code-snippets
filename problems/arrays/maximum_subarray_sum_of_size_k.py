class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Given an integer array `nums`, find the subarray with the largest sum, and return its sum.
        A subarray is a contiguous non-empty sequence of elements within an array.

        This implementation uses a brute-force approach to find the maximum subarray sum.
        It iterates through all possible contiguous subarrays, calculates their sum,
        and keeps track of the maximum sum encountered.
        """
        n = len(nums)
        
        # Initialize max_so_far with the smallest possible value.
        # This ensures that any actual subarray sum, even a negative one, will be larger.
        max_so_far = -float('inf') 

        # Outer loop iterates through all possible starting points of a subarray.
        for i in range(n):
            current_sum = 0
            # Inner loop iterates through all possible ending points for the current starting point.
            # It also incrementally calculates the sum of the current subarray.
            for j in range(i, n):
                current_sum += nums[j]
                # Update max_so_far if the current subarray sum is greater.
                max_so_far = max(max_so_far, current_sum)
                
        return max_so_far
