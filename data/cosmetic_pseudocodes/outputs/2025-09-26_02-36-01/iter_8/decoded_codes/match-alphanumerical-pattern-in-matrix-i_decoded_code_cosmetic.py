class Solution:
    def findPattern(self, board, pattern):
        totalRows = len(board)
        totalCols = len(board[0])
        patternRows = len(pattern)
        patternCols = len(pattern[0])

        def matches(rowIndex, colIndex):
            mapCharToDigit = {}
            mapDigitToChar = {}

            outerCounter = 0
            while outerCounter <= patternRows - 1:
                innerCounter = 0
                while innerCounter <= patternCols - 1:
                    currentPatternChar = pattern[outerCounter][innerCounter]
                    currentBoardDigit = board[rowIndex + outerCounter][colIndex + innerCounter]

                    if '0' <= currentPatternChar <= '9':
                        digitValue = int(currentPatternChar)
                        if digitValue != currentBoardDigit:
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

                    innerCounter += 1
                outerCounter += 1

            return True

        rowIterator = 0
        while rowIterator <= totalRows - patternRows:
            colIterator = 0
            while colIterator <= totalCols - patternCols:
                if matches(rowIterator, colIterator):
                    return [rowIterator, colIterator]
                colIterator += 1
            rowIterator += 1

        return [-1, -1]