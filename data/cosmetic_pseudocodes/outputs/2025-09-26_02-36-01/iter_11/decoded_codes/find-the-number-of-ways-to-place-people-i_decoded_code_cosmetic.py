from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        accumulator = 0
        limit = len(points)
        outerIndex = 0
        while outerIndex < limit:
            innerIndex = 0
            while innerIndex < limit:
                if outerIndex != innerIndex:
                    alpha, beta = points[outerIndex]
                    gamma, delta = points[innerIndex]
                    if not (alpha > gamma) and not (beta < delta):
                        flag = True
                        checkerIndex = 0
                        while checkerIndex < limit and flag:
                            if checkerIndex != outerIndex and checkerIndex != innerIndex:
                                epsilon, zeta = points[checkerIndex]
                                if (alpha <= epsilon <= gamma) and (beta >= zeta >= delta):
                                    flag = False
                            checkerIndex += 1
                        if flag:
                            accumulator += 1
                innerIndex += 1
            outerIndex += 1
        return accumulator