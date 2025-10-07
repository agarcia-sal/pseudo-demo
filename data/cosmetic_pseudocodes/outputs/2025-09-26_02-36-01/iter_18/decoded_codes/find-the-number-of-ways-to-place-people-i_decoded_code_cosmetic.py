from typing import List

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        totalMatches = 0
        lengthPoints = len(points)
        outerIndex = 0
        while outerIndex < lengthPoints:
            innerIndex = 0
            while innerIndex < lengthPoints:
                if outerIndex != innerIndex:
                    valA, valB = points[outerIndex]
                    valC, valD = points[innerIndex]
                    if (valA > valC) or (valB < valD):
                        pass
                    else:
                        isValid = True
                        tempIndex = 0
                        while tempIndex < lengthPoints:
                            if tempIndex != outerIndex and tempIndex != innerIndex:
                                valE, valF = points[tempIndex]
                                if (valA <= valE <= valC) and (valD <= valF <= valB):
                                    isValid = False
                                    break
                            tempIndex += 1
                        if isValid:
                            totalMatches += 1
                innerIndex += 1
            outerIndex += 1
        return totalMatches