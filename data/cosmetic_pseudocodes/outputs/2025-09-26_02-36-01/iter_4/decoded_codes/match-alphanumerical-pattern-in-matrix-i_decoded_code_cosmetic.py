class Solution:
    def findPattern(self, board, pattern):
        totalRows = len(board)
        totalCols = len(board[0]) if board else 0
        patternRows = len(pattern)
        patternCols = len(pattern[0]) if pattern else 0

        def matches(rowIdx, colIdx):
            charToDigitMap = {}
            digitToCharMap = {}

            for rowCounter in range(patternRows):
                for colCounter in range(patternCols):
                    patternChar = pattern[rowCounter][colCounter]
                    boardDigit = board[rowIdx + rowCounter][colIdx + colCounter]

                    if patternChar.isdigit():
                        if int(patternChar) != boardDigit:
                            return False
                    else:
                        if patternChar in charToDigitMap:
                            if charToDigitMap[patternChar] != boardDigit:
                                return False
                        else:
                            if boardDigit in digitToCharMap:
                                return False
                            charToDigitMap[patternChar] = boardDigit
                            digitToCharMap[boardDigit] = patternChar
            return True

        for r in range(totalRows - patternRows + 1):
            for c in range(totalCols - patternCols + 1):
                if matches(r, c):
                    return [r, c]

        return [-1, -1]