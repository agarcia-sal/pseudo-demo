class Solution:
    def numberOfPairs(self, points):
        counter = 0
        lengthVal = len(points)
        indexA = 0
        while indexA < lengthVal:
            indexB = 0
            while indexB < lengthVal:
                if indexA != indexB:
                    pointAX = points[indexA][0]
                    pointAY = points[indexA][1]
                    pointBX = points[indexB][0]
                    pointBY = points[indexB][1]
                    if (pointAX <= pointBX) and (pointAY >= pointBY):
                        isValid = False
                        indexC = 0
                        while indexC < lengthVal:
                            if indexC != indexA and indexC != indexB:
                                pointCX = points[indexC][0]
                                pointCY = points[indexC][1]
                                # If pointC is inside or on the rectangle defined by pointA and pointB
                                if not (pointAX > pointCX or pointCX > pointBX or pointAY < pointCY or pointCY < pointBY):
                                    isValid = True
                                    break
                            indexC += 1
                        if not isValid:
                            counter += 1
                indexB += 1
            indexA += 1
        return counter