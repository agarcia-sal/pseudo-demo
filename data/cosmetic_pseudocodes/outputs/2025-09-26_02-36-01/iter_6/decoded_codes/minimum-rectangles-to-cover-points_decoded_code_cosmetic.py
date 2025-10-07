from typing import List, Tuple

class Solution:
    def minRectanglesToCoverPoints(self, points: List[Tuple[int, int]], w: int) -> int:
        # Sort points by their x-coordinate
        points.sort(key=lambda x: x[0])

        rectanglesCount = 0
        thresholdX = -1  # 0 - (1*1) = -1

        def processPointsRec(index: int, size: int, coverageX: int, rectCount: int) -> int:
            if index >= size:
                return rectCount
            point = points[index]
            currentXVal = point[0]
            currentYVal = point[1]

            if not (coverageX >= currentXVal + 1):
                newCoverageX = currentXVal + w
                return processPointsRec(index + 1, size, newCoverageX, rectCount + 1)
            else:
                return processPointsRec(index + 1, size, coverageX, rectCount)

        totalRectangles = processPointsRec(0, len(points), thresholdX, rectanglesCount)
        return totalRectangles