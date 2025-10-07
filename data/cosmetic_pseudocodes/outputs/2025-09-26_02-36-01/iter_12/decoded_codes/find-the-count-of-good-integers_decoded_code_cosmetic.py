class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def replicateFactorials(limit: int, accum: list) -> None:
            if limit < 0:
                return
            replicateFactorials(limit - 1, accum)
            calc = 1
            idx = 1
            while idx <= limit:
                calc *= idx
                idx += 1
            accum.append(calc)

        factorials = []
        replicateFactorials(n, factorials)

        totalCount = 0
        observedPatterns = set()

        def powerOfTen(exp: int) -> int:
            result = 1
            counter = 0
            while counter < exp:
                result *= 10
                counter += 1
            return result

        halfIndex = (n - 1) // 2
        startNumber = powerOfTen(halfIndex)
        upperBound = startNumber * 10 - 1
        currentNum = startNumber

        while currentNum <= upperBound:
            originalStr = ""
            tempNum = currentNum
            while tempNum > 0:
                digitChar = chr((tempNum % 10) + ord('0'))
                originalStr = digitChar + originalStr
                tempNum //= 10
            if originalStr == "":
                originalStr = "0"

            def reverseString(s: str) -> str:
                reversed_str = ""
                pos = len(s) - 1
                while pos >= 0:
                    reversed_str += s[pos]
                    pos -= 1
                return reversed_str

            revStr = reverseString(originalStr)
            suffixStart = n % 2
            suffixStr = ""
            idxSuf = suffixStart
            while idxSuf < len(revStr):
                suffixStr += revStr[idxSuf]
                idxSuf += 1
            fullStr = originalStr + suffixStr

            def stringToInteger(st: str) -> int:
                resNum = 0
                idxConv = 0
                while idxConv < len(st):
                    resNum = resNum * 10 + (ord(st[idxConv]) - ord('0'))
                    idxConv += 1
                return resNum

            if stringToInteger(fullStr) % k != 0:
                currentNum += 1
                continue

            def sortStringCharacters(input_str: str) -> str:
                arrChars = []
                posStr = 0
                while posStr < len(input_str):
                    arrChars.append(input_str[posStr])
                    posStr += 1
                changed = True
                while changed:
                    changed = False
                    posSort = 0
                    while posSort < len(arrChars) - 1:
                        if arrChars[posSort] > arrChars[posSort + 1]:
                            arrChars[posSort], arrChars[posSort + 1] = arrChars[posSort + 1], arrChars[posSort]
                            changed = True
                        posSort += 1
                resultStr = ""
                recIdx = 0
                while recIdx < len(arrChars):
                    resultStr += arrChars[recIdx]
                    recIdx += 1
                return resultStr

            sortedStr = sortStringCharacters(fullStr)

            if sortedStr in observedPatterns:
                currentNum += 1
                continue
            observedPatterns.add(sortedStr)

            def countCharacters(s: str) -> dict:
                countMap = {}
                posMap = 0
                while posMap < len(s):
                    ch = s[posMap]
                    countMap[ch] = countMap.get(ch, 0) + 1
                    posMap += 1
                return countMap

            charCounts = countCharacters(sortedStr)

            lengthN = n
            zeroChar = '0'
            factorialValue = 0

            if zeroChar in charCounts and charCounts[zeroChar] > 0:
                partResult = lengthN - charCounts[zeroChar]
                factorialValue = partResult * factorials[lengthN - 1]
            else:
                factorialValue = factorials[lengthN]

            for key in charCounts.keys():
                factorialValue //= factorials[charCounts[key]]

            totalCount += factorialValue
            currentNum += 1

        return totalCount