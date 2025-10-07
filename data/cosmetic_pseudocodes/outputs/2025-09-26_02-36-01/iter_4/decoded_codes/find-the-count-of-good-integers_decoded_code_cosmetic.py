class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # Precompute factorials from 0! to n!
        factorials = []
        for index in range(n + 1):
            factVal = 1
            mulCounter = 1
            while mulCounter <= index:
                factVal *= mulCounter
                mulCounter += 1
            factorials.append(factVal)

        resultSum = 0
        seenStrings = set()

        halfBase = 10 ** ((n - 1) // 2)
        currentVal = halfBase
        upperBound = (halfBase * 10) - 1

        while currentVal <= upperBound:
            strVal = str(currentVal)

            revStr = ''
            revIndex = len(strVal) - 1
            while revIndex >= 0:
                revStr += strVal[revIndex]
                revIndex -= 1

            remainderIndex = n % 2
            suffixStr = revStr[remainderIndex:]

            strVal_full = strVal + suffixStr

            intVal = int(strVal_full)
            if intVal % k != 0:
                currentVal += 1
                continue

            # Create sorted string to check uniqueness
            sortedChars = []
            charIndex = 0
            while charIndex < len(strVal_full):
                sortedChars.append(strVal_full[charIndex])
                charIndex += 1
            sortedChars.sort()
            tStr = ''.join(sortedChars)

            if tStr in seenStrings:
                currentVal += 1
                continue
            seenStrings.add(tStr)

            frequencyMap = {}
            charIter = 0
            while charIter < len(tStr):
                ch = tStr[charIter]
                if ch not in frequencyMap:
                    frequencyMap[ch] = 1
                else:
                    frequencyMap[ch] += 1
                charIter += 1

            zeroCount = frequencyMap.get('0', 0)

            if zeroCount > 0:
                multiplier = factorials[n - 1]
                resVal = (n - zeroCount) * multiplier
            else:
                resVal = factorials[n]

            for value in frequencyMap.values():
                resVal //= factorials[value]

            resultSum += resVal
            currentVal += 1

        return resultSum