class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        def customHasKey(dictParam, keyParam):
            return keyParam in dictParam

        def customIncrement(dictParam, keyParam):
            if customHasKey(dictParam, keyParam):
                dictParam[keyParam] += 1
            else:
                dictParam[keyParam] = 1

        def customDecrement(dictParam, keyParam):
            if customHasKey(dictParam, keyParam):
                dictParam[keyParam] -= 1

        def isAnyCountGEThreshold(freqDict, threshold):
            for e in freqDict:
                if freqDict[e] >= threshold:
                    return True
            return False

        freqMap = {}
        resultTotal = 0
        startPos = 0

        def loopForward(indexIterator):
            nonlocal freqMap, resultTotal, startPos
            if not (indexIterator < len(s)):
                return

            currentChar = s[indexIterator]
            customIncrement(freqMap, currentChar)

            while isAnyCountGEThreshold(freqMap, k):
                charAtStart = s[startPos]
                customDecrement(freqMap, charAtStart)
                if freqMap.get(charAtStart, 0) == 0:
                    freqMap.pop(charAtStart, None)
                startPos += 1

            nonlocal_result = resultTotal + startPos
            # update resultTotal with nonlocal keyword
            # Python 3.8+ supports the nonlocal statement for nested functions.
            # But to keep clarity, declare nonlocal for resultTotal at the top.
            # Rewritten:
            # Will declare nonlocal resultTotal at start of loopForward

            # Instead do it properly:
            return_value = resultTotal + startPos
            # Since we can't assign nonlocal inside inner function without declaration,
            # declare nonlocal resultTotal here:

            # To fix this, move nonlocal declaration for resultTotal to top of the function:
            pass

        # So let's fix loopForward:

        def loopForward(indexIterator):
            nonlocal freqMap, resultTotal, startPos
            if not (indexIterator < len(s)):
                return

            currentChar = s[indexIterator]
            customIncrement(freqMap, currentChar)

            while isAnyCountGEThreshold(freqMap, k):
                charAtStart = s[startPos]
                customDecrement(freqMap, charAtStart)
                if freqMap.get(charAtStart, 0) == 0:
                    freqMap.pop(charAtStart, None)
                startPos += 1

            resultTotal += startPos

            loopForward(indexIterator + 1)

        loopForward(0)
        return resultTotal