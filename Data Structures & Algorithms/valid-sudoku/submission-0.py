class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            rowSet = set()
            for rowElem in row:
                if rowElem in rowSet:
                    return False
                elif rowElem != ".":
                    rowSet.add(rowElem)
        cols = []
        for i in range(len(board)):
            colSet = set()
            for j in range(len(board)):
                colElem = board[j][i]
                if colElem in colSet:
                    return False
                elif colElem != '.':
                    colSet.add(colElem)

        # loop through rows
        # map each row to the current column value
        # add current column value to colSet

        # 0,0 0,1 0,2 0,3          0,6
        # 1,0 1,1 1,2
        # 2,0 2,1 2,2          2,5           2,8
        # 3,0 0,1 0,2 3,3          3,6
        # 4,0 1,1 1,2
        # 5,0 2,1 2,2          5,5           5,8
        # 6,0 0,1 0,2 6,3          6,6
        # 7,0 1,1 1,2
        # 8,0 2,1 2,2          8,5           8,8
            
        for n in list(range(3)):
            for i in list(range(3)):
                boxSet = set()
                for j in list(range(3)):
                    for k in list(range(3)):
                        boxElem = board[n*3+j][i*3+k]
                        if boxElem in boxSet:
                            return False
                        elif boxElem != '.':
                            boxSet.add(boxElem)
        
        return True
        