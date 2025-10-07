class Solution:
    def numberOfPairs(self, points):
        def loopK(xiVal, yiVal, xjVal, yjVal, nLen, si, sj, validFlag):
            # Using a list for validFlag to allow mutation within nested scope
            if si >= nLen:
                validFlag[0] = True
                return
            if si == sj:
                loopK(xiVal, yiVal, xjVal, yjVal, nLen, si + 1, sj, validFlag)
                return
            tempx, tempy = points[si]
            if (xiVal <= tempx <= xjVal) and (yjVal <= tempy <= yiVal):
                validFlag[0] = False
                return
            loopK(xiVal, yiVal, xjVal, yjVal, nLen, si + 1, sj, validFlag)

        acc = 0
        lengthPoints = len(points)
        outerIdx = 0
        while outerIdx < lengthPoints:
            innerIdx = 0
            while innerIdx < lengthPoints:
                if outerIdx != innerIdx:
                    px, py = points[outerIdx]
                    qx, qy = points[innerIdx]
                    if px <= qx and py >= qy:
                        isValid = [False]
                        loopK(px, py, qx, qy, lengthPoints, 0, innerIdx, isValid)
                        if isValid[0]:
                            acc += 1
                innerIdx += 1
            outerIdx += 1
        return acc