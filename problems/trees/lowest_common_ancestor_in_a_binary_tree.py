import collections

class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Finds the minimum element in a rotated sorted array.

        The array `nums` is originally sorted in ascending order, but it might have been
        rotated between 1 and `n` times. All elements in `nums` are unique.
        The algorithm must run in O(log n) time.

        The core idea is to use a modified binary search. In a rotated sorted array,
        the minimum element is the only element that is smaller than its predecessor
        (unless it's the first element in a non-rotated array). By comparing the
        middle element with the rightmost element, we can determine which half
        of the array contains the minimum value and discard the other half,
        thus achieving O(log n) complexity.

        Args:
            nums: A list of unique integers representing a rotated sorted array.
                  Constraints: 1 <= nums.length <= 5000
                               -5000 <= nums[i] <= 5000
                               All the integers of nums are unique.
                               nums is sorted and rotated at some pivot.

        Returns:
            The minimum element in the array.

        Raises:
            ValueError: If the input array `nums` is empty, as per problem constraints
                        nums.length >= 1. This check is kept for robustness in a general context.

        Time Complexity: O(log n) - Each iteration of the while loop effectively halves
                         the search space.
        Space Complexity: O(1) - Only a few constant extra variables are used for pointers.

        Example:
            >>> Solution().findMin([3,4,5,1,2])
            1
            >>> Solution().findMin([4,5,6,7,0,1,2])
            0
            >>> Solution().findMin([11,13,15,17])
            11
        """
        if not nums:
            raise ValueError("Input array cannot be empty. (Problem constraints: nums.length >= 1)")
            
        left, right = 0, len(nums) - 1
        
        # Optimization: If the array is not rotated at all (or rotated n times),
        # the first element is the minimum. This is identifiable if nums[left] <= nums[right].
        # This condition also efficiently handles arrays with a single element (e.g., [5]).
        if nums[left] <= nums[right]:
            return nums[left]
            
        # Binary search loop continues as long as the search space has more than one element.
        while left < right:
            mid = left + (right - left) // 2 # Calculate mid-point to prevent potential integer overflow
                                             # and ensure it leans towards the left in even-length segments.
            
            # The core logic: Compare nums[mid] with nums[right].
            # This comparison helps to identify which half is sorted and which half
            # contains the pivot (minimum element).

            # If nums[mid] > nums[right]:
            # This indicates that the minimum element must be in the right half of the array.
            # Example: `[4,5,6,7,0,1,2]`
            #   L=0, R=6, Mid=3 (val 7). `nums[3]` (7) > `nums[6]` (2).
            #   The sorted segment is `[4,5,6,7]`. The minimum `0` is in `[0,1,2]`.
            #   So, we discard `left` to `mid` and set `left = mid + 1`.
            if nums[mid] > nums[right]:
                left = mid + 1
            # If nums[mid] <= nums[right]:
            # This indicates that the minimum element is in the left half of the array,
            # or it is `nums[mid]` itself.
            # Example: `[7,0,1,2,4,5,6]`
            #   L=0, R=6, Mid=3 (val 2). `nums[3]` (2) <= `nums[6]` (6).
            #   The minimum `0` is in `[7,0,1,2]`.
            #   We keep `mid` in the search space because it could be the minimum.
            #   So, we set `right = mid`.
            # Example: `[1,2,3,4,5]` (not rotated, but this case is already handled by initial check)
            #   L=0, R=4, Mid=2 (val 3). `nums[2]` (3) <= `nums[4]` (5).
            #   Minimum `1` is in `[1,2,3]`. New R=2.
            else: # nums[mid] <= nums[right]
                right = mid
                
        # When the loop terminates, `left` will be equal to `right`.
        # This pointer will be at the index of the minimum element.
        return nums[left]

# Test Cases
if __name__ == "__main__":
    solver = Solution()

    def run_test(name, nums, expected):
        try:
            result = solver.findMin(nums)
            assert result == expected, f"FAIL: {name} - Input: {nums}, Expected: {expected}, Got: {result}"
            print(f"PASS: {name} - Input: {nums}, Result: {result}")
        except ValueError as e:
            assert "empty array" in str(e), f"FAIL: {name} - Unexpected error: {e}"
            print(f"PASS: {name} - Input: {nums}, Error: {e}")
        except AssertionError as e:
            print(e)
            
    print("--- Basic Rotated Array Tests ---")
    run_test("TC1 (Mid rotation)", [3,4,5,1,2], 1)
    run_test("TC2 (Right rotation)", [4,5,6,7,0,1,2], 0)
    run_test("TC3 (Left rotation)", [7,0,1,2,4,5,6], 0)
    run_test("TC4 (Large numbers)", [100,200,300,-10,-5,0,50], -10)
    run_test("TC5 (Different length)", [8,9,1,2,3,4,5,6,7], 1)


    print("\n--- Edge Case Tests ---")
    run_test("TC6 (Single element)", [1], 1)
    run_test("TC7 (Two elements, rotated)", [2,1], 1)
    run_test("TC8 (Two elements, not rotated)", [1,2], 1)
    run_test("TC9 (Not rotated)", [1,2,3,4,5], 1)
    run_test("TC10 (Rotated n-1 times)", [2,3,4,5,1], 1)
    run_test("TC11 (Rotated 1 time)", [5,1,2,3,4], 1)
    run_test("TC12 (Minimum at end, large array)", [10,20,30,40,50,0,1,2,3,4,5,6,7,8,9], 0)

    print("\n--- Error Handling Test ---")
    run_test("TC13 (Empty array)", [], ValueError("Input array cannot be empty."))