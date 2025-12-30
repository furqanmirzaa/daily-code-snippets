import collections
import unittest

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

        target_counts = collections.Counter(t)
        required_chars = len(target_counts)
        formed_chars = 0
        window_counts = collections.defaultdict(int)

        left = 0
        min_len = float('inf')
        min_window_start = 0

        for right in range(len(s)):
            char_r = s[right]
            window_counts[char_r] += 1

            if char_r in target_counts and window_counts[char_r] == target_counts[char_r]:
                formed_chars += 1

            while formed_chars == required_chars and left <= right:
                current_window_len = right - left + 1
                if current_window_len < min_len:
                    min_len = current_window_len
                    min_window_start = left

                char_l = s[left]
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
