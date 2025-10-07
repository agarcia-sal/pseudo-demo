from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        # Custom sort: by x ascending, y descending
        points.sort(key=lambda p: (p.x, -p.y))

        totalPairs = 0
        lengthPoints = len(points)

        for outerIndex in range(lengthPoints - 1):
            px1, py1 = points[outerIndex].x, points[outerIndex].y

            for innerIndex in range(outerIndex + 1, lengthPoints):
                px2, py2 = points[innerIndex].x, points[innerIndex].y

                if px1 <= px2 and py1 >= py2:
                    isValidPair = True
                    for midIndex in range(outerIndex + 1, innerIndex):
                        midX, midY = points[midIndex].x, points[midIndex].y

                        cond1 = (px1 <= midX <= px2)
                        cond2 = (py2 <= midY <= py1)

                        if cond1 and cond2:
                            isValidPair = False
                            break

                    if isValidPair:
                        totalPairs += 1

        return totalPairs