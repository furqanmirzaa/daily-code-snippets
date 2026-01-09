class Solution:
    def findMin(self, nums: list[int]) -> int:
        """
        Finds the minimum element in a rotated sorted array.

        The array `nums` is originally sorted in ascending order, but it might have been
        rotated between 1 and `n` times. All elements in `nums` are unique.
        The algorithm must run in O(log n) time.

        Args:
            nums: A list of unique integers representing a rotated sorted array.

        Returns:
            The minimum element in the array.

        Raises:
            ValueError: If the input array `nums` is empty.

        Example:
            >>> Solution().findMin([3,4,5,1,2])
            1
            >>> Solution().findMin([4,5,6,7,0,1,2])
            0
            >>> Solution().findMin([11,13,15,17])
            11
        """
        # Handle edge case for an empty array
        if not nums:
            raise ValueError("Input array cannot be empty.")
            
        left, right = 0, len(nums) - 1
        
        # Optimization: If the array is not rotated at all (or rotated n times),
        # the first element is the minimum. This is identifiable if nums[left] <= nums[right].
        # This also efficiently handles arrays with a single element (e.g., [5]).
        if nums[left] <= nums[right]:
            return nums[left]
            
        # Perform binary search to find the minimum element
        # The loop continues as long as the search space has more than one element (left < right).
        while left < right:
            mid = left + (right - left) // 2 # Calculate mid-point to prevent potential integer overflow
                                             # and ensure it leans towards the left in even-length segments.
            
            # The core logic: Compare nums[mid] with nums[right].
            # This comparison helps to identify which half is sorted and which half
            # contains the pivot (minimum element).

            # If nums[mid] > nums[right]:
            # This implies that the minimum element must be in the right half of the array
            # (from mid + 1 to right). The left half (left to mid) is sorted in increasing order,
            # but the overall segment (left to right) is rotated. Thus, the minimum must be after mid.
            # Example: [4,5,6,7,0,1,2]
            #   L=0, R=6, Mid=3 (val 7). Here, nums[3] (7) > nums[6] (2).
            #   The sorted segment is `[4,5,6,7]`. The minimum `0` is in `[0,1,2]` which is to the right.
            #   So, we discard the left half including mid and set `left = mid + 1`.
            if nums[mid] > nums[right]:
                left = mid + 1
            # If nums[mid] <= nums[right]:
            # This implies that the minimum element is in the left half of the array (from left to mid),
            # or it is `nums[mid]` itself. We cannot discard `mid` as it might be the minimum.
            # Example: [7,0,1,2,4,5,6]
            #   L=0, R=6, Mid=3 (val 2). Here, nums[3] (2) <= nums[6] (6).
            #   The minimum `0` is in `[7,0,1,2]` which is to the left (or at mid).
            #   So, we narrow the search to the left half including mid and set `right = mid`.
            # Example: [1,2,3,4,5] (not rotated, but this case is also handled by initial check)
            #   L=0, R=4, Mid=2 (val 3). Here, nums[2] (3) <= nums[4] (5).
            #   Minimum `1` is in `[1,2,3]`. New R=2.
            else: # nums[mid] <= nums[right]
                right = mid
                
        # The loop terminates when left == right. At this point, `left` (or `right`)
        # points to the minimum element in the array.
        return nums[left]

# Test Cases
if __name__ == "__main__":
    solver = Solution()

    print("--- Basic Test Cases ---")
    print(f"Test Case 1: [3,4,5,1,2] -> Expected: 1, Got: {solver.findMin([3,4,5,1,2])}")
    print(f"Test Case 2: [4,5,6,7,0,1,2] -> Expected: 0, Got: {solver.findMin([4,5,6,7,0,1,2])}")
    print(f"Test Case 3: [11,13,15,17] -> Expected: 11, Got: {solver.findMin([11,13,15,17])}")
    print(f"Test Case 4: [7,0,1,2,4,5,6] -> Expected: 0, Got: {solver.findMin([7,0,1,2,4,5,6])}")

    print("\n--- Edge Cases ---")
    # Array with one element
    print(f"Test Case 5: [1] -> Expected: 1, Got: {solver.findMin([1])}")
    # Array with two elements, rotated
    print(f"Test Case 6: [2,1] -> Expected: 1, Got: {solver.findMin([2,1])}")
    # Array with two elements, not rotated
    print(f"Test Case 7: [1,2] -> Expected: 1, Got: {solver.findMin([1,2])}")
    # Array not rotated (e.g., [1,2,3,4,5], handled by initial condition and also by loop)
    print(f"Test Case 8: [1,2,3,4,5] -> Expected: 1, Got: {solver.findMin([1,2,3,4,5])}")
    # Array rotated n-1 times
    print(f"Test Case 9: [2,3,4,5,1] -> Expected: 1, Got: {solver.findMin([2,3,4,5,1])}")

    print("\n--- Error Handling Test ---")
    # Test for ValueError (empty array)
    try:
        solver.findMin([])
    except ValueError as e:
        print(f"Test Case 10: Empty array -> Expected: ValueError, Got: {e}")
    else:
        print("Test Case 10 failed: Expected ValueError for empty array, but no error raised.")