class Solution:
    def __is_alpha_numeric(self, ch):
        return (ord("A") <= ord(ch) <= ord("Z") or 
            ord("a") <= ord(ch) <= ord("z") or
            ord("0") <= ord(ch) <= ord("9"))

    def isPalindrome(self, s: str) -> bool:
        lower_s = s.lower()
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.__is_alpha_numeric(lower_s[l]):
                l += 1
            while r > l and not self.__is_alpha_numeric(lower_s[r]):
                r -= 1

            if lower_s[l] != lower_s[r]:
                return False

            l, r = l+1, r-1

        

        return True

        
        