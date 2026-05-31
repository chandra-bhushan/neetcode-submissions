class Solution:
    def isPalindrome(self, s: str) -> bool:

        alpha_s = "".join(ch.lower() for ch in s if ch.isalnum())
        return alpha_s[::1] == alpha_s[::-1]
        