class Solution:
    def findPattern(self, board, pattern):
        height = len(board)
        width = len(board[0])
        p_height = len(pattern)
        p_width = len(pattern[0])

        def matches(row, col):
            mapCharToDigit = {}
            mapDigitToChar = {}

            for idxRow in range(p_height):
                for idxCol in range(p_width):
                    patChar = pattern[idxRow][idxCol]
                    brdVal = board[row + idxRow][col + idxCol]

                    if '0' <= patChar <= '9':
                        if int(patChar) != brdVal:
                            return False
                    else:
                        if patChar in mapCharToDigit:
                            if mapCharToDigit[patChar] != brdVal:
                                return False
                        else:
                            if brdVal in mapDigitToChar:
                                return False
                            mapCharToDigit[patChar] = brdVal
                            mapDigitToChar[brdVal] = patChar
            return True

        for rIndex in range(height - p_height + 1):
            for cIndex in range(width - p_width + 1):
                if matches(rIndex, cIndex):
                    return [rIndex, cIndex]

        return [-1, -1]