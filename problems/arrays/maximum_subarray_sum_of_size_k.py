import sys

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        """
        Finds the contiguous subarray within a given integer array `nums` that has the largest sum.
        
        This problem is a classic application of Kadane's Algorithm, which efficiently solves
        the maximum subarray sum problem using dynamic programming principles.
        
        A subarray is defined as a contiguous non-empty sequence of elements.
        
        Algorithm (Kadane's):
        The algorithm iterates through the array once, maintaining two key variables:
        1. `max_current`: This variable stores the maximum sum of a subarray that *ends* at the
           current element being processed. It is updated by deciding whether to extend the
           previous subarray (`max_current + current_element`) or to start a new subarray
           from the `current_element` itself. The choice is `max(current_element, max_current + current_element)`.
        2. `max_global`: This variable stores the overall maximum sum found across *all* subarrays
           processed so far. It is updated whenever `max_current` becomes greater than the
           current `max_global` value. The choice is `max(max_global, max_current)`.
           
        Initialization:
        Problem constraints (e.g., 1 <= nums.length <= 10^5) typically guarantee that `nums` is
        non-empty. Therefore, both `max_current` and `max_global` can be safely initialized
        with the first element of the array (`nums[0]`).

        Args:
            nums: A list of integers. Representing the input array.
                  Constraints: 1 <= nums.length <= 10^5
                               -10^4 <= nums[i] <= 10^4

        Returns:
            An integer representing the maximum sum of any contiguous subarray within `nums`.

        Time Complexity: O(N)
            The algorithm processes each element of the input array `nums` exactly once.
            Inside the loop, all operations (element access, addition, and two comparisons)
            are constant time (O(1)). Therefore, the total time complexity is linear
            with respect to the number of elements N in `nums`.

        Space Complexity: O(1)
            The algorithm uses a fixed amount of extra space for a few variables
            (`max_current`, `max_global`, `num`, `i`), regardless of the input array's size.
            No additional data structures that grow with the input size are allocated.
        """
        
        # Initialize max_current and max_global with the first element of the array.
        # This is safe due to the problem constraints guaranteeing a non-empty array.
        max_current: int = nums[0]  # Maximum sum of a subarray ending at the current position
        max_global: int = nums[0]   # Overall maximum sum found so far across all subarrays

        # Iterate through the array starting from the second element (index 1).
        # The first element's impact is already captured by the initializations.
        for i in range(1, len(nums)):
            num: int = nums[i]
            
            # Update `max_current`:
            # A subarray ending at `num` either starts at `num` itself, or extends
            # the maximum subarray ending at the previous element.
            max_current = max(num, max_current + num)
            
            # Update `max_global`:
            # The overall maximum sum is the greater of the current `max_global` and
            # the `max_current` sum ending at the current position.
            max_global = max(max_global, max_current)
            
        return max_global


# --- Test Cases and Execution Framework ---
def run_tests():
    """
    Executes a suite of test cases for the `maxSubArray` function.
    Prints detailed results for each test and provides a summary.
    """
    solver = Solution()
    
    # Each test case is defined as a tuple: (input_nums, expected_output, description)
    test_cases = [
        # Standard Test Cases (from problem examples or common scenarios)
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6, "Example from problem description: [4, -1, 2, 1]"),
        ([1, 2, 3], 6, "All positive numbers: [1, 2, 3]"),
        ([-1, -2, -3], -1, "All negative numbers: [-1] (the largest single negative)"),
        ([1, -2, 3, -1, 2], 4, "Mixed positive/negative, max subarray in middle: [3, -1, 2]"),
        ([5, 4, -1, 7, 8], 23, "Sequence with increasing sum: [5, 4, -1, 7, 8]"),

        # Edge Cases
        ([5], 5, "Single positive element array"),
        ([-10], -10, "Single negative element array"),
        ([0], 0, "Single zero element array"),
        ([0, 0, 0], 0, "Array of zeros"),
        ([1, -1, 1, -1, 1], 1, "Alternating positive/negative, max is a single element"),
        ([7, -3, 10, -4, 2, 1, -9, 8], 14, "Complex mixed array with peak sum: [7, -3, 10]"),
        ([2, -3, 4, -1, -2, 1, 5, -3], 7, "Max subarray spanning multiple segments: [4, -1, -2, 1, 5]"),
        ([-5, -1, -2, -3, -4], -1, "Another all negative, max is largest negative"),
        ([10, -100, 5, 1, 2], 8, "Max after a very large drop: [5, 1, 2]")
    ]

    print("\n--- Running maxSubArray Test Suite ---\n")
    all_passed = True
    for i, (nums, expected, description) in enumerate(test_cases):
        try:
            result = solver.maxSubArray(nums)
            status = "PASSED" if result == expected else "FAILED"
            test_info = f"Test {i+1} [{description}]\n  Input: {nums}\n  Expected: {expected}, Got: {result} -- {status}"
            print(test_info)
            
            if result != expected:
                all_passed = False
                print("  " + "!"*50)
                
        except Exception as e:
            all_passed = False
            error_info = f"Test {i+1} [{description}]\n  Input: {nums}\n  ERROR: An unexpected exception occurred: {e}"
            print(error_info)
            print("  " + "!"*50)
            
        print("-"*60)

    if all_passed:
        print("\nAll 🚀 test cases passed successfully! The solution is robust.")
    else:
        print("\nSome ❌ test cases failed. Please review the implementation.")
        sys.exit(1) # Exit with a non-zero status code to indicate test failures

if __name__ == "__main__":
    run_tests()
