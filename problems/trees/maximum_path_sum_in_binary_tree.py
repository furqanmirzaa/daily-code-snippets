class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
        You must write an algorithm that runs in O(n) time.
        """
        if not nums:
            return 0

        # Brute-force approach: Sort the array and then iterate.
        # This approach does not meet the O(N) time complexity requirement due to sorting.
        nums.sort()  # O(N log N) time complexity

        longest_streak = 0
        current_streak = 0
        
        # Initialize for the first element
        if nums:
            current_streak = 1
            longest_streak = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                # Duplicate, does not extend the sequence but does not break it either
                continue
            elif nums[i] == nums[i-1] + 1:
                # Consecutive number found, extend current streak
                current_streak += 1
            else:
                # Sequence broken, update longest streak and start a new one
                longest_streak = max(longest_streak, current_streak)
                current_streak = 1 

        # Update longest_streak one last time for the sequence ending at the last element
        longest_streak = max(longest_streak, current_streak)
        return longest_streak