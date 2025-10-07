class Solution:
    def getSmallestString(self, s: str, k: int) -> str:
        def cyclic_distance(c1: str, c2: str) -> int:
            def abs_val(num: int) -> int:
                return -num if num < 0 else num

            charCodeDiff = abs_val(ord(c1) - ord(c2))
            altDist = 26 - charCodeDiff
            return charCodeDiff if charCodeDiff < altDist else altDist

        charList = list(s)
        posCounter = 0
        strLength = len(s)
        valRemain = k

        while True:
            if not (valRemain > 0 and posCounter < strLength):
                break

            if charList[posCounter] == 'a':
                posCounter += 1
                continue

            distToA = cyclic_distance(charList[posCounter], 'a')

            if distToA <= valRemain:
                charList[posCounter] = 'a'
                valRemain -= distToA
            else:
                originalCharCode = ord(charList[posCounter])
                newCharCode = originalCharCode - valRemain
                charList[posCounter] = chr(newCharCode)
                valRemain = 0

            posCounter += 1

        resultStr = ''.join(charList)
        return resultStr