class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len, t_len = len(s),  len(t)
        if s_len != t_len:
            return False
        dict_s, dict_t = {}, {}
        for i in range(s_len):
            dict_s[s[i]] = dict_s.get(s[i], 0) + 1
            dict_t[t[i]] = dict_t.get(t[i], 0) + 1

        for s_key, s_value in dict_s.items():
            t_value = dict_t.get(s_key, 0)
            if s_value != t_value:
                return False

        return True
        
