from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Problem: Group Anagrams
        # Category: Array, Hash Table, String, Sorting
        # Difficulty: Medium
        # Description: Given an array of strings `strs`, group the anagrams together.
        # You can return the answer in any order. An Anagram is a word or phrase formed by rearranging
        # the letters of a different word or phrase, typically using all the original letters exactly once.

        # --- Optimized Solution: Using a Hash Map (Dictionary) ---
        anagram_map = defaultdict(list)

        for s in strs:
            sorted_s_key = "".join(sorted(s))
            anagram_map[sorted_s_key].append(s)

        return list(anagram_map.values())

# --- Test Cases --- 

def test_solution():
    sol = Solution()

    # Helper function to sort results for consistent comparison, as order doesn't matter
    def sort_result(result_list: List[List[str]]) -> List[List[str]]:
        return sorted([sorted(group) for group in result_list], key=lambda x: x[0] if x else '')

    # Test Case 1: Example from problem (multiple anagrams)
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    expected1 = sort_result([["bat"],["nat","tan"],["ate","eat","tea"]])
    result1 = sort_result(sol.groupAnagrams(strs1))
    assert result1 == expected1, f"Test Case 1 Failed: Input: {strs1}, Expected: {expected1}, Got: {result1}"

    # Test Case 2: Empty string
    strs2 = [""]
    expected2 = sort_result([[""]])
    result2 = sort_result(sol.groupAnagrams(strs2))
    assert result2 == expected2, f"Test Case 2 Failed: Input: {strs2}, Expected: {expected2}, Got: {result2}"

    # Test Case 3: Single character string
    strs3 = ["a"]
    expected3 = sort_result([["a"]])
    result3 = sort_result(sol.groupAnagrams(strs3))
    assert result3 == expected3, f"Test Case 3 Failed: Input: {strs3}, Expected: {expected3}, Got: {result3}"

    # --- Edge Cases ---

    # Edge Case 4: Empty input list
    strs4 = []
    expected4 = []
    result4 = sol.groupAnagrams(strs4)
    assert result4 == expected4, f"Edge Case 4 Failed: Input: {strs4}, Expected: {expected4}, Got: {result4}"

    # Edge Case 5: All unique strings (no anagrams)
    strs5 = ["abc", "def", "ghi"]
    expected5 = sort_result([["abc"],["def"],["ghi"]])
    result5 = sort_result(sol.groupAnagrams(strs5))
    assert result5 == expected5, f"Edge Case 5 Failed: Input: {strs5}, Expected: {expected5}, Got: {result5}"

    # Edge Case 6: All strings are anagrams of each other
    strs6 = ["arc", "car", "rac"]
    expected6 = sort_result([["arc", "car", "rac"]])
    result6 = sort_result(sol.groupAnagrams(strs6))
    assert result6 == expected6, f"Edge Case 6 Failed: Input: {strs6}, Expected: {expected6}, Got: {result6}"

    # Edge Case 7: Strings with varying lengths, some anagrams, some not
    strs7 = ["listen", "silent", "hello", "ehllo", "top"]
    expected7 = sort_result([["listen", "silent"], ["hello", "ehllo"], ["top"]])
    result7 = sort_result(sol.groupAnagrams(strs7))
    assert result7 == expected7, f"Edge Case 7 Failed: Input: {strs7}, Expected: {expected7}, Got: {result7}"

    print("All test cases and edge cases passed!")

if __name__ == "__main__":
    test_solution()