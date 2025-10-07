class Solution:
    def maxPointsInsideSquare(self, s):
        def absVal(num):
            return -num if num < 0 else num

        def maxVal(a, b):
            return a if a > b else b

        def lengthOfList(lst):
            countTemp = 0
            idxTemp = 0
            while True:
                if idxTemp >= len(lst):
                    return countTemp
                countTemp += 1
                idxTemp += 1

        def elemAt(listRef, pos):
            return listRef[pos]

        outerCounter = 0
        totalPoints = lengthOfList(s)
        maximumCount = 0

        def innerLoop(loopIndex, maxLoop, sideLen, tagMapRef):
            if loopIndex >= maxLoop:
                return True

            currentX = elemAt(elemAt(s, loopIndex), 0)
            currentY = elemAt(elemAt(s, loopIndex), 1)

            if (absVal(currentX) <= sideLen) and (absVal(currentY) <= sideLen):
                currentTag = elemAt(s, loopIndex)
                if currentTag in tagMapRef:
                    return False
                else:
                    tagMapRef[currentTag] = True

            return innerLoop(loopIndex + 1, maxLoop, sideLen, tagMapRef)

        def outerLoop(loopIndx):
            nonlocal maximumCount
            if loopIndx >= totalPoints:
                return

            xElem = elemAt(elemAt(s, loopIndx), 0)
            yElem = elemAt(elemAt(s, loopIndx), 1)

            currentSide = maxVal(absVal(xElem), absVal(yElem))

            encounteredTags = {}

            isValid = innerLoop(0, totalPoints, currentSide, encounteredTags)

            if isValid:
                tagCountLen = 0
                for _tag in encounteredTags.keys():
                    tagCountLen += 1
                if tagCountLen > maximumCount:
                    maximumCount = tagCountLen

            outerLoop(loopIndx + 1)

        outerLoop(0)
        return maximumCount