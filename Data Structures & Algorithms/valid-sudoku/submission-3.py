class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=set()
        cols=set()
        box=set()

        for r in range(9):
            for c in range(9):
                value=board[r][c]
                box_id=(r//3,c//3)
                #conditions
                if value=='.':
                    continue
                if (value,r) in row:
                    return False
                if (value,c) in cols:
                    return False
                if (value,box_id) in box:
                    return False

                row.add((value,r))
                cols.add((value,c))
                box.add((value,box_id))

        return True