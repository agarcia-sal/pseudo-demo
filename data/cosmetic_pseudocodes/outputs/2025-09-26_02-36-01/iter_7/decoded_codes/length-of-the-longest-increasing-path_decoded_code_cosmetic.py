from bisect import bisect_left

class Solution:
    def maxPathLength(self, coordinates, k):
        pivotX = coordinates[k][0]
        pivotY = coordinates[k][1]

        lesserPoints = []
        idx = 0
        while idx < len(coordinates):
            px, py = coordinates[idx]
            if not (px >= pivotX or py >= pivotY):
                lesserPoints.append((px, py))
            idx += 1

        greaterPoints = []
        j = 0
        while j < len(coordinates):
            cx, cy = coordinates[j]
            if cx > pivotX and cy > pivotY:
                greaterPoints.append((cx, cy))
            j += 1

        return 1 + self._lengthOfLIS(lesserPoints) + self._lengthOfLIS(greaterPoints)

    def _lengthOfLIS(self, coordinates):
        def compareFirstAscSecondDesc(a, b):
            if a[0] > b[0]:
                return 1
            elif a[0] < b[0]:
                return -1
            else:
                if a[1] < b[1]:
                    return 1
                elif a[1] > b[1]:
                    return -1
                else:
                    return 0

        # Python sort key to mimic compare function:
        # Sort by first ascending, second descending
        coordsCopy = sorted(coordinates, key=lambda x: (x[0], -x[1]))

        tailsArray = []
        for _, currentY in coordsCopy:
            # Use bisect_left on tailsArray for currentY
            # tailsArray is strictly increasing sequence of y's
            pos = bisect_left(tailsArray, currentY)
            if pos == len(tailsArray):
                tailsArray.append(currentY)
            else:
                tailsArray[pos] = currentY

        return len(tailsArray)