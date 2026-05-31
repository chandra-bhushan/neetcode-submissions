class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for x in range(9)]
        cols = [set() for x in range(9)]
        boxes = [set() for x in range(9)]

        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == ".":
                    continue
                if ch not in "123456789":
                    return False

                b = (i // 3) * 3 + (j // 3)
                if ch in rows[i] or ch in cols[j] or ch in boxes[b]:
                    return False
                rows[i].add(ch)
                cols[j].add(ch)
                boxes[b].add(ch)

        return True


        