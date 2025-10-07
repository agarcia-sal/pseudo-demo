class Solution:
    def findPattern(self, board, pattern):
        def isEquivalent(xPos, yPos):
            mapCharToNum = {}
            mapNumToChar = {}

            def isDigitChar(ch):
                return '0' <= ch <= '9'

            for idxRow in range(len(pattern)):
                for idxCol in range(len(pattern[0])):
                    patChar = pattern[idxRow][idxCol]
                    brdNum = board[xPos + idxRow][yPos + idxCol]
                    if isDigitChar(patChar):
                        digVal = int(patChar)
                        if digVal != brdNum:
                            return False
                    else:
                        if patChar in mapCharToNum:
                            if mapCharToNum[patChar] != brdNum:
                                return False
                        else:
                            if brdNum in mapNumToChar:
                                return False
                            mapCharToNum[patChar] = brdNum
                            mapNumToChar[brdNum] = patChar
            return True

        maxRowIter = len(board) - len(pattern)
        maxColIter = len(board[0]) - len(pattern[0])

        outerIter = 0
        while outerIter <= maxRowIter:
            innerIter = 0
            while innerIter <= maxColIter:
                if isEquivalent(outerIter, innerIter):
                    return [outerIter, innerIter]
                innerIter += 1
            outerIter += 1

        return [-1, -1]