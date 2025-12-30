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
        # Problem constraints (1 <= nums.length) ensure nums is never empty, 
        # so nums[0] could also be used for initialization.
        max_so_far = -float('inf') 

        # Outer loop iterates through all possible starting points (i) of a subarray.
        for i in range(n):
            current_sum = 0
            # Inner loop iterates through all possible ending points (j) for the subarray
            # starting at 'i'. It also incrementally calculates the sum of the current subarray.
            for j in range(i, n):
                current_sum += nums[j]
                # Update max_so_far if the current subarray sum is greater.
                max_so_far = max(max_so_far, current_sum)
                
        return max_so_far

"""
Complexity Analysis for Brute-Force Solution:

Time Complexity: O(N^2)
- The outer loop runs 'N' times (from i=0 to N-1).
- The inner loop runs 'N-i' times for each 'i'. On average, it runs N/2 times.
- Specifically, the sum of iterations is N + (N-1) + ... + 1, which simplifies to N*(N+1)/2.
- Therefore, the number of operations is proportional to N^2.

Space Complexity: O(1)
- The algorithm uses a fixed amount of extra space for variables like 'n', 'max_so_far', 
  'i', 'j', and 'current_sum', regardless of the input array size.
- No additional data structures that grow with 'N' are used.
"""
