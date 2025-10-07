class Solution:
    def findPattern(self, board, pattern):
        totalRows = len(board)
        totalCols = len(board[0]) if board else 0
        patternHeight = len(pattern)
        patternWidth = len(pattern[0]) if pattern else 0

        def matches(rowIndex, colIndex):
            mapCharToDigit = {}
            mapDigitToChar = {}

            def loopOuter(idx):
                if idx >= patternHeight:
                    return True
                else:
                    def loopInner(jdx):
                        if jdx >= patternWidth:
                            return loopOuter(idx + 1)
                        currentPatternChar = pattern[idx][jdx]
                        currentBoardDigit = board[rowIndex + idx][colIndex + jdx]

                        if '0' <= currentPatternChar <= '9':
                            numericValue = ord(currentPatternChar) - ord('0')
                            if numericValue != currentBoardDigit:
                                return False
                        else:
                            if currentPatternChar in mapCharToDigit:
                                if mapCharToDigit[currentPatternChar] != currentBoardDigit:
                                    return False
                            else:
                                if currentBoardDigit in mapDigitToChar:
                                    return False
                                mapCharToDigit[currentPatternChar] = currentBoardDigit
                                mapDigitToChar[currentBoardDigit] = currentPatternChar
                        return loopInner(jdx + 1)

                    return loopInner(0)

            return loopOuter(0)

        def searchRows(r):
            if r > totalRows - patternHeight:
                return [-1, -1]
            else:
                def searchCols(c):
                    if c > totalCols - patternWidth:
                        return searchRows(r + 1)
                    else:
                        if matches(r, c):
                            return [r, c]
                        else:
                            return searchCols(c + 1)
                return searchCols(0)

        return searchRows(0)