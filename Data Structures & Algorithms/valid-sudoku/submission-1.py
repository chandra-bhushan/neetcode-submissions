class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # need to validate row, col and 3x3 box
        row_count = len(board)
        col_count = len(board[0])
        rows = [set() for x in range(row_count)] 
        cols = [set() for x in range(col_count)]
        boxes = [set() for x in range((row_count * col_count) // 9 )]
        DIGITS = "123456789"
        EMPTY = "."
        

        for i in range(row_count):
            for j in range(col_count):
                ch = board[i][j]
                if ch == EMPTY:
                    continue
                if ch not in DIGITS:
                    return False
                
                box_number = ((i // 3) * 3) + (j // 3)
                if (ch in rows[i]) or (ch in cols[j]) or (ch in boxes[box_number]):
                    return False
                
                rows[i].add(ch)
                cols[j].add(ch)
                boxes[box_number].add(ch)

        
        return True
                



        