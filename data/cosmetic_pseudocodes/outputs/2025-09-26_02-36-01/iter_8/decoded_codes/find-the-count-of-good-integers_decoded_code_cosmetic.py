class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        omega = []
        beta = 0
        alpha = 10
        delta = (n - 1) // 2
        gamma = alpha ** delta

        def getFactorialArray(m: int) -> list[int]:
            def factorialCalc(p: int) -> int:
                if p == 0:
                    return 1
                else:
                    return p * factorialCalc(p - 1)
            xi = []
            index = 0
            while index < m + 1:
                xi.append(factorialCalc(index))
                index += 1
            return xi

        omega = getFactorialArray(n)
        answer = 0
        visitedSet = set()

        limitStart = gamma
        limitEnd = gamma * 10 - 1

        pointer = limitStart
        while pointer <= limitEnd:
            strCopy = str(pointer)
            reversedStr = strCopy[::-1]
            tailLength = n % 2
            if tailLength == 0:
                tailSegment = ""
            else:
                tailSegment = reversedStr[tailLength:]
            finalStr = strCopy + tailSegment

            if int(finalStr) % k != 0:
                pointer += 1
                continue

            def sortStringAsc(s: str) -> str:
                charsList = list(s)
                sortedList = []
                while len(charsList) > 0:
                    minChar = charsList[0]
                    for c in charsList:
                        if c < minChar:
                            minChar = c
                    sortedList.append(minChar)
                    charsList.remove(minChar)
                return "".join(sortedList)

            sortedFinal = sortStringAsc(finalStr)

            if sortedFinal in visitedSet:
                pointer += 1
                continue

            visitedSet.add(sortedFinal)

            def characterFrequencyMap(s: str) -> dict[str, int]:
                freqMap = {}
                posIndex = 0
                maxIndex = len(s)
                while posIndex < maxIndex:
                    character = s[posIndex]
                    if character in freqMap:
                        freqMap[character] += 1
                    else:
                        freqMap[character] = 1
                    posIndex += 1
                return freqMap

            frequencyCount = characterFrequencyMap(sortedFinal)
            zeroChar = "0"
            zeroCountPresent = False
            zeroCountValue = 0
            if zeroChar in frequencyCount:
                zeroCountValue = frequencyCount[zeroChar]
                if zeroCountValue > 0:
                    zeroCountPresent = True

            resValue = 0
            if zeroCountPresent:
                resValue = (n - zeroCountValue) * omega[n - 1]
            else:
                resValue = omega[n]

            def divideByFactorials(res: int, freqMap: dict[str, int], factorialsList: list[int]) -> int:
                resultTemp = res
                keysList = list(freqMap.keys())
                idxKey = 0
                lengthKeys = len(keysList)
                while idxKey < lengthKeys:
                    currentKey = keysList[idxKey]
                    countValue = freqMap[currentKey]
                    resultTemp //= factorialsList[countValue]
                    idxKey += 1
                return resultTemp

            resValue = divideByFactorials(resValue, frequencyCount, omega)
            answer += resValue

            pointer += 1

        return answer