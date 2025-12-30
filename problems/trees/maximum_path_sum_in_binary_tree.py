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

    test_cases = [
        ([100, 4, 200, 1, 3, 2], 4, "Basic example: 1,2,3,4"),
        ([], 0, "Empty array"),
        ([1], 1, "Single element array"),
        ([1, 2, 3, 4, 5], 5, "Already sorted array"),
        ([5, 4, 3, 2, 1], 5, "Reverse sorted array"),
        ([1, 2, 10, 11, 12, 13], 4, "Disjoint sequences, longest is 10,11,12,13"),
        ([1, 2, 0, 1, 3], 4, "Duplicates and order doesn't matter, longest is 0,1,2,3"),
        ([-1, 0, 1], 3, "Negative numbers sequence"),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9, "Complex mix, one long sequence 0-8"),
        ([5, 9, 2, 11, 13, 10], 3, "Mixed sequences, longest is 9,10,11"),
        ([1, 2, 2, 3, 4], 4, "Duplicates at start/middle of sequence: 1,2,3,4"),
        ([10, 1, 9, 2, 8, 3, 7, 4, 6, 5], 10, "Numbers shuffled, full sequence 1-10"),
        ([7, -9, 3, -6, 3, 5, 3, 6, -8, -4, -3, -2, 1, -7, -1, -9, 5, 5, -3, -1, -2, 0, 4], 6, "Complex mix with negative numbers, longest sequence -4 to 1"),
    ]
    
    total_tests = len(test_cases)
    passed_tests = 0

    print("--- Running Tests for Longest Consecutive Sequence ---")
    for i, (nums, expected, description) in enumerate(test_cases):
        result = sol.longestConsecutive(nums)
        print(f"\nTest Case {i+1}: {description}")
        print(f"  Input: {nums}")
        print(f"  Expected: {expected}, Got: {result}")
        try:
            assert result == expected
            print("  Status: PASSED")
            passed_tests += 1
        except AssertionError:
            print(f"  Status: FAILED - Expected {expected}, Got {result}")
        print("-" * 40)

    print(f"\nSummary: {passed_tests}/{total_tests} test cases passed.")
    if passed_tests == total_tests:
        print("All test cases passed successfully!")
    else:
        print("Some test cases failed. Please review the implementation.")