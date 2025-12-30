class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
        This algorithm runs in O(N) time, fulfilling the problem requirements.

        Optimized approach using a HashSet:
        1. Store all unique numbers from `nums` into a hash set (`num_set`).
           This step takes O(N) time and O(N) space.
        2. Initialize `longest_streak = 0`.
        3. Iterate through each `num` in the original `nums` array:
           a. Check if `num - 1` is NOT in `num_set`. If it's not, then `num` is a potential start of a new consecutive sequence.
              (This is the key optimization: we only start counting a sequence from its absolute beginning).
           b. If `num` is a potential start, initialize `current_num = num` and `current_streak = 1`.
           c. While `current_num + 1` IS in `num_set`, increment `current_num` and `current_streak`.
              This extends the current consecutive sequence.
           d. After the inner `while` loop finishes (meaning the sequence has ended), update `longest_streak`:
              `longest_streak = max(longest_streak, current_streak)`.
        Overall Time Complexity: O(N).
          Each number is added to the set once (O(N)). Then, for each number, it's checked if it's a sequence start. The inner while loop runs for each number only if it's part of a sequence that started with `num` (and its predecessor wasn't in the set). Crucially, each number is visited at most a constant number of times (set insertion, `(num-1) in num_set` check, and being incremented in the `while` loop). Thus, the total operations remain proportional to N.
        Overall Space Complexity: O(N) to store the numbers in the hash set.
        """
        if not nums:
            return 0

        num_set = set(nums)  # O(N) time, O(N) space to build the set of unique numbers

        longest_streak = 0

        for num in nums:
            # Check if `num` is the start of a sequence (i.e., `num - 1` is not present).
            # This prevents re-checking sequences from their middle elements.
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # Extend the sequence as long as consecutive numbers are found in the set.
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the maximum streak found so far.
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak