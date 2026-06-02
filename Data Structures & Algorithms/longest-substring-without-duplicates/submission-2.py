class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        # abcabcbb
        left = 0
        s_len = len(s)
        max_len = 1

        seen_queue = deque()

        for index, ch in enumerate(s):
            if ch in seen_queue:
                while True:
                    popped_char = seen_queue.popleft()
                    left += 1
                    if popped_char == ch:
                        break
                
            
            seen_queue.append(ch)

            max_len = max(max_len, index - left + 1)

        return max_len



        