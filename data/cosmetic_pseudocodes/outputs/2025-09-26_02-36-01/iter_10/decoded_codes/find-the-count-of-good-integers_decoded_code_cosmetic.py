class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def calcFactorial(m: int) -> int:
            if m <= 1:
                return 1
            else:
                return m * calcFactorial(m - 1)

        def toString(val: int) -> str:
            digits = []
            temp = val
            while temp > 0:
                digits.append(chr((temp % 10) + 48))
                temp //= 10
            if len(digits) == 0:
                return "0"
            # Reverse digits
            reversed_digits = []
            while digits:
                reversed_digits.append(digits.pop())
            return "".join(reversed_digits)

        def reverseString(s: str) -> str:
            result = []
            idx = len(s) - 1
            while idx >= 0:
                result.append(s[idx])
                idx -= 1
            return "".join(result)

        def substringFrom(s: str, startIdx: int) -> str:
            result = []
            idx = startIdx
            while idx < len(s):
                result.append(s[idx])
                idx += 1
            return "".join(result)

        def sortStringAsc(s: str) -> str:
            chars = []
            pos = 0
            while pos < len(s):
                chars.append(s[pos])
                pos += 1

            def insertionSort(arr: list) -> list:
                i = 1
                while i < len(arr):
                    key = arr[i]
                    j = i - 1
                    while j >= 0 and arr[j] > key:
                        arr[j + 1] = arr[j]
                        j -= 1
                    arr[j + 1] = key
                    i += 1
                return arr

            chars = insertionSort(chars)
            sortedStr = []
            pos = 0
            while pos < len(chars):
                sortedStr.append(chars[pos])
                pos += 1
            return "".join(sortedStr)

        def frequencyMap(s: str) -> dict:
            freq = {}
            p = 0
            while p < len(s):
                c = s[p]
                if c in freq:
                    freq[c] += 1
                else:
                    freq[c] = 1
                p += 1
            return freq

        tempList = []
        idx = 0
        while idx <= n:
            tempList.append(calcFactorial(idx))
            idx += 1

        resultSum = 0
        visitedSet = set()

        expBase = 10 ** ((n - 1) // 2)
        current = expBase

        while current < expBase * 10:
            baseStr = toString(current)
            restPart = substringFrom(reverseString(baseStr), n % 2)
            baseStr = baseStr + restPart

            value = 0
            pos = 0
            while pos < len(baseStr):
                value = value * 10 + (ord(baseStr[pos]) - 48)
                pos += 1

            if value % k != 0:
                current += 1
                continue

            ordered = sortStringAsc(baseStr)
            if ordered in visitedSet:
                current += 1
                continue

            visitedSet.add(ordered)
            freqDict = frequencyMap(ordered)

            if '0' in freqDict and freqDict['0'] > 0:
                resValue = (n - freqDict['0']) * tempList[n - 1]
            else:
                resValue = tempList[n]

            for v in freqDict.values():
                resValue //= tempList[v]

            resultSum += resValue
            current += 1

        return resultSum