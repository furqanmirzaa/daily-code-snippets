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

        Time Complexity: O(log n) - Each step of binary search reduces the search space by half.
        Space Complexity: O(1) - We only use a few extra variables for pointers.
        """
        if not nums:
            raise ValueError("Input array cannot be empty.")
            
        left, right = 0, len(nums) - 1
        
        while left < right: # Loop until left and right pointers meet
            mid = left + (right - left) // 2
            
            # If nums[mid] > nums[right], it means the pivot (minimum) is in the right part (mid+1 to right).
            # Example: [4,5,6,7,0,1,2]
            #   L=0, R=6, Mid=3 (val 7). nums[3] (7) > nums[6] (2). So min is in [0,1,2].
            #   New L=4.
            # Example: [3,4,5,1,2]
            #   L=0, R=4, Mid=2 (val 5). nums[2] (5) > nums[4] (2). So min is in [1,2].
            #   New L=3.
            if nums[mid] > nums[right]:
                left = mid + 1
            # If nums[mid] <= nums[right], it means the pivot (minimum) is in the left part (left to mid).
            # It could be nums[mid] itself, or something to its left.
            # Example: [7,0,1,2,4,5,6]
            #   L=0, R=6, Mid=3 (val 2). nums[3] (2) <= nums[6] (6). So min is in [7,0,1,2].
            #   New R=3.
            # Example: [1,2,3,4,5] (not rotated)
            #   L=0, R=4, Mid=2 (val 3). nums[2] (3) <= nums[4] (5). So min is in [1,2,3].
            #   New R=2.
            else: # nums[mid] <= nums[right]
                right = mid
                
        # When left == right, we have found the minimum element.
        return nums[left]

# Test Cases
if __name__ == "__main__":
    solver = Solution()

    # Basic rotated arrays
    print(f"Test Case 1: [3,4,5,1,2] -> Expected: 1, Got: {solver.findMin([3,4,5,1,2])}")
    print(f"Test Case 2: [4,5,6,7,0,1,2] -> Expected: 0, Got: {solver.findMin([4,5,6,7,0,1,2])}")
    print(f"Test Case 3: [11,13,15,17] -> Expected: 11, Got: {solver.findMin([11,13,15,17])}")
    print(f"Test Case 4: [7,0,1,2,4,5,6] -> Expected: 0, Got: {solver.findMin([7,0,1,2,4,5,6])}")