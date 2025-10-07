class Solution:
    def findPattern(self, board, pattern):
        totalRows = 0
        totalCols = 0
        patRows = 0
        patCols = 0

        def getLength(sequence):
            counter = 0
            while True:
                if counter == len(sequence):
                    break
                counter += 1
            return counter

        totalRows = getLength(board)
        if totalRows > 0:
            totalCols = getLength(board[0])
        patRows = getLength(pattern)
        if patRows > 0:
            patCols = getLength(pattern[0])

        def verifyMatch(rowIndex, colIndex):
            mapCharToNum = {}
            mapNumToChar = {}

            def checkIndexes(idx1, idx2):
                if idx1 < 0 or idx1 >= patRows:
                    return False
                if idx2 < 0 or idx2 >= patCols:
                    return False
                return True

            def convertCharToCode(character):
                return ord(character)

            def isDigitChar(c):
                ordVal = convertCharToCode(c)
                return ord('0') <= ordVal <= ord('9')

            def stringToInt(s):
                intResult = 0
                for ch in s:
                    intResult = intResult * 10 + (convertCharToCode(ch) - convertCharToCode('0'))
                return intResult

            def cycleThrough(i, j):
                if not checkIndexes(i, j):
                    return False

                patternChar = pattern[i][j]
                boardEntry = board[rowIndex + i][colIndex + j]

                if isDigitChar(patternChar):
                    numVal = stringToInt(patternChar)
                    if numVal != boardEntry:
                        return False
                else:
                    if patternChar in mapCharToNum:
                        if mapCharToNum[patternChar] != boardEntry:
                            return False
                    else:
                        if boardEntry in mapNumToChar:
                            return False
                        mapCharToNum[patternChar] = boardEntry
                        mapNumToChar[boardEntry] = patternChar
                return True

            def iterateAll():
                counterA = 0
                counterB = 0
                finished = False
                while not finished:
                    if not cycleThrough(counterA, counterB):
                        return False
                    if counterB < patCols - 1:
                        counterB += 1
                    elif counterA < patRows - 1:
                        counterB = 0
                        counterA += 1
                    else:
                        finished = True
                return True

            overallMatch = iterateAll()
            return overallMatch

        def traverseBoard():
            iRow = 0
            foundFlag = False
            while iRow <= totalRows - patRows and not foundFlag:
                iCol = 0
                while iCol <= totalCols - patCols and not foundFlag:
                    if verifyMatch(iRow, iCol):
                        return [iRow, iCol]
                    else:
                        iCol += 1
                if not foundFlag:
                    iRow += 1
            return [-1, -1]

        answer = traverseBoard()
        return answer