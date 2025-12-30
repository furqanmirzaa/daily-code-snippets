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
        Finds the minimum window substring of `s` that contains all characters of `t`
        using the optimized sliding window approach.

        This algorithm employs a two-pointer (left and right) sliding window.
        It systematically expands the window using the `right` pointer and then,
        when a valid window is found (containing all characters from `t` with required frequencies),
        it attempts to contract the window from the `left` to find the smallest valid one.
        Frequency maps (`target_counts` and `window_counts`) are used to efficiently
        track character occurrences and validate window contents.

        Args:
            s: The main string to search within.
            t: The target string defining the characters and their required frequencies
               that must be present in the window.

        Returns:
            The smallest substring of `s` that contains all characters of `t`.
            Returns an empty string ("") if no such window is found.

        Time Complexity: O(|s| + |t|)
        - Initializing `target_counts` takes O(|t|) time.
        - The two pointers `left` and `right` traverse `s` at most once. Each character
          in `s` is processed by the `right` pointer once (added to window) and by
          the `left` pointer once (removed from window).
        - Dictionary operations (access, insert, delete) take O(1) on average.
        - Therefore, the overall time complexity is linear with respect to the
          lengths of `s` and `t`.

        Space Complexity: O(k) where `k` is the number of unique characters in `t`.
        - `target_counts`: Stores frequency of characters in `t`. At most `k`
          unique characters (where `k` is bounded by the size of the character set, e.g., 52 for English alphabet or 128 for ASCII).
        - `window_counts`: Stores frequency of characters in the current window.
          Similar to `target_counts`, `O(k)`.
        - The space complexity is `O(k)`, which can be considered `O(1)` as `k` is constant with respect to input size `m` and `n`.
        """
        if not t:
            return ""
        if not s:
            return ""

        # `target_counts` stores the required frequency of each character in `t`.
        target_counts: Dict[str, int] = collections.Counter(t)

        # `required_chars` is the count of unique characters from `t` that
        # we still need to match in the current window's frequency.
        required_chars: int = len(target_counts)

        # `formed_chars` tracks how many unique characters from `t` are
        # present in the current window with at least their required frequency.
        formed_chars: int = 0

        # `window_counts` stores the frequency of characters in the current sliding window.
        window_counts: DefaultDict[str, int] = collections.defaultdict(int)

        # `left` pointer for the start of the current window.
        left: int = 0
        # `min_len` stores the length of the smallest valid window found so far.
        min_len: float = float('inf')
        # `min_window_start` stores the starting index of the smallest valid window.
        min_window_start: int = 0

        # Iterate with the `right` pointer to expand the window.
        for right in range(len(s)):
            char_r: str = s[right]
            window_counts[char_r] += 1

            # If the character added to the window is one of `t`'s characters
            # and its count in the window now matches the required count in `t`,
            # increment `formed_chars`.
            if char_r in target_counts and window_counts[char_r] == target_counts[char_r]:
                formed_chars += 1

            # While all required characters are present (i.e., `formed_chars` equals `required_chars`),
            # try to shrink the window from the `left`.
            while formed_chars == required_chars and left <= right:
                current_window_len: int = right - left + 1

                # If the current window is smaller than the minimum found so far, update.
                if current_window_len < min_len:
                    min_len = current_window_len
                    min_window_start = left

                char_l: str = s[left]
                window_counts[char_l] -= 1

                # If the character removed from the left was a required character
                # and its count now falls below the target count, decrement `formed_chars`.
                if char_l in target_counts and window_counts[char_l] < target_counts[char_l]:
                    formed_chars -= 1

                left += 1  # Shrink window by moving `left` pointer

        # If `min_len` is still infinity, no valid window was found.
        if min_len == float('inf'):
            return ""
        else:
            # Return the minimum window substring.
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
