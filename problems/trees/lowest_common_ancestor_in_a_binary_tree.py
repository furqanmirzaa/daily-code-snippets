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
        """
        # Brute force approach: Iterate through the array to find the minimum.
        # This approach does not meet the O(log n) requirement.
        
        if not nums:
            raise ValueError("Input array cannot be empty.")
            
        min_element = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < min_element:
                min_element = nums[i]
        return min_element