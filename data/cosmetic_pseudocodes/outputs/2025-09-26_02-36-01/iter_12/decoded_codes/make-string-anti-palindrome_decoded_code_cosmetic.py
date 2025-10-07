class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        def innerSwap(arr, x, y):
            arr[x], arr[y] = arr[y], arr[x]

        def isEqual(a, b):
            return a == b

        def strJoin(charList):
            acc = ""
            INDEX = 0
            while INDEX < len(charList):
                acc += charList[INDEX]
                INDEX += 1
            return acc

        def lessThan(a, b):
            return a < b

        def notEqual(a, b):
            return a != b

        def lengthOf(array):
            count = 0
            for _ in array:
                count += 1
            return count

        def floorDivide(a, b):
            tempQ = a / b
            return int(tempQ - (tempQ % 1))

        def getElement(arr, idx):
            return arr[idx]

        def setElement(arr, idx, val):
            arr[idx] = val

        def lessOrEqual(a, b):
            return a <= b

        def greaterOrEqual(a, b):
            return a >= b

        def createSortedList(text):
            charsList = []
            for index in range(len(text)):
                charsList.append(text[index])
            gap = lengthOf(charsList)
            swappedFlag = True
            while gap > 1 or swappedFlag:
                if gap > 1:
                    gap = max(1, floorDivide(gap, 1.247))
                swappedFlag = False
                i = 0
                while lessThan(i + gap, lengthOf(charsList)):
                    if charsList[i] > charsList[i + gap]:
                        tempVal = charsList[i]
                        charsList[i] = charsList[i + gap]
                        charsList[i + gap] = tempVal
                        swappedFlag = True
                    i += 1
            return charsList

        characters = createSortedList(s)
        lengthN = lengthOf(characters)
        halfM = floorDivide(lengthN, 2)

        def conditionCheck(arr, idx1, idx2):
            return isEqual(getElement(arr, idx1), getElement(arr, idx2))

        if lengthN % 2 == 1:
            # For odd length strings, it's impossible to form an anti-palindrome
            return "-1"

        if conditionCheck(characters, halfM, halfM - 1):
            alpha = halfM

            def loopForwardLimit(arr, startIndex, maxIndex):
                currentIndex = startIndex
                while lessThan(currentIndex, maxIndex) and conditionCheck(arr, currentIndex, currentIndex - 1):
                    currentIndex += 1
                return currentIndex

            beta = loopForwardLimit(characters, alpha, lengthN)
            gamma = halfM

            def loopSwapCondition(arr, idxStart, idxEnd, lengthTotal):
                i = idxStart
                j = idxEnd
                while lessThan(j, lengthTotal) and conditionCheck(arr, j, lengthTotal - j - 1):
                    if greaterOrEqual(i, lengthTotal):
                        return False
                    innerSwap(arr, i, j)
                    i += 1
                    j += 1
                return True

            ifSwapResult = loopSwapCondition(characters, beta, gamma, lengthN)
            if not ifSwapResult:
                return "-1"

        def searchAndSwap(arr, posI, half, totalLength):
            swappedFlagInternal = False
            kIdx = half
            foundSwap = False

            def mismatchCheck(val1, val2, val3, val4):
                return notEqual(val1, val2) and notEqual(val1, val4)

            while lessThan(kIdx, totalLength) and not foundSwap:
                cond1 = mismatchCheck(
                    getElement(arr, kIdx),
                    getElement(arr, posI),
                    getElement(arr, posI),
                    getElement(arr, totalLength - posI - 1),
                )
                if cond1:
                    innerSwap(arr, kIdx, posI)
                    swappedFlagInternal = True
                    foundSwap = True
                kIdx += 1
            return swappedFlagInternal

        for indexI in range(halfM):
            if conditionCheck(characters, indexI, lengthN - indexI - 1):
                swapSuccess = searchAndSwap(characters, indexI, halfM, lengthN)
                if not swapSuccess:
                    return "-1"

        return strJoin(characters)