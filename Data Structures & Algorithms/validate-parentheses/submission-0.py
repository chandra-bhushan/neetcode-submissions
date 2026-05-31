class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for ch in s:
            if ch in "({[":
                stack.append(ch)
            else:
                if not stack:
                    return False # no open present for found closing
                open = stack.pop()
                if  pairs[ch] != open:
                    return False

        return len(stack) == 0

        