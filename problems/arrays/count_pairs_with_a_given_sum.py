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
        # The core idea is that anagrams have the same canonical representation.
        # A simple canonical representation for a string is its sorted form.
        # We can use this sorted representation as a key in a hash map (dictionary).
        # The values associated with each key will be a list of original strings that
        # share that same sorted form, meaning they are anagrams of each other.

        # defaultdict(list) automatically creates an empty list for a key if it doesn't exist yet.
        anagram_map = defaultdict(list)

        for s in strs:
            # Sort the string to get its canonical representation (e.g., "eat", "tea", "ate" all become "aet")
            # Using ''.join(sorted(s)) to convert the sorted list of characters back into a string key.
            sorted_s_key = "".join(sorted(s))
            
            # Append the original string 's' to the list associated with its sorted key
            anagram_map[sorted_s_key].append(s)

        # The values of the hash map are the desired groups of anagrams.
        # Convert the dictionary values (lists of anagrams) into a list of lists.
        return list(anagram_map.values())

        # --- Complexity Analysis for Optimized Solution ---
        # Time Complexity:
        # We iterate through N strings in the input list.
        # For each string, we sort it. If K is the maximum length of a string, sorting takes O(K log K).
        # Inserting into a hash map (or appending to a list within a hash map) takes O(K) on average
        # (due to string hashing and potential string copy for storage).
        # Total time complexity: O(N * K log K).
        # This is generally much better than O(N^2 * K log K) if N is large.

        # Space Complexity:
        # The hash map stores N strings in total.
        # Each key is a sorted string (max length K), and each value is a list of original strings.
        # In the worst case, all strings are unique, so the map stores N keys and N strings.
        # Total space complexity: O(N * K) to store the hash map and its contents.