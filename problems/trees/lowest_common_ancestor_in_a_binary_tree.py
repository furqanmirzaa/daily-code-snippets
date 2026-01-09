class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Problem: Find Minimum in Rotated Sorted Array
        Category: Arrays, Binary Search
        Difficulty: Medium
        Description: Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
        For example, the array nums = [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2] if it was rotated 4 times.
        Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], ..., a[n-2]].
        Given the sorted rotated array nums of unique elements, return the minimum element of this array.
        You must write an algorithm that runs in O(log n) time.

        Time Complexity: O(log n) - Each step of binary search reduces the search space by half.
        Space Complexity: O(1) - We only use a few extra variables for pointers.
        """
        if not nums:
            raise ValueError("Input array cannot be empty.")
            
        left, right = 0, len(nums) - 1
        
        # The key idea: The minimum element is the only one that breaks the "sorted" property
        # (i.e., nums[i] < nums[i-1]) or is the first element if the array is not rotated.

        # We use a binary search to continuously narrow down the search space.
        while left < right: # Loop until left and right pointers meet
            mid = left + (right - left) // 2 # Calculate mid-point to prevent overflow
            
            # If nums[mid] > nums[right], it means the pivot (minimum element)
            # is located in the right half of the current search space (from mid + 1 to right).
            # This is because the left half (left to mid) is still sorted and increasing,
            # but the overall segment (left to right) is rotated, meaning the minimum must be after mid.
            # Example: [4,5,6,7,0,1,2]
            #   L=0, R=6, Mid=3 (val 7). nums[3] (7) > nums[6] (2). The minimum (0) is in [0,1,2].
            #   So, we eliminate the left half including mid. New L becomes 4.
            if nums[mid] > nums[right]:
                left = mid + 1
            # If nums[mid] <= nums[right], it means the pivot (minimum element)
            # is located in the left half of the current search space (from left to mid).
            # It could be nums[mid] itself, or an element to its left.
            # We keep `mid` in the search space because it might be the minimum.
            # Example: [7,0,1,2,4,5,6]
            #   L=0, R=6, Mid=3 (val 2). nums[3] (2) <= nums[6] (6). The minimum (0) is in [7,0,1,2].
            #   So, we narrow the search to the left half including mid. New R becomes 3.
            # Example: [1,2,3,4,5] (not rotated)
            #   L=0, R=4, Mid=2 (val 3). nums[2] (3) <= nums[4] (5). The minimum (1) is in [1,2,3].
            #   New R=2.
            else: # nums[mid] <= nums[right]
                right = mid
                
        # When the loop terminates, `left` will be equal to `right`. At this point,
        # `left` (or `right`) points to the minimum element in the array.
        return nums[left]