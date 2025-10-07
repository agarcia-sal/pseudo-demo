class Solution:
    def numberOfPairs(self, points):
        totalPairs = 0
        lengthPoints = len(points)

        def innerLoopJ(indexI, indexJ, isValid):
            nonlocal totalPairs
            if indexJ > lengthPoints - 2:
                return isValid
            else:
                if indexI != indexJ:
                    pointIX, pointIY = points[indexI]
                    pointJX, pointJY = points[indexJ]

                    if (pointIX <= pointJX) and (pointIY >= pointJY):
                        def checkKLoop(kIndex, stillValid):
                            if kIndex > lengthPoints - 2 or stillValid == 0:
                                return stillValid
                            else:
                                if kIndex != indexI and kIndex != indexJ:
                                    pointKX, pointKY = points[kIndex]
                                    if (pointIX <= pointKX <= pointJX) and (pointIY >= pointKY >= pointJY):
                                        stillValid = 0
                                        return stillValid
                                    else:
                                        return checkKLoop(kIndex + 1, stillValid)
                                else:
                                    return checkKLoop(kIndex + 1, stillValid)

                        validFlag = 1
                        validFlag = checkKLoop(0, validFlag)

                        if validFlag == 1:
                            totalPairs += 1
                return innerLoopJ(indexI, indexJ + 1, isValid)

        def outerLoopI(indexI):
            if indexI > lengthPoints - 2:
                return
            else:
                innerLoopJ(indexI, 0, 1)
                outerLoopI(indexI + 1)

        outerLoopI(0)
        return totalPairs