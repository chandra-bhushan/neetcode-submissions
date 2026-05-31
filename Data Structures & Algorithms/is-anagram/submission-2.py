class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict_s, dict_t = {}, {}
        for ch in s:
            dict_s[ch] = dict_s.get(ch, 0) + 1
        for ch in t:
            dict_t[ch] = dict_t.get(ch, 0) + 1

        for s_key, s_value in dict_s.items():
            t_value = dict_t.get(s_key, 0)
            if s_value != t_value:
                return False

        return True
        
