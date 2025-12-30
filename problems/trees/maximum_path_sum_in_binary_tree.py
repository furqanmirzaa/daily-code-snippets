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
        if not t:
            return ""
        if not s:
            return ""

        target_counts: Dict[str, int] = collections.Counter(t)
        required_chars: int = len(target_counts)
        formed_chars: int = 0
        window_counts: DefaultDict[str, int] = collections.defaultdict(int)

        left: int = 0
        min_len: float = float('inf')
        min_window_start: int = 0

        for right in range(len(s)):
            char_r: str = s[right]
            window_counts[char_r] += 1

            if char_r in target_counts and window_counts[char_r] == target_counts[char_r]:
                formed_chars += 1

            while formed_chars == required_chars and left <= right:
                current_window_len: int = right - left + 1

                if current_window_len < min_len:
                    min_len = current_window_len
                    min_window_start = left

                char_l: str = s[left]
                window_counts[char_l] -= 1

                if char_l in target_counts and window_counts[char_l] < target_counts[char_l]:
                    formed_chars -= 1

                left += 1

        if min_len == float('inf'):
            return ""
        else:
            return s[min_window_start : min_window_start + min_len]

class TestMinWindow(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    # --- Basic Examples from Problem / Common Cases ---
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

    # --- Edge Cases ---
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
        self.assertEqual(self.sol.minWindow("hello", "helloworld"), "")

    def test_s_has_only_one_char(self):
        self.assertEqual(self.sol.minWindow("x", "x"), "x")
        self.assertEqual(self.sol.minWindow("x", "y"), "")

    def test_t_has_only_one_char(self):
        self.assertEqual(self.sol.minWindow("banana", "a"), "a")
        self.assertEqual(self.sol.minWindow("hello", "l"), "l") 

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

    # --- More Comprehensive Tests ---
    def test_mixed_case(self):
        self.assertEqual(self.sol.minWindow("aBcdeFg", "BCF"), "BcdeF")
        self.assertEqual(self.sol.minWindow("aBcDeFgHij", "BCH"), "BcDeFgHi")

    def test_target_with_duplicates_sparse_s(self):
        self.assertEqual(self.sol.minWindow("abccba", "aa"), "abccba")
        self.assertEqual(self.sol.minWindow("figeha__ch_e", "aei"), "igeha")
        self.assertEqual(self.sol.minWindow("AYZABXAPPS", "AAB"), "AYZAB")

    def test_target_with_duplicates_compact_s(self):
        self.assertEqual(self.sol.minWindow("ADOBECODEBANC", "BCC"), "CODEBANC")
        self.assertEqual(self.sol.minWindow("ADOBECODEBANC", "AABC"), "ADOBECODEBA")

    def test_s_contains_t_exactly_once(self):
        self.assertEqual(self.sol.minWindow("abcdefg", "cde"), "cde")

    def test_t_is_single_char_repeated(self):
        self.assertEqual(self.sol.minWindow("banana", "nn"), "nan")

    def test_complex_long_string(self):
        s = "THISISATESTSTRINGWITHMANYCHARACTERSANDTHEDESIREDWINDOWISHERE"
        t = "TESTWINDOW"
        self.assertEqual(self.sol.minWindow(s, t), "TESTSTRINGWITHMANYCHARACTERSANDTHEDESIREDWINDOW")

    def test_no_match_at_all(self):
        self.assertEqual(self.sol.minWindow("abcdef", "xyz"), "")

    def test_all_s_is_window(self):
        self.assertEqual(self.sol.minWindow("hello", "hol"), "hello")
