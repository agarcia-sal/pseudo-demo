class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        def buildFactorials(limit: int, accList: list[int], idx: int) -> list[int]:
            if idx > limit:
                return accList
            else:
                prevVal = 1 if idx == 0 else idx * accList[idx - 1]
                accList.append(prevVal)
                return buildFactorials(limit, accList, idx + 1)

        def factorialList(size: int) -> list[int]:
            return buildFactorials(size, [1], 1)

        def freqCount(txt: str) -> dict[str, int]:
            def helper(i: int, m: dict[str, int]) -> dict[str, int]:
                if i < 0:
                    return m
                else:
                    ch = txt[i]
                    updatedCount = m[ch] + 1 if ch in m else 1
                    newMap = m.copy()
                    newMap[ch] = updatedCount
                    return helper(i - 1, newMap)
            return helper(len(txt) - 1, {})

        factorials = factorialList(n)
        resultSum = 0
        visitedSet: set[str] = set()

        halfBase = 1
        for _ in range((n - 1) // 2):
            halfBase *= 10

        def reverseString(s: str) -> str:
            def revHelper(i: int, acc: str) -> str:
                if i < 0:
                    return acc
                else:
                    return revHelper(i - 1, acc + s[i])
            return revHelper(len(s) - 1, "")

        def substringFrom(s: str, startIdx: int) -> str:
            def subHelper(i: int, acc: str) -> str:
                if i > len(s) - 1:
                    return acc
                else:
                    return subHelper(i + 1, acc + s[i])
            return subHelper(startIdx, "")

        def sortStringAscending(inputStr: str) -> str:
            charsList = [inputStr[i] for i in range(len(inputStr))]
            for pass_ in range(len(charsList) - 1, 0, -1):
                for pos in range(pass_):
                    if charsList[pos] > charsList[pos + 1]:
                        charsList[pos], charsList[pos + 1] = charsList[pos + 1], charsList[pos]
            sortedStr = ""
            for chIdx in range(len(charsList)):
                sortedStr += charsList[chIdx]
            return sortedStr

        def dividesWithoutRemainder(num: int, divisor: int) -> bool:
            return (num - (num // divisor) * divisor) == 0

        def calculateRes(freqMap: dict[str, int], totalLen: int, factorialListInput: list[int]) -> int:
            if '0' in freqMap and freqMap['0'] > 0:
                zeroCount = freqMap['0']
                initialVal = (totalLen - zeroCount) * factorialListInput[totalLen - 1]
            else:
                initialVal = factorialListInput[totalLen]

            def divideAll(factors: list[int], val: int) -> int:
                if len(factors) == 0:
                    return val
                else:
                    head = factors[0]
                    tail = factors[1:]
                    return divideAll(tail, val // factorialListInput[head])

            freqValuesList = []
            for key in freqMap:
                freqValuesList.append(freqMap[key])
            return divideAll(freqValuesList, initialVal)

        def buildPalindrome(num: int) -> str:
            stringNum = str(num)
            revStr = reverseString(stringNum)
            extraPart = substringFrom(revStr, n % 2)
            return stringNum + extraPart

        def iterateAndAccumulate(current: int, maxVal: int, accum: int, visited: set[str]) -> int:
            if current > maxVal:
                return accum
            else:
                palindromeCandidate = buildPalindrome(current)
                if not dividesWithoutRemainder(int(palindromeCandidate), k):
                    return iterateAndAccumulate(current + 1, maxVal, accum, visited)
                sortedForm = sortStringAscending(palindromeCandidate)
                if sortedForm in visited:
                    return iterateAndAccumulate(current + 1, maxVal, accum, visited)
                else:
                    newVisited = visited.copy()
                    newVisited.add(sortedForm)
                    frequencyMap = freqCount(sortedForm)
                    resVal = calculateRes(frequencyMap, n, factorials)
                    return iterateAndAccumulate(current + 1, maxVal, accum + resVal, newVisited)

        maxRange = halfBase * 10 - 1
        finalAnswer = iterateAndAccumulate(halfBase, maxRange, resultSum, visitedSet)
        return finalAnswer