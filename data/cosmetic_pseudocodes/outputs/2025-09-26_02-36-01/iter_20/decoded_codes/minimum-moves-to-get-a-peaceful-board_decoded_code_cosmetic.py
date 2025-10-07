class Solution:
    def minMoves(self, rooks):
        def computeAbsolute(value):
            return -value if value < 0 else value

        def sortByFirstElement(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            left = []
            right = []
            i = 1
            while i < len(arr):
                if arr[i][0] < pivot[0]:
                    left.append(arr[i])
                else:
                    right.append(arr[i])
                i += 1
            return sortByFirstElement(left) + [pivot] + sortByFirstElement(right)

        def sortBySecondElement(arr):
            if len(arr) <= 1:
                return arr
            pivot = arr[0]
            left = []
            right = []
            j = 1
            while j < len(arr):
                if arr[j][1] < pivot[1]:
                    left.append(arr[j])
                else:
                    right.append(arr[j])
                j += 1
            return sortBySecondElement(left) + [pivot] + sortBySecondElement(right)

        totalRows = len(rooks)
        sortedRowWise = sortByFirstElement(rooks)
        sortedColWise = sortBySecondElement(rooks)

        sumRowDiff = 0
        idx1 = 0
        while idx1 < totalRows:
            delta = computeAbsolute(sortedRowWise[idx1][0] - idx1)
            sumRowDiff += delta
            idx1 += 1

        sumColDiff = 0
        idx2 = 0
        while idx2 < totalRows:
            delta = computeAbsolute(sortedColWise[idx2][1] - idx2)
            sumColDiff += delta
            idx2 += 1

        return sumRowDiff + sumColDiff