from typing import Dict


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        start: int = 0
        longest: int = 0
        t: Dict[str, int] = {}
        for index, string in enumerate(s):
            if string in t:
                if t[string] >= start:
                    start = t[string] + 1
            longest = max(longest, index - start + 1)
            t[string] = index

        return longest


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("") == 0)
    print(Solution().lengthOfLongestSubstring("acbabcbb") == 3)
    print(Solution().lengthOfLongestSubstring("bbbbb") == 1)
    print(Solution().lengthOfLongestSubstring("pwwkew") == 3)
    print(Solution().lengthOfLongestSubstring("aab") == 2)
    print(Solution().lengthOfLongestSubstring("abc") == 3)
    print(Solution().lengthOfLongestSubstring("tmmzuxtt") == 5)
