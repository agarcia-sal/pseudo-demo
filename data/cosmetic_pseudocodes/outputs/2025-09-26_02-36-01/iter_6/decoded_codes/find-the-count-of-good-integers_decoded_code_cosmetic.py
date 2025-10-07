class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        factorials = []

        def calcFactorial(m: int) -> int:
            if m <= 1:
                return 1
            else:
                return m * calcFactorial(m - 1)

        idx = 0
        limit = n  # (n + 1) - 1 is n
        while idx < limit:
            f = calcFactorial(idx)
            factorials.append(f)
            idx += 1

        resultSum = 0
        seenPatterns = set()
        midBase = 10 ** ((n - 1) // 2)

        def reverseString(s: str) -> str:
            if len(s) <= 1:
                return s
            else:
                return reverseString(s[1:]) + s[0]

        def getFrequencyMap(text: str) -> dict:
            freqMap = {}
            pos = 0
            length = len(text)
            while pos < length:
                ch = text[pos]
                freqMap[ch] = freqMap.get(ch, 0) + 1
                pos += 1
            return freqMap

        def sortString(inputStr: str) -> str:
            # Bubble sort as in pseudocode
            charList = list(inputStr)
            i = 0
            length = len(charList)
            while i < length - 1:
                j = 0
                while j < length - i - 1:
                    if charList[j] > charList[j + 1]:
                        charList[j], charList[j + 1] = charList[j + 1], charList[j]
                    j += 1
                i += 1
            return "".join(charList)

        currentNum = midBase
        upperBound = midBase * 10
        while True:
            s1 = str(currentNum)
            revPart = reverseString(s1)
            offset = n % 2
            tailSubstr = revPart[offset:]
            combinedStr = s1 + tailSubstr

            if int(combinedStr) % k != 0:
                currentNum += 1
                if currentNum >= upperBound:
                    break
                continue

            sortedStr = sortString(combinedStr)

            if sortedStr in seenPatterns:
                currentNum += 1
                if currentNum >= upperBound:
                    break
                continue
            else:
                seenPatterns.add(sortedStr)

            freqCounter = getFrequencyMap(sortedStr)

            calculationResult = 0

            zeroCount = freqCounter.get('0', 0)
            if zeroCount > 0:
                calculationResult = (n - zeroCount) * factorials[n - 1]
            else:
                calculationResult = factorials[n]

            for val in freqCounter.values():
                calculationResult //= factorials[val]

            resultSum += calculationResult

            currentNum += 1
            if currentNum >= upperBound:
                break

        return resultSum