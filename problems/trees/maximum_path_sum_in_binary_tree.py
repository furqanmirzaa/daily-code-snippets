import collections
import unittest
from typing import Dict, DefaultDict

class Solution:
    """
    Solution for the Minimum Window Substring problem.

    Given two strings `s` and `t` of lengths `m` and `n` respectively,
    return the minimum window substring of `s` such that every character in `t`
    (including duplicates) is included in the window.
    If there is no such window, return an empty string "".

    The problem guarantees that the answer will be unique if one exists.
    A substring is a contiguous sequence of characters within the string.
    """
    def minWindow(self, s: str, t: str) -> str:
        """
        Finds the minimum window substring of `s` that contains all characters of `t`.

        This algorithm employs a two-pointer (left and right) sliding window approach.
        It systematically expands the window using the `right` pointer and then,
        when a valid window is found (containing all characters from `t` with required frequencies),
        it attempts to contract the window from the `left` to find the smallest valid one.
        Frequency maps (`target_counts` and `window_counts`) are used to efficiently
        track character occurrences and validate window contents.

        Args:
            s: The main string in which to search for the window.
            t: The target string defining the characters and their required frequencies
               that must be present in the window.

        Returns:
            The smallest substring of `s` that contains all characters of `t`.
            Returns an empty string ("") if no such window is found.

        Time Complexity: O(|s| + |t|)
        - Initializing `target_counts` takes O(|t|) time.
        - Both `left` and `right` pointers traverse `s` at most once. Each character
          in `s` is processed by the `right` pointer once (added to window) and by
          the `left` pointer once (removed from window).
        - Dictionary operations (access, insert, delete) take O(1) on average.
        - Therefore, the overall time complexity is linear with respect to the
          lengths of `s` and `t`.

        Space Complexity: O(k)
        - `target_counts`: Stores frequency of characters in `t`. At most `k`
          unique characters, where `k` is the size of the character set (e.g., 52 for
          English alphabet, 128 for ASCII, 256 for extended ASCII).
        - `window_counts`: Stores frequency of characters in the current window.
          Similar to `target_counts`, it also takes O(k) space.
        - As `k` is a constant value independent of the input string lengths,
          the space complexity can be considered O(1).
        """
        # Handle edge cases where `t` or `s` are empty.
        # If t is empty, any window (including empty) satisfies the condition, but problem implies t has chars.
        # Returning "" for empty t is a common convention or problem specific.
        if not t:
            return ""
        if not s:
            return ""

        # `target_counts`: Frequency map for characters in `t`.
        # Example: t = "ABC" -> {'A': 1, 'B': 1, 'C': 1}
        target_counts: Dict[str, int] = collections.Counter(t)

        # `required_chars`: The number of unique characters from `t` that we need to
        # match in terms of their required frequency.
        required_chars: int = len(target_counts)

        # `formed_chars`: Tracks how many unique characters from `t` have been
        # found in the current window with at least their `target_counts` frequency.
        formed_chars: int = 0

        # `window_counts`: Frequency map for characters within the current sliding window `s[left...right]`.
        window_counts: DefaultDict[str, int] = collections.defaultdict(int)

        # `left`: The left pointer of the sliding window.
        left: int = 0
        # `min_len`: Stores the length of the shortest valid window found so far.
        # Initialized to infinity.
        min_len: float = float('inf')
        # `min_window_start`: Stores the starting index of the shortest valid window.
        min_window_start: int = 0

        # Iterate with the `right` pointer to expand the window.
        for right in range(len(s)):
            char_r: str = s[right]
            window_counts[char_r] += 1  # Add current character to window_counts

            # Check if this character is part of `t` and its count in the window
            # has just reached the required frequency.
            if char_r in target_counts and window_counts[char_r] == target_counts[char_r]:
                formed_chars += 1

            # While the current window is valid (i.e., `formed_chars` matches `required_chars`),
            # try to shrink it from the `left`.
            while formed_chars == required_chars and left <= right:
                current_window_len: int = right - left + 1

                # If this window is shorter than `min_len`, update `min_len` and `min_window_start`.
                if current_window_len < min_len:
                    min_len = current_window_len
                    min_window_start = left

                char_l: str = s[left]
                window_counts[char_l] -= 1  # Remove character from window_counts

                # If the character removed from the left was a required character
                # and its count now falls below the target count, decrement `formed_chars`.
                if char_l in target_counts and window_counts[char_l] < target_counts[char_l]:
                    formed_chars -= 1

                left += 1  # Move `left` pointer to shrink the window

        # If `min_len` remains infinity, no valid window was found.
        if min_len == float('inf'):
            return ""
        else:
            # Return the substring corresponding to the minimum valid window.
            return s[min_window_start : min_window_start + min_len]

class TestMinWindow(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        s = "ADOBECODEBANC"
        t = "ABC"
        self.assertEqual(self.sol.minWindow(s, t), "BANC")

    def test_example_2(self):
        s = "a"
        t = "a"
        self.assertEqual(self.sol.minWindow(s, t), "a")

    def test_example_3(self):
        s = "a"
        t = "aa"
        self.assertEqual(self.sol.minWindow(s, t), "")

    def test_example_4(self):
        s = "ADOBECODEBANC"
        t = "AABC"
        self.assertEqual(self.sol.minWindow(s, t), "ADOBECODEBA")

    def test_example_5(self):
        s = "ab"
        t = "b"
        self.assertEqual(self.sol.minWindow(s, t), "b")

    # Edge Cases
    def test_t_is_empty(self):
        self.assertEqual(self.sol.minWindow("any_string", ""), "")

    def test_s_is_empty(self):
        self.assertEqual(self.sol.minWindow("", "abc"), "")
        self.assertEqual(self.sol.minWindow("", ""), "")

    def test_no_valid_window(self):
        self.assertEqual(self.sol.minWindow("abc", "xyz"), "")
        self.assertEqual(self.sol.minWindow("ab", "c"), "")

    def test_t_longer_than_s(self):
        self.assertEqual(self.sol.minWindow("a", "abc"), "")

    def test_s_has_only_one_char(self):
        self.assertEqual(self.sol.minWindow("x", "x"), "x")
        self.assertEqual(self.sol.minWindow("x", "y"), "")

    def test_t_has_only_one_char(self):
        self.assertEqual(self.sol.minWindow("banana", "a"), "a")
        self.assertEqual(self.sol.minWindow("hello", "l"), "ll") 

    def test_s_and_t_are_same(self):
        self.assertEqual(self.sol.minWindow("hello", "hello"), "hello")

    def test_all_chars_identical(self):
        self.assertEqual(self.sol.minWindow("aaaaa", "aa"), "aa")
        self.assertEqual(self.sol.minWindow("bbbbbb", "bbb"), "bbb")

    def test_window_at_start(self):
        self.assertEqual(self.sol.minWindow("abracadabra", "abc"), "abr")

    def test_window_at_end(self):
        self.assertEqual(self.sol.minWindow("hello", "ol"), "llo")
        self.assertEqual(self.sol.minWindow("xyzabc", "abc"), "abc")
