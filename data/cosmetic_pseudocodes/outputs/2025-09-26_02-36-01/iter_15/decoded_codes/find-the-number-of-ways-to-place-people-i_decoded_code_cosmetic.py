from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        result = 0
        length = len(points)

        outerIdx = 0
        while outerIdx < length:
            innerIdx = 0
            while innerIdx < length:
                if outerIdx != innerIdx:
                    p0x, p0y = points[outerIdx]
                    p1x, p1y = points[innerIdx]

                    if p0x <= p1x and p0y >= p1y:
                        isValid = True
                        checker = 0

                        while checker < length and isValid:
                            if checker != outerIdx and checker != innerIdx:
                                px, py = points[checker]
                                if p0x <= px <= p1x and p0y >= py >= p1y:
                                    isValid = False
                                    break
                            checker += 1

                        if isValid:
                            result += 1
                innerIdx += 1
            outerIdx += 1

        return result