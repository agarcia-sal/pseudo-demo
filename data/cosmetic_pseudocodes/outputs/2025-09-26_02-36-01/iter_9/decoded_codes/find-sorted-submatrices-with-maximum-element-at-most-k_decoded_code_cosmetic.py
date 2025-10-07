class Solution:
    def countSubmatrices(self, matrix, limit):
        height = len(matrix)
        width = len(matrix[0])
        totalCount = 0

        def validateBound(submat):
            for line in submat:
                for val in line:
                    if val > limit:
                        return False
            return True

        def confirmDescending(submat):
            for currentLine in submat:
                for pos in range(1, len(currentLine)):
                    if currentLine[pos] > currentLine[pos - 1]:
                        return False
            return True

        def extractBlock(gridBlock, startR, endR, startC, endC):
            def takeSlice(seq, startIdx, endIdx):
                return seq[startIdx:endIdx + 1]

            segmentRows = takeSlice(gridBlock, startR, endR)
            slicedSub = [takeSlice(row, startC, endC) for row in segmentRows]
            return slicedSub

        rowStart = 0
        while rowStart < height:
            colStart = 0
            while colStart < width:
                rowEnd = rowStart
                while rowEnd < height:
                    colEnd = colStart
                    while colEnd < width:
                        piece = extractBlock(matrix, rowStart, rowEnd, colStart, colEnd)
                        if validateBound(piece) and confirmDescending(piece):
                            totalCount += 1
                        colEnd += 1
                    rowEnd += 1
                colStart += 1
            rowStart += 1

        return totalCount