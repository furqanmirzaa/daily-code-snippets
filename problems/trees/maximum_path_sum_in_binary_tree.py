import collections

class Solution:
    """
    Given two strings s and t of lengths m and n respectively,
    return the minimum window substring of s such that every character in t
    (including duplicates) is included in the window.
    If there is no such window, return an empty string "".

    The test cases will be generated such that the answer is unique.
    A substring is a contiguous sequence of characters within the string.
    """
    def minWindow(self, s: str, t: str) -> str:
        """
        Finds the minimum window substring of s that contains all characters of t
        using a brute-force approach.
        """
        if not t:
            return ""
        if not s:
            return ""

        target_counts = collections.Counter(t)
        min_len = float('inf')
        min_window_start = 0

        def contains_all_chars(window_str_counts, target_str_counts):
            for char, count in target_str_counts.items():
                if window_str_counts[char] < count:
                    return False
            return True

        for i in range(len(s)):
            for j in range(i, len(s)):
                current_substring = s[i : j + 1]
                current_window_counts = collections.Counter(current_substring)

                if contains_all_chars(current_window_counts, target_counts):
                    if len(current_substring) < min_len:
                        min_len = len(current_substring)
                        min_window_start = i

        if min_len == float('inf'):
            return ""
        else:
            return s[min_window_start : min_window_start + min_len]
