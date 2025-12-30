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

        Complexity Analysis:
        Let |s| be the length of string s (m) and |t| be the length of string t (n).

        Time Complexity:
        - The outer loop iterates from `i = 0` to `m-1`.
        - The inner loop iterates from `j = i` to `m-1`. This results in `O(m^2)` possible substrings.
        - Inside the inner loop:
            - Slicing `s[i : j + 1]` takes `O(m)` time in the worst case.
            - `collections.Counter(current_substring)` takes `O(m)` time to build the frequency map for the current substring.
            - `contains_all_chars` iterates over `target_counts`, which has at most `k` unique characters (where `k` is at most 52 for English alphabet or 128 for ASCII). This takes `O(k)` time.
        - Therefore, the total time complexity is approximately `O(m^2 * (m + k))` which simplifies to `O(m^3)` in the worst case if we consider `k` as a constant, or more precisely `O(m^2 * m + m^2 * k)`.
          This approach is too slow for typical constraints (e.g., m up to 10^5).

        Space Complexity:
        - `target_counts`: `O(k)` where `k` is the number of unique characters in `t`.
        - `current_window_counts`: `O(k)` for each substring.
        - The space required for the substring `current_substring` is `O(m)`.
        - Overall, the space complexity is `O(m + k)`.

        This brute-force approach is highly inefficient for large inputs.
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
