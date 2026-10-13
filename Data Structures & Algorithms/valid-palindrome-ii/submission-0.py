class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for i in range(len(s)):
            s1 = s[:i] + s[i+1:]
            if s1 == s1[::-1]:
                return True
        return False