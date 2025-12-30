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
        using the optimized sliding window approach.

        Complexity Analysis:
        Let |s| be the length of string s (m) and |t| be the length of string t (n).

        Time Complexity:
        - Initializing `target_counts` takes `O(n)` time.
        - The two pointers `left` and `right` traverse `s`. The `right` pointer
          moves from `0` to `m-1`, visiting each character once. The `left` pointer
          also moves from `0` to `m-1`, visiting each character at most once.
        - Inside the loop, dictionary operations (get, set, increment, decrement)
          take `O(1)` on average.
        - Thus, the overall time complexity is `O(m + n)`.

        Space Complexity:
        - `target_counts`: Stores frequency of characters in `t`. At most `k`
          unique characters (where `k` is bounded by the size of the character set, e.g., 52 for English alphabet or 128 for ASCII). So `O(k)`.
        - `window_counts`: Stores frequency of characters in the current window.
          Similar to `target_counts`, `O(k)`.
        - The space complexity is `O(k)`, which can be considered `O(1)` as `k` is constant with respect to input size `m` and `n`.

        This optimized approach is efficient for large inputs.
        """
        if not t:
            return ""
        if not s:
            return ""

        # Dictionary to store the frequency of characters in t
        target_counts = collections.Counter(t)

        # Number of unique characters in t that must be present in the window
        # with at least their required frequency.
        required_chars = len(target_counts)

        # Current number of unique characters in window that meet the requirement
        formed_chars = 0

        # Dictionary to store the frequency of characters in the current window
        window_counts = collections.defaultdict(int)

        # Pointers for the sliding window
        left = 0
        min_len = float('inf')
        min_window_start = 0

        for right in range(len(s)):
            char_r = s[right]
            window_counts[char_r] += 1

            # If the character from s[right] is in t and its count in the window
            # matches its required count in t, increment formed_chars.
            if char_r in target_counts and window_counts[char_r] == target_counts[char_r]:
                formed_chars += 1

            # Try to shrink the window from the left if all required characters are found
            while formed_chars == required_chars and left <= right:
                # Update minimum window if current window is smaller
                current_window_len = right - left + 1
                if current_window_len < min_len:
                    min_len = current_window_len
                    min_window_start = left

                char_l = s[left]
                window_counts[char_l] -= 1

                # If the character removed from the left was a required character
                # and its count now falls below the target count, decrement formed_chars.
                if char_l in target_counts and window_counts[char_l] < target_counts[char_l]:
                    formed_chars -= 1

                left += 1

        if min_len == float('inf'):
            return ""
        else:
            return s[min_window_start : min_window_start + min_len]
