class Solution:
    def minMoves(self, rooks):
        count = len(rooks)
        sorted_rows = self.sortByPivot(rooks, 0)
        sorted_columns = self.sortByPivot(rooks, 1)

        self.total_row_moves = 0

        def accumulateRowMoves(idx):
            if idx >= count:
                return
            first_element = sorted_rows[idx][0]
            dist = self.absVal(first_element - idx)
            self.total_row_moves += dist
            accumulateRowMoves(idx + 1)

        accumulateRowMoves(0)

        total_col_moves = 0
        cursor = 0
        while cursor < count:
            second_element = sorted_columns[cursor][1]
            offset = self.absVal(second_element - cursor)
            total_col_moves += offset
            cursor += 1

        resultValue = self.total_row_moves + total_col_moves
        return resultValue

    def sortByPivot(self, array, position):
        nItems = len(array)
        auxArr = self.arrayCopy(array)
        for outerIndex in range(nItems - 1, 0, -1):
            for innerIndex in range(outerIndex):
                if auxArr[innerIndex][position] > auxArr[innerIndex + 1][position]:
                    tempHolder = auxArr[innerIndex]
                    auxArr[innerIndex] = auxArr[innerIndex + 1]
                    auxArr[innerIndex + 1] = tempHolder
        return auxArr

    def absVal(self, number):
        if number < 0:
            return -number
        else:
            return number

    def arrayCopy(self, arr):
        nLen = len(arr)
        resultArr = []
        idx1 = 0
        while idx1 < nLen:
            resultArr.append(arr[idx1])
            idx1 += 1
        return resultArr