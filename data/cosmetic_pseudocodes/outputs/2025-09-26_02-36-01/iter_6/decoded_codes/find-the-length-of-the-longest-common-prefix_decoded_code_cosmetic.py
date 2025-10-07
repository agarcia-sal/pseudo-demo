class Solution:
    def longestCommonPrefix(self, arr1: list[int], arr2: list[int]) -> int:
        prefixesOne = set()

        def toString(value) -> str:
            return str(value)

        indexA = 0

        def fillPrefixesA():
            nonlocal indexA
            if indexA >= len(arr1):
                return
            elementStr = toString(arr1[indexA])
            lengthStr = len(elementStr)
            cursorB = lengthStr

            def addPrefixesB():
                nonlocal cursorB
                if cursorB < 1:
                    return
                preSubstr = elementStr[:cursorB]
                prefixesOne.add(preSubstr)
                cursorB -= 1
                addPrefixesB()

            addPrefixesB()
            indexA += 1
            fillPrefixesA()

        fillPrefixesA()

        prefixesTwo = set()
        positionC = 0

        def processArrayTwo():
            nonlocal positionC
            if positionC >= len(arr2):
                return
            stringVal = toString(arr2[positionC])
            lengthVal = len(stringVal)
            posD = 1
            while posD <= lengthVal:
                subStringD = stringVal[:posD]
                prefixesTwo.add(subStringD)
                posD += 1
            positionC += 1
            processArrayTwo()

        processArrayTwo()

        maxCommonLen = 0
        iterE = list(prefixesOne)
        idxE = 0
        while idxE < len(iterE):
            currentX = iterE[idxE]
            if currentX in prefixesTwo:
                lenX = len(currentX)
                if lenX > maxCommonLen:
                    maxCommonLen = lenX
            idxE += 1

        return maxCommonLen