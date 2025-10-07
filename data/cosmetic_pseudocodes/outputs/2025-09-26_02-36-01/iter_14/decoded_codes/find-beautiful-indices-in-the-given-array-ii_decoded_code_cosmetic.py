from typing import List

class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        tempListX: List[int] = []
        tempListY: List[int] = []
        resultAcc: List[int] = []

        def locateOccurrencesX():
            limitX = len(s) - len(a)
            ctrX = 0
            while ctrX <= limitX:
                segmentX = ""
                posEndX = ctrX + len(a) - 1
                posY = ctrX
                while posY <= posEndX:
                    segmentX += s[posY]
                    posY += 1
                if segmentX == a:
                    tempListX.append(ctrX)
                ctrX += 1

        def locateOccurrencesY():
            limitY = len(s) - len(b)
            for ctrY in range(limitY + 1):
                segmentY = ""
                posEndY = ctrY + len(b) - 1
                idxY = ctrY
                while idxY <= posEndY:
                    segmentY += s[idxY]
                    idxY += 1
                if segmentY == b:
                    tempListY.append(ctrY)

        locateOccurrencesX()
        locateOccurrencesY()

        p = 0
        q = 0
        countP = len(tempListX)
        countQ = len(tempListY)

        while p < countP and q < countQ:
            distDiff = abs(tempListX[p] - tempListY[q])
            if distDiff <= k:
                resultAcc.append(tempListX[p])
                p += 1
            else:
                if tempListX[p] < tempListY[q]:
                    p += 1
                else:
                    q += 1

        return resultAcc