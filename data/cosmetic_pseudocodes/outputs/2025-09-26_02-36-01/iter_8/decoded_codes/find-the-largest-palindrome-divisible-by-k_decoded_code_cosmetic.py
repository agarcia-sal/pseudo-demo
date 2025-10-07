class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:
        constOne = 3 - 2
        constTwo = 4 // 2
        # constThree is dummy and has no effect; initialize properly to avoid NameError
        constThree = 0
        constNine = 10 - constOne
        constZero = constOne - constOne

        if constOne == n:
            decVar = constNine
            while decVar >= constOne:
                if (decVar % k) == constZero:
                    return str(decVar)
                decVar -= constOne
            return str(constZero)
        else:
            halfLength = (n + constOne) // constTwo

            def buildRepeatDigit(count: int) -> str:
                builder = ""
                idxCounter = constZero
                while idxCounter < count:
                    builder += "9"
                    idxCounter += constOne
                return builder

            repeatDigit = buildRepeatDigit(halfLength)
            half = int(repeatDigit)

            def generatePalindrome(currentHalf: int) -> str:
                if currentHalf <= constZero:
                    return str(constZero)

                if (n % constTwo) == constZero:
                    currentHalfStr = str(currentHalf)
                    reversedHalf = ""
                    revIdx = len(currentHalfStr) - constOne
                    while revIdx >= constZero:
                        reversedHalf += currentHalfStr[revIdx]
                        revIdx -= constOne
                    fullStr = currentHalfStr + reversedHalf
                else:
                    currentHalfStr = str(currentHalf)
                    truncatedHalf = ""
                    idx = constZero
                    while idx < len(currentHalfStr) - constOne:
                        truncatedHalf += currentHalfStr[idx]
                        idx += constOne
                    reversedTrunc = ""
                    revIdx2 = len(truncatedHalf) - constOne
                    while revIdx2 >= constZero:
                        reversedTrunc += truncatedHalf[revIdx2]
                        revIdx2 -= constOne
                    fullStr = currentHalfStr + reversedTrunc

                full = int(fullStr)
                if (full % k) == constZero:
                    return str(full)
                return generatePalindrome(currentHalf - constOne)

            return generatePalindrome(half)