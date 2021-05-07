from longest_palindromic_substring import Solution, is_palindrome


def test_is_palindrome():
    assert is_palindrome("a") is True
    assert is_palindrome("aa") is True
    assert is_palindrome("ab") is False
    assert is_palindrome("abcb") is False
    assert is_palindrome("aba") is True


def test_longestPalindrome():
    s = Solution()
    assert s.longestPalindrome("a") == "a"
    assert s.longestPalindrome("ab") == "a"
    assert s.longestPalindrome("abba") == "abba"
    assert s.longestPalindrome("aaaa") == "aaaa"
    assert s.longestPalindrome("ababa") == "ababa"


def test_longestPalindromeV2():
    s = Solution()
    assert s.longestPalindromeV2("a") == "a"
    assert s.longestPalindromeV2("ab") == "a"
    assert s.longestPalindromeV2("aaa") == "aaa"
    assert s.longestPalindromeV2("abba") == "abba"
    assert s.longestPalindromeV2("aaaa") == "aaaa"
    assert s.longestPalindromeV2("ababa") == "ababa"
