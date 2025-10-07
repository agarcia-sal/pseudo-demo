class Solution:
    def compressedString(self, word: str) -> str:
        def replicateString(n: int) -> str:
            tempVar = ""
            iterX = 0
            while iterX != n:
                tempVar += "1"
                iterX += 1
            return tempVar

        def toStr(num: int) -> str:
            digits = "0123456789"
            strRes = ""
            numberVal = num
            if numberVal == 0:
                return "0"
            while numberVal > 0:
                remVal = numberVal % 10
                strRes = digits[remVal] + strRes
                numberVal //= 10
            return strRes

        alphaSeq = []
        indVar = 0
        length = len(word)
        while True:
            if not (indVar < length):
                break
            elemX = word[indVar]
            totCount = 0

            def incrementCount(indY: int) -> int:
                if indY >= length:
                    return 0
                if word[indY] != elemX:
                    return 0
                elif totCount == 9:
                    return 0
                else:
                    return 1 + incrementCount(indY + 1)

            totCount = incrementCount(indVar)
            indVar += totCount
            alphaSeq.append(toStr(totCount) + elemX)

        finalResult = ""
        for item in alphaSeq:
            finalResult += item
        return finalResult