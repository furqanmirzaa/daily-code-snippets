class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
        You must write an algorithm that runs in O(n) time.

        Brute-force approach (current implementation):
        1. Sort the array: This takes O(N log N) time.
        2. Iterate through the sorted array to find consecutive sequences: This takes O(N) time.
        Overall Time Complexity: O(N log N) due to the sorting step.
        Overall Space Complexity: O(1) or O(log N) depending on the sort implementation (e.g., Python's Timsort uses O(N) worst-case space, O(log N) average).
        This approach does NOT meet the O(N) time complexity requirement specified in the problem.
        """
        if not nums:
            return 0

        nums.sort()  # O(N log N) time complexity

        longest_streak = 0
        current_streak = 0
        
        if nums: # nums is guaranteed not empty due to previous check
            current_streak = 1
            longest_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                current_streak += 1
            else:
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1 

        longest_streak = max(longest_streak, current_streak)
        return longest_streak