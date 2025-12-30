class Solution:
    """
    Solution for the Longest Consecutive Sequence problem.

    This problem asks to find the length of the longest sequence of consecutive integers
    within an unsorted array of integers. The algorithm must run in O(n) time complexity.
    """

    def longestConsecutive(self, nums: list[int]) -> int:
        """
        Calculates the length of the longest consecutive elements sequence in an unsorted array.

        The approach leverages a hash set to achieve O(N) time complexity.
        It works by identifying potential start points of consecutive sequences and then
        extending these sequences.

        Args:
            nums: A list of unsorted integers.

        Returns:
            An integer representing the length of the longest consecutive elements sequence.

        Time Complexity:
            O(N) - Building the hash set takes O(N) time. Iterating through `nums` takes O(N) time.
            The inner `while` loop, which extends the current streak, runs for each number at most once
            across all sequences (because once a number is part of a sequence, it won't be considered
            as a 'start' again, and its successors are only checked once as part of its sequence).
            Therefore, overall, each number is visited a constant number of times (set insertion,
            checking for predecessor, and being extended).

        Space Complexity:
            O(N) - A hash set (`num_set`) is used to store all unique numbers from the input array.
            In the worst case, all numbers are unique, requiring O(N) space.
        """
        if not nums:
            return 0

        # Store all numbers in a set for O(1) average time lookups.
        num_set = set(nums)

        longest_streak = 0

        # Iterate through the original `nums` array to find potential start points of sequences.
        for num in nums:
            # A number `num` is considered the start of a consecutive sequence if `num - 1`
            # is not present in the `num_set`. This optimization prevents redundant checks
            # for numbers that are part of an already-started sequence.
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1

                # Extend the sequence as long as consecutive numbers are found in the set.
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                
                # Update the overall longest streak found so far.
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
        ([1, 1, 1, 1], 1, "All duplicates, single number sequence"),
        ([1, 3, 5, 7, 9], 1, "No consecutive numbers at all, longest is 1"),
    ]
    
    total_tests = len(test_cases)
    passed_tests = 0

    print("\n" + "=" * 50)
    print("--- Running Tests for Longest Consecutive Sequence ---")
    print("=" * 50)

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
        print("-" * 50)

    print(f"\nSummary: {passed_tests}/{total_tests} test cases passed.")
    if passed_tests == total_tests:
        print("All test cases passed successfully!")
    else:
        print("Some test cases failed. Please review the implementation.")
    print("=" * 50)