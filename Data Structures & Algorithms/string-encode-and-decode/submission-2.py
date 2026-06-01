class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result += "|" + str(len(s)) + "|" + s

        return result


    def decode(self, s: str) -> List[str]:
        len_s = len(s)
        if not s:
            return []

        start = 0
        done = False
        result = []
        while not done:
            # get the len of next word
            word_len = int(s[start+1: s.index("|", start + 1)])
            count_len = len(str(word_len))
            cur_start = start + count_len + 2
            word = s[cur_start : cur_start + word_len]
            result.append(word)
            start = cur_start + word_len
            if len_s <= start:
                done = True

        return result


