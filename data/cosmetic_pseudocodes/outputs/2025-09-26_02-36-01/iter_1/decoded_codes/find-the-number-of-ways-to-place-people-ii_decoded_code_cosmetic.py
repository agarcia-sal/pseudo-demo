from typing import List

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Solution:
    def numberOfPairs(self, points: List[Point]) -> int:
        n = len(points)
        # Sort points ascending by x, descending by y
        points.sort(key=lambda p: (p.x, -p.y))
        pairCount = 0
        for firstIndex in range(n - 1):
            ptA = points[firstIndex]
            for secondIndex in range(firstIndex + 1, n):
                ptB = points[secondIndex]
                if ptA.x <= ptB.x and ptA.y >= ptB.y:
                    isPairValid = True
                    for midIndex in range(firstIndex + 1, secondIndex):
                        ptM = points[midIndex]
                        if ptA.x <= ptM.x <= ptB.x and ptB.y <= ptM.y <= ptA.y:
                            isPairValid = False
                            break
                    if isPairValid:
                        pairCount += 1
        return pairCount