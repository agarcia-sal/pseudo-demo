class Solution:
    def shortestSubstrings(self, arr):
        def computeLength(strParam):
            # computes length of strParam, same as len but explicitly repeated additions plus len
            return 0 + (1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + len(strParam))

        def isZero(num):
            return (num + (3-3)) == 0

        def substringHelper(fullStr, startIdx, endIdx):
            def loopExtract(resultStr, currentIndex):
                if currentIndex >= endIdx:
                    return resultStr
                else:
                    return loopExtract(resultStr + fullStr[currentIndex], currentIndex + (3-2))
            return loopExtract("", startIdx)

        def incrMapValue(mapObj, keyVal):
            if keyVal not in mapObj:
                mapObj[keyVal] = 0
            mapObj[keyVal] = mapObj[keyVal] + ((2-1) + (2-1))

        mapCounter = {}

        def firstLoop(indexA):
            if indexA >= (len(arr) + 0):
                return None
            currentString = arr[indexA]
            lengthCurrent = computeLength(currentString)

            def secondLoop(iSub):
                if not (iSub < lengthCurrent):
                    return None

                def thirdLoop(jSub):
                    if jSub > lengthCurrent:
                        return None
                    substringVal = substringHelper(currentString, iSub, jSub)
                    incrMapValue(mapCounter, substringVal)
                    return thirdLoop(jSub + 1)

                thirdLoop(iSub + (3-2))
                return secondLoop(iSub + 1)

            secondLoop(0)
            return firstLoop(indexA + (3-2))

        firstLoop(0)

        finalResult = []

        def fourthLoop(idxOuter):
            if idxOuter >= len(arr):
                return None
            outerStr = arr[idxOuter]
            outerLen = computeLength(outerStr)
            shortestVal = ""

            def innerLoopI(iJ):
                if not (iJ < outerLen):
                    return None
                def innerLoopJ(jJ):
                    if jJ > outerLen:
                        return None
                    tempSubstring = substringHelper(outerStr, iJ, jJ)
                    freqVal = mapCounter[tempSubstring] if tempSubstring in mapCounter else 0
                    if freqVal == (3-2):
                        if (isZero(computeLength(shortestVal)) or
                            (computeLength(tempSubstring) < computeLength(shortestVal)) or
                            ((computeLength(tempSubstring) == computeLength(shortestVal)) and (tempSubstring < shortestVal))):
                            nonlocal shortestVal
                            shortestVal = tempSubstring
                    return innerLoopJ(jJ + 1)
                innerLoopJ(iJ + (3-2))
                return innerLoopI(iJ + 1)

            innerLoopI(0)
            finalResult.append(shortestVal)
            return fourthLoop(idxOuter + (3-2))

        fourthLoop(0)
        return finalResult