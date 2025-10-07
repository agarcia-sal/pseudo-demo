from bisect import bisect_left

class Solution:
    def maxPathLength(self, coordinates, k):
        pivotX = coordinates[k][0]
        pivotY = coordinates[k][1]

        leftCoords = []
        idx = 0
        while idx < len(coordinates):
            currentX = coordinates[idx][0]
            currentY = coordinates[idx][1]
            if not (currentX >= pivotX or currentY >= pivotY):
                leftCoords.append((currentX, currentY))
            idx += 1

        rightCoords = []
        idx = 0
        while idx < len(coordinates):
            currX = coordinates[idx][0]
            currY = coordinates[idx][1]
            if not (currX <= pivotX or currY <= pivotY):
                rightCoords.append((currX, currY))
            idx += 1

        return 1 + self._lengthOfLIS(leftCoords) + self._lengthOfLIS(rightCoords)

    def _lengthOfLIS(self, coordinates):
        # Sort by first element ascending, then second element descending
        coordinates.sort(key=lambda x: (x[0], -x[1]))

        tails = []
        iterIdx = 0
        while iterIdx < len(coordinates):
            currentY = coordinates[iterIdx][1]
            if len(tails) == 0 or currentY > tails[-1]:
                tails.append(currentY)
            else:
                insertionIndex = bisect_left(tails, currentY)
                tails[insertionIndex] = currentY
            iterIdx += 1

        return len(tails)