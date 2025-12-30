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
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest_streak = max(longest_streak, current_streak)
        
        return longest_streak

# Test cases
if __name__ == "__main__":
    sol = Solution()

    print("--- Running Basic Tests ---")

    # Test Case 1: Basic example
    nums1 = [100, 4, 200, 1, 3, 2]
    expected1 = 4 # Sequence: 1, 2, 3, 4
    result1 = sol.longestConsecutive(nums1)
    print(f"Input: {nums1}, Expected: {expected1}, Got: {result1}")
    assert result1 == expected1, f"Test Case 1 Failed: Expected {expected1}, Got {result1}"

    # Test Case 2: Empty array
    nums2 = []
    expected2 = 0
    result2 = sol.longestConsecutive(nums2)
    print(f"Input: {nums2}, Expected: {expected2}, Got: {result2}")
    assert result2 == expected2, f"Test Case 2 Failed: Expected {expected2}, Got {result2}"

    # Test Case 3: Single element
    nums3 = [1]
    expected3 = 1
    result3 = sol.longestConsecutive(nums3)
    print(f"Input: {nums3}, Expected: {expected3}, Got: {result3}")
    assert result3 == expected3, f"Test Case 3 Failed: Expected {expected3}, Got {result3}"

    # Test Case 4: Already sorted array
    nums4 = [1, 2, 3, 4, 5]
    expected4 = 5
    result4 = sol.longestConsecutive(nums4)
    print(f"Input: {nums4}, Expected: {expected4}, Got: {result4}")
    assert result4 == expected4, f"Test Case 4 Failed: Expected {expected4}, Got {result4}"

    # Test Case 5: Reverse sorted array
    nums5 = [5, 4, 3, 2, 1]
    expected5 = 5
    result5 = sol.longestConsecutive(nums5)
    print(f"Input: {nums5}, Expected: {expected5}, Got: {result5}")
    assert result5 == expected5, f"Test Case 5 Failed: Expected {expected5}, Got {result5}"
    
    # Test Case 6: Disjoint sequences
    nums6 = [1, 2, 10, 11, 12, 13]
    expected6 = 4 # Sequence: 10, 11, 12, 13
    result6 = sol.longestConsecutive(nums6)
    print(f"Input: {nums6}, Expected: {expected6}, Got: {result6}")
    assert result6 == expected6, f"Test Case 6 Failed: Expected {expected6}, Got {result6}"

    # Test Case 7: Duplicates - should not affect length
    nums7 = [1, 2, 0, 1, 3]
    expected7 = 4 # Sequence: 0, 1, 2, 3
    result7 = sol.longestConsecutive(nums7)
    print(f"Input: {nums7}, Expected: {expected7}, Got: {result7}")
    assert result7 == expected7, f"Test Case 7 Failed: Expected {expected7}, Got {result7}"

    print("\nAll basic test cases passed!")