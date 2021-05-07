import typing


def is_palindrome(s: str) -> bool:
    if len(s) <= 1:
        return True

    status: bool = True
    half = int(len(s) / 2)
    if len(s) % 2 == 0:
        left, right = half - 1, half
    else:
        left, right = half, half

    while left >= 0 and right < len(s):
        if s[left] != s[right]:
            status = False
            break
        left -= 1
        right += 1
    return status


class Solution:

    # 暴力破解
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        palindrome = s[0]
        for i in range(0, len(s) - 1):
            j = len(s) - 1
            while j >= 0:
                if s[i] != s[j]:
                    j -= 1
                else:
                    if is_palindrome(s[i:j + 1]):
                        if len(s[i:j + 1]) > len(palindrome):
                            palindrome = s[i:j + 1]
                        break
                    else:
                        j -= 1

        return palindrome

    # 动态规划
    def longestPalindromeV2(self, s: str) -> str:
        """
        dp[i][j] 保存字符串 s[i:j] 是否回文（i <= j）
        从长度为 1 的子串依次遍历，长度为 1 的子串肯定是回文的，其长度就是 1；
        然后是长度为 2 的子串依次遍历，只要 str[i] == str[j] ，它就是回文的，其长度为 2；
        接下来，长度大于 2 的子串，如果有 str[i] == str[j] ，且去掉两头的子串 dp[i + 1][j - 1]也是回文子串，那么该字符串就是回文字符串。
        """
        if len(s) <= 1:
            return s

        row = len(s)
        dp: typing.List[typing.List[int]] = [[None for i in range(row)] for i in range(row)]

        start = 0
        max_length = 1

        length = 1
        for i in range(0, row - length + 1):
            dp[i][i] = 1

        length = 2
        for i in range(0, row - length + 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                if length > max_length:
                    start = i
                    max_length = length

        length = 3
        while length <= row:
            for i in range(0, row - length + 1):
                if s[i] == s[i + length - 1] and dp[i + 1][i + length - 2] == 1:
                    dp[i][i + length - 1] = 1
                    if length > max_length:
                        start = i
                        max_length = length
            length += 1

        return s[start: start + max_length]


if __name__ == "__main__":
    print(Solution().longestPalindromeV2("abbac"))
