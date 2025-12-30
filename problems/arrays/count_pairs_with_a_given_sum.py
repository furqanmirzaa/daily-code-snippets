from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Problem: Group Anagrams
        # Category: Array, Hash Table, String, Sorting
        # Difficulty: Medium
        # Description: Given an array of strings `strs`, group the anagrams together.
        # You can return the answer in any order. An Anagram is a word or phrase formed by rearranging
        # the letters of a different word or phrase, typically using all the original letters exactly once.

        # --- Brute-Force Solution with Complexity Analysis ---
        # The idea is to iterate through each string and, for each unvisited string,
        # compare it with all subsequent unvisited strings to find its anagrams.
        # Anagrams can be identified by sorting the characters of both strings and comparing the sorted results.

        n = len(strs)
        result = []
        visited = [False] * n # Keep track of strings that have already been grouped

        # Time Complexity:
        # Outer loop runs N times (where N is the number of strings).
        # Inner loop runs up to N times.
        # Inside the inner loop, `sorted(s)` takes O(K log K) time, where K is the maximum length of a string.
        # Comparing two sorted strings also takes O(K) time.
        # So, the anagram check is O(K log K).
        # Total time complexity: O(N * N * K log K) = O(N^2 * K log K).

        # Space Complexity:
        # `visited` array takes O(N) space.
        # Storing `result` could take up to O(N * K) space in the worst case (all strings are unique and stored).
        # `sorted(s)` creates temporary strings, taking O(K) space.
        # Total space complexity: O(N + N*K) = O(N*K).

        for i in range(n):
            if visited[i]:
                continue # Skip strings already processed

            current_group = [strs[i]]
            visited[i] = True

            # Compare strs[i] with all subsequent unvisited strings
            for j in range(i + 1, n):
                if not visited[j]:
                    # Check if strs[i] and strs[j] are anagrams by sorting them
                    if sorted(strs[i]) == sorted(strs[j]):
                        current_group.append(strs[j])
                        visited[j] = True
            result.append(current_group)

        return result