class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        factorials = []
        idx = 0
        while idx <= n:
            factValue = 1
            step = 1
            while step <= idx:
                factValue *= step
                step += 1
            factorials.append(factValue)
            idx += 1

        resultAcc = 0
        visitedStrings = set()
        halfBase = 10 ** ((n - 1) // 2)
        currentNum = halfBase

        def isDivisible(strVal: str) -> bool:
            numericVal = 0
            pos = 0
            length = len(strVal)
            while pos < length:
                numericVal = numericVal * 10 + (ord(strVal[pos]) - ord('0'))
                pos += 1
            return (numericVal % k) == 0

        def charFrequency(s: str) -> dict:
            freqMap = {}
            for ch in s:
                freqMap[ch] = freqMap.get(ch, 0) + 1
            return freqMap

        def sortStringAsc(strVal: str) -> str:
            charList = list(strVal)
            swapped = True
            while swapped:
                swapped = False
                for i in range(len(charList) - 1):
                    if charList[i] > charList[i + 1]:
                        charList[i], charList[i + 1] = charList[i + 1], charList[i]
                        swapped = True
            return ''.join(charList)

        limit = halfBase * 10
        while currentNum < limit:
            # Convert currentNum to string with no leading zeros since currentNum >= halfBase
            strNum = ''
            tempNum = currentNum
            while True:
                digitChar = chr((tempNum % 10) + ord('0'))
                strNum = digitChar + strNum
                tempNum //= 10
                if tempNum == 0:
                    break

            revStr = ''
            revLen = len(strNum)
            while True:
                revLen -= 1
                if revLen < 0:
                    break
                revStr += strNum[revLen]

            suffixStart = n % 2
            appendedStr = strNum + revStr[suffixStart:]

            if not isDivisible(appendedStr):
                currentNum += 1
                continue

            orderedStr = sortStringAsc(appendedStr)
            if orderedStr in visitedStrings:
                currentNum += 1
                continue

            visitedStrings.add(orderedStr)

            frequencies = charFrequency(orderedStr)
            zeroChar = '0'
            totalRes = 0

            if zeroChar in frequencies and frequencies[zeroChar] > 0:
                totalRes = (n - frequencies[zeroChar]) * factorials[n - 1]
            else:
                totalRes = factorials[n]

            for freqKey in frequencies:
                totalRes //= factorials[frequencies[freqKey]]

            resultAcc += totalRes
            currentNum += 1

        return resultAcc