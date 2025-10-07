from bisect import bisect_left

class Solution:
    def maxPathLength(self, coordinates, k):
        pivotX, pivotY = coordinates[k]
        lesserCoords = []
        idx = 0
        while idx < len(coordinates):
            currentX, currentY = coordinates[idx]
            if currentX < pivotX and currentY < pivotY:
                lesserCoords.append((currentX, currentY))
            idx += 1

        greaterCoords = []
        pointer = 0
        while pointer < len(coordinates):
            curX, curY = coordinates[pointer]
            if curX > pivotX and curY > pivotY:
                greaterCoords.append((curX, curY))
            pointer += 1

        sumLength = 1
        sumLength += self._lengthOfLIS(lesserCoords)
        sumLength += self._lengthOfLIS(greaterCoords)
        return sumLength

    def _lengthOfLIS(self, coordinates):
        coordinates_sort = sorted(coordinates, key=lambda a: (a[0], -a[1]))
        tailArr = []
        i = 0
        while i < len(coordinates_sort):
            _, valY = coordinates_sort[i]
            if not tailArr or valY > tailArr[-1]:
                tailArr.append(valY)
            else:
                insertPos = bisect_left(tailArr, valY)
                tailArr[insertPos] = valY
            i += 1
        return len(tailArr)