class Solution:
    def numberOfPairs(self, inputList):
        def isBetween(a, lower, upper):
            return lower <= a <= upper

        def pointCheck(px, py, qx, qy, rx, ry):
            return isBetween(rx, px, qx) and isBetween(ry, qy, py)

        resultCount = 0
        size = len(inputList)

        def iterateI(indexI):
            nonlocal resultCount
            if indexI >= size:
                return

            def iterateJ(indexJ):
                nonlocal resultCount
                if indexJ >= size:
                    return

                if indexI != indexJ:
                    xI, yI = inputList[indexI]
                    xJ, yJ = inputList[indexJ]

                    if xI <= xJ and yI >= yJ:
                        isValid = True

                        def iterateK(indexK):
                            nonlocal isValid
                            if indexK >= size or not isValid:
                                return

                            if indexK != indexI and indexK != indexJ:
                                xK, yK = inputList[indexK]
                                if xI <= xK <= xJ and yI >= yK >= yJ:
                                    isValid = False
                                    return
                            iterateK(indexK + 1)

                        iterateK(0)

                        if isValid:
                            resultCount += 1

                iterateJ(indexJ + 1)

            iterateJ(0)
            iterateI(indexI + 1)

        iterateI(0)
        return resultCount