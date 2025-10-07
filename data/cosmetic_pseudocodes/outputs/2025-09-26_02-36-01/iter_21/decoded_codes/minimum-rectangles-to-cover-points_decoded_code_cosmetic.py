class Solution:
    def minRectanglesToCoverPoints(self, points, w):
        vU = -1
        resCount = 0

        self.quickSortByX(points, 0, len(points) - 1)

        def recurseIndex(idx):
            nonlocal vU, resCount
            if idx >= len(points):
                return
            vX = points[idx][0]
            if vX > vU:
                vU = vX + w
                resCount += 1
            recurseIndex(idx + 1)

        recurseIndex(0)
        return resCount

    def quickSortByX(self, arr, start, end):
        if start >= end:
            return
        pivotVal = arr[end][0]
        pIndex = start
        for i in range(start, end):
            if arr[i][0] <= pivotVal:
                self.swap(arr, i, pIndex)
                pIndex += 1
        self.swap(arr, pIndex, end)
        self.quickSortByX(arr, start, pIndex - 1)
        self.quickSortByX(arr, pIndex + 1, end)

    def swap(self, arr, idx1, idx2):
        arr[idx1], arr[idx2] = arr[idx2], arr[idx1]