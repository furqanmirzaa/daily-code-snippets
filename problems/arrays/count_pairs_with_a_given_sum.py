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

    # Example 1 from problem description
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    expected1 = sorted([["bat"],["nat","tan"],["ate","eat","tea"]], key=lambda x: sorted(x[0])) # Sorting for consistent comparison
    result1 = sorted([sorted(group) for group in sol.groupAnagrams(strs1)], key=lambda x: x[0])
    
    # The problem states return in any order, so we need to sort the result for comparison
    # Sort inner lists and then sort the outer list based on the first element of each inner list
    assert result1 == sorted([["bat"],["nat","tan"],["ate","eat","tea"]], key=lambda x: x[0]), f"Test Case 1 Failed: {result1}"

    # Example 2 from problem description
    strs2 = [""]
    result2 = sol.groupAnagrams(strs2)
    assert result2 == [[""]], f"Test Case 2 Failed: {result2}"

    # Example 3 from problem description
    strs3 = ["a"]
    result3 = sol.groupAnagrams(strs3)
    assert result3 == [["a"]], f"Test Case 3 Failed: {result3}"

    print("All basic test cases passed!")

if __name__ == "__main__":
    test_solution()