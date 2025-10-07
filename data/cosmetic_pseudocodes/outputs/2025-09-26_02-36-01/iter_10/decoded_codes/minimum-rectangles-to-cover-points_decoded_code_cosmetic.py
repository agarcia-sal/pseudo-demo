class Solution:
    def minRectanglesToCoverPoints(self, points, w):
        def customSort(arr):
            # Bubble sort on points based on x-coordinate
            n = len(arr)
            while True:
                swapped = False
                for i in range(n - 1):
                    if arr[i][0] > arr[i + 1][0]:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]
                        swapped = True
                if not swapped:
                    break

        customSort(points)

        def processPointsRecursively(i, limit, lastMaxX, count):
            if i >= limit:
                return count
            xVal = points[i][0]
            if xVal > lastMaxX:
                newMaxX = xVal + w
                return processPointsRecursively(i + 1, limit, newMaxX, count + 1)
            else:
                return processPointsRecursively(i + 1, limit, lastMaxX, count)

        return processPointsRecursively(0, len(points), -1, 0)