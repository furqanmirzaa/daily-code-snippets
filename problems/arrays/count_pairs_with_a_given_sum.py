from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together from a given list of strings.

        An Anagram is a word or phrase formed by rearranging the letters of a
        different word or phrase, typically using all the original letters exactly once.

        The solution uses a hash map (dictionary) where the keys are the sorted
        (canonical) form of the strings, and the values are lists of the original
        strings that share that canonical form.

        Args:
            strs: A list of strings.

        Returns:
            A list of lists of strings, where each inner list contains a group
            of anagrams. The order of inner lists and strings within them does
            not matter.

        Time Complexity:
            O(N * K log K)
            - N is the number of strings in the input list `strs`.
            - K is the maximum length of a string in `strs`.
            - For each of the N strings, we sort it, which takes O(K log K) time.
            - Joining the sorted characters back into a string takes O(K).
            - Hash map insertion (key creation and list append) takes O(K) on average
              (due to string hashing and potential string copy).
            - The overall complexity is dominated by sorting all strings.

        Space Complexity:
            O(N * K)
            - N is the number of strings in the input list `strs`.
            - K is the maximum length of a string in `strs`.
            - In the worst case, all strings are unique (no anagrams), so the hash map
              stores N keys (each of length K) and N original strings (each of length K).
            - The space for storing the `anagram_map` and its contents scales with N*K.
        """
        # Initialize a defaultdict where the default value for a new key is an empty list.
        # This allows us to directly append strings without checking if the key exists first.
        anagram_map = defaultdict(list)

        # Iterate through each string in the input list
        for s in strs:
            # 1. Create a canonical key for the string:
            #    - Convert the string to a list of characters.
            #    - Sort the list of characters (e.g., 'eat' -> ['a', 'e', 't']).
            #    - Join the sorted characters back into a string (e.g., ['a', 'e', 't'] -> 'aet').
            #    All anagrams will produce the same sorted string key.
            sorted_s_key = "".join(sorted(s))
            
            # 2. Add the original string to the list associated with its canonical key:
            #    The defaultdict ensures that if sorted_s_key is new, an empty list is created
            #    before 's' is appended.
            anagram_map[sorted_s_key].append(s)

        # 3. Extract the groups of anagrams:
        #    The values of the `anagram_map` are the lists of strings that are anagrams
        #    of each other. Convert these values to a list of lists.
        return list(anagram_map.values())

# --- Test Cases ---
# Helper function to sort results for consistent comparison, as the problem allows any order.
# It sorts the inner lists alphabetically and then sorts the outer list based on the first element of each inner list.
def sort_result(result_list: List[List[str]]) -> List[List[str]]:
    return sorted([sorted(group) for group in result_list], key=lambda x: x[0] if x else '')

def test_solution():
    sol = Solution()

    # Test Case 1: Example from problem (multiple anagrams)
    strs1 = ["eat","tea","tan","ate","nat","bat"]
    expected1 = sort_result([["bat"],["nat","tan"],["ate","eat","tea"]])
    result1 = sort_result(sol.groupAnagrams(strs1))
    assert result1 == expected1, f"Test Case 1 Failed: Input: {strs1}, Expected: {expected1}, Got: {result1}"

    # Test Case 2: Single empty string
    strs2 = [""]
    expected2 = sort_result([[""]])
    result2 = sort_result(sol.groupAnagrams(strs2))
    assert result2 == expected2, f"Test Case 2 Failed: Input: {strs2}, Expected: {expected2}, Got: {result2}"

    # Test Case 3: Single character string
    strs3 = ["a"]
    expected3 = sort_result([["a"]])
    result3 = sort_result(sol.groupAnagrams(strs3))
    assert result3 == expected3, f"Test Case 3 Failed: Input: {strs3}, Expected: {expected3}, Got: {result3}"

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

    # Additional Test Case 8: Longer list with mixed cases of anagrams and non-anagrams
    strs8 = ["zone", "done", "noez", "node", "apple", "ppale", "aple", "melon"]
    expected8 = sort_result([
        ["zone", "noez"],
        ["done", "node"],
        ["apple", "ppale"],
        ["aple"],
        ["melon"]
    ])
    result8 = sort_result(sol.groupAnagrams(strs8))
    assert result8 == expected8, f"Additional Test Case 8 Failed: Input: {strs8}, Expected: {expected8}, Got: {result8}"

    # Additional Test Case 9: Strings with duplicate characters
    strs9 = ["aab", "baa", "bba", "abb"]
    expected9 = sort_result([["aab", "baa", "abb"], ["bba"]])
    result9 = sort_result(sol.groupAnagrams(strs9))
    assert result9 == expected9, f"Additional Test Case 9 Failed: Input: {strs9}, Expected: {expected9}, Got: {result9}"

    print("All test cases and edge cases passed successfully!")

if __name__ == "__main__":
    test_solution()