class Solution:
    def findPattern(self, board, pattern):
        rows_board, cols_board = len(board), len(board[0])
        rows_pat, cols_pat = len(pattern), len(pattern[0])

        def verifyMatch(x, y):
            mapA = {}
            mapB = {}
            for outer_index in range(rows_pat):
                for inner_index in range(cols_pat):
                    elementA = pattern[outer_index][inner_index]
                    elementB = board[x + outer_index][y + inner_index]

                    if '0' <= elementA <= '9':
                        if int(elementA) != elementB:
                            return False
                    else:
                        if elementA in mapA:
                            if mapA[elementA] != elementB:
                                return False
                        else:
                            if elementB in mapB:
                                return False
                            mapA[elementA] = elementB
                            mapB[elementB] = elementA
            return True

        limitR = rows_board - rows_pat
        limitC = cols_board - cols_pat

        for idxR in range(limitR + 1):
            for idxC in range(limitC + 1):
                if verifyMatch(idxR, idxC):
                    return [idxR, idxC]

        return [-1, -1]