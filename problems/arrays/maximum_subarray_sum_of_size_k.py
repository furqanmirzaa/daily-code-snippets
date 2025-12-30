class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Given an integer array `nums`, find the subarray with the largest sum, and return its sum.
        A subarray is a contiguous non-empty sequence of elements within an array.

        This implementation uses Kadane's Algorithm, an efficient dynamic programming approach.

        Kadane's algorithm works by iterating through the array and keeping track of two main values:
        1. `max_current`: The maximum sum of a subarray ending at the current position.
           It's updated by comparing the current number itself (starting a new subarray)
           with the sum of the current number and the `max_current` from the previous position
           (extending the previous subarray).
        2. `max_global`: The overall maximum sum found anywhere in the array so far.
           It's updated whenever `max_current` surpasses its current value.
        
        Problem constraints typically guarantee `1 <= nums.length`, meaning `nums` is never empty.
        This allows initializing `max_current` and `max_global` with `nums[0]`.
        """
        
        # Initialize max_current and max_global with the first element of the array.
        # This is safe because problem constraints guarantee that `nums` is non-empty.
        max_current = nums[0]  # Max sum of a subarray ending at the current position
        max_global = nums[0]   # Overall maximum sum found so far across all subarrays

        # Iterate through the array starting from the second element (index 1).
        # The first element is already handled by initialization.
        for i in range(1, len(nums)):
            num = nums[i]
            
            # Calculate the maximum sum of a subarray ending at the current position 'i'.
            # We either extend the previous subarray (max_current + num) or start a new subarray
            # from the current number 'num' if 'num' itself is greater.
            max_current = max(num, max_current + num)
            
            # Update the overall maximum sum if the `max_current` (max sum ending at 'i')
            # is greater than the `max_global` (overall max sum found so far).
            max_global = max(max_global, max_current)
            
        return max_global

"""
Complexity Analysis for Kadane's Algorithm (Optimized Solution):

Time Complexity: O(N)
- The algorithm iterates through the input array 'nums' exactly once.
- Inside the loop, all operations (accessing an element, two comparisons, one addition)
  are constant time (O(1)).
- Therefore, the total time complexity is directly proportional to the number of elements N.

Space Complexity: O(1)
- The algorithm uses a fixed number of extra variables ('max_current', 'max_global', 'num', 'i')
  regardless of the input array's size.
- No additional data structures that grow with 'N' are used.
- This makes it an extremely efficient solution in terms of both time and space.
"""
