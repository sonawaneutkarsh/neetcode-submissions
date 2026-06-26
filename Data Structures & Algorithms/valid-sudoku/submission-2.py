class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=set()
        cols=set()
        box=set()

        for r in range(9):
            for c in range(9):
                val=board[r][c]
            
                if val=='.':
                    continue
                
                box_id=(r//3,c//3)

                if (val,r) in rows:
                    return False
                
                if (val,c) in cols:
                    return False
                
                if (val,box_id) in box:
                    return False
                
                rows.add((val,r))
                cols.add((val,c))
                box.add((val,box_id))
        return True