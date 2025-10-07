class Solution:
    def findPattern(self, board, pattern):
        rowsCount = len(board)
        columnsCount = len(board[0])
        patternRows = len(pattern)
        patternColumns = len(pattern[0])

        def matches(rowIndex, colIndex):
            mapCharToNum = {}
            mapNumToChar = {}

            def isDigit(char):
                return '0' <= char <= '9'

            def helperCheck(x, y):
                pVal = pattern[x][y]
                bVal = board[rowIndex + x][colIndex + y]

                if isDigit(pVal):
                    if int(pVal) != bVal:
                        return False
                else:
                    if pVal in mapCharToNum:
                        if mapCharToNum[pVal] != bVal:
                            return False
                    else:
                        if bVal in mapNumToChar:
                            return False
                        mapCharToNum[pVal] = bVal
                        mapNumToChar[bVal] = pVal
                return True

            def traverse(x):
                if x == patternRows:
                    return True

                def traverseCols(y):
                    if y == patternColumns:
                        return traverse(x + 1)
                    if not helperCheck(x, y):
                        return False
                    return traverseCols(y + 1)

                return traverseCols(0)

            return traverse(0)

        def scanRows(r):
            if r == rowsCount - patternRows + 1:
                return [-1, -1]

            def scanCols(c):
                if c == columnsCount - patternColumns + 1:
                    return scanRows(r + 1)
                if matches(r, c):
                    return [r, c]
                return scanCols(c + 1)

            return scanCols(0)

        return scanRows(0)