class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Solution:
    def numberOfPairs(self, points):
        def customSort(arr, low, high):
            if low < high:
                pivotIndex = low
                pivot = arr[pivotIndex]
                left = low + 1
                right = high
                while left <= right:
                    while left <= high and (arr[left].x < pivot.x or (arr[left].x == pivot.x and arr[left].y > pivot.y)):
                        left += 1
                    while right > low and (arr[right].x > pivot.x or (arr[right].x == pivot.x and arr[right].y < pivot.y)):
                        right -= 1
                    if left < right:
                        arr[left], arr[right] = arr[right], arr[left]
                        left += 1
                        right -= 1
                arr[low], arr[right] = arr[right], arr[low]
                customSort(arr, low, right - 1)
                customSort(arr, right + 1, high)

        def isValidPair(array, startIdx, endIdx, px, py, qx, qy):
            if not (px <= qx and py >= qy):
                return False

            def checkIntermediate(index):
                if index >= endIdx:
                    return True
                cx = array[index].x
                cy = array[index].y
                if (px <= cx <= qx) and (qy <= cy <= py):
                    return False
                return checkIntermediate(index + 1)

            return checkIntermediate(startIdx + 1)

        customSort(points, 0, len(points) - 1)

        totalPoints = len(points)
        pairCounter = 0
        outerIndex = 0

        while outerIndex <= totalPoints - 2:
            innerIndex = totalPoints - 1
            while innerIndex > outerIndex:
                pxVal = points[outerIndex].x
                pyVal = points[outerIndex].y
                qxVal = points[innerIndex].x
                qyVal = points[innerIndex].y

                if pxVal <= qxVal and pyVal >= qyVal:
                    if isValidPair(points, outerIndex, innerIndex, pxVal, pyVal, qxVal, qyVal):
                        pairCounter += 1
                innerIndex -= 1
            outerIndex += 1

        return pairCounter