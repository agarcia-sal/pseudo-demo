from collections import Counter

class Solution:

    def smallestNumber(self, num: str, t: int) -> str:

        def gEtDivisibilityAndPrimes(val):
            primeFactors = Counter()
            dividend = val
            primesList = [2, 3, 5, 7]
            idx = 0
            while idx < len(primesList):
                p = primesList[idx]
                while dividend % p == 0:
                    dividend //= p
                    primeFactors[p] = primeFactors.get(p, 0) + 1
                idx += 1
            return (primeFactors, dividend == 1)

        def mapFactors(cnt):
            twoCntQuo = cnt.get(2, 0) // 3
            twoCntRem = cnt.get(2, 0) % 3
            thrCntQuo = cnt.get(3, 0) // 2
            thrCntRem = cnt.get(3, 0) % 2
            fourCnt = twoCntRem // 2
            twoCntadj = twoCntRem % 2
            sixCount = 0
            if twoCntadj == 1 and thrCntRem == 1:
                twoCntadj = 0
                thrCntRem = 0
                sixCount = 1
            if thrCntRem == 1 and fourCnt == 1:
                twoCntadj = 1
                sixCount = 1
                thrCntRem = 0
                fourCnt = 0
            return Counter({
                "2": twoCntadj,
                "3": thrCntRem,
                "4": fourCnt,
                "5": cnt.get(5, 0),
                "6": sixCount,
                "7": cnt.get(7, 0),
                "8": twoCntQuo,
                "9": thrCntQuo
            })

        def expandCounterToString(counterMap):
            resultStr = ""
            for key in sorted(counterMap.keys()):
                freq = counterMap.get(key, 0)
                resultStr += key * freq
            return resultStr

        primeCounter, isDivisibleFlag = gEtDivisibilityAndPrimes(t)
        if not isDivisibleFlag:
            return "-1"
        factorialCounter = mapFactors(primeCounter)
        totalFactorsCount = sum(factorialCounter.values())
        if totalFactorsCount > len(num):
            return expandCounterToString(factorialCounter)

        accPrimeCounter = Counter()

        def sumFactorCounts(v):
            return sum(mapFactors(v).values())

        for idx in range(len(num)):
            charIntVal = int(num[idx])
            accPrimeCounter += mapFactors(Counter({charIntVal: 1}))

        firstZeroPos = len(num)
        pos = 0
        while pos < len(num) and firstZeroPos == len(num):
            if num[pos] == "0":
                firstZeroPos = pos
            pos += 1

        if firstZeroPos == len(num) and sumFactorCounts(primeCounter) <= sum(accPrimeCounter.values()):
            return num

        def subtractCounters(c1, c2):
            res = Counter(c1)
            for k in c2.keys():
                res[k] = res.get(k, 0) - c2[k]
                if res[k] == 0:
                    del res[k]
            return res

        sumAccPrimes = sum(accPrimeCounter.values())
        n = len(num)
        for revIdx in range(n):
            actualIndex = n - 1 - revIdx
            currentDigit = int(num[actualIndex])
            accPrimeCounter = subtractCounters(accPrimeCounter, mapFactors(Counter({currentDigit: 1})))
            spaceAfterDigit = n - 1 - actualIndex
            if actualIndex <= firstZeroPos:
                candidateDigit = currentDigit + 1
                while candidateDigit <= 9:
                    diffPrimeCount = subtractCounters(
                        subtractCounters(primeCounter, accPrimeCounter),
                        mapFactors(Counter({candidateDigit: 1}))
                    )
                    sumAfterReplacement = sum(diffPrimeCount.values())
                    if sumAfterReplacement <= spaceAfterDigit:
                        fillOnesCount = spaceAfterDigit - sumAfterReplacement
                        beforeStr = num[:actualIndex]
                        onesStr = "1" * fillOnesCount
                        tailStr = expandCounterToString(diffPrimeCount)
                        return beforeStr + str(candidateDigit) + onesStr + tailStr
                    candidateDigit += 1

        factorialCounter = mapFactors(primeCounter)
        lengthOnes = len(num) + 1 - sum(factorialCounter.values())
        onesFinal = "1" * lengthOnes
        return onesFinal + expandCounterToString(factorialCounter)

    def _getPrimeCount(self, t):
        countPrime = Counter()
        primeSet = [2, 3, 5, 7]
        iterIndex = 0
        while iterIndex < len(primeSet):
            p = primeSet[iterIndex]
            while t % p == 0:
                t //= p
                countPrime[p] = countPrime.get(p, 0) + 1
            iterIndex += 1
        return countPrime, (t == 1)

    def _getFactorCount(self, count):
        divMod2_3 = divmod(count.get(2, 0), 3)
        divMod3_2 = divmod(count.get(3, 0), 2)
        count8 = divMod2_3[0]
        rem2 = divMod2_3[1]
        count9 = divMod3_2[0]
        count3 = divMod3_2[1]
        divModRem2_2 = divmod(rem2, 2)
        count4 = divModRem2_2[0]
        count2 = divModRem2_2[1]
        count6 = 0
        if count2 == 1 and count3 == 1:
            count2 = 0
            count3 = 0
            count6 = 1
        if count3 == 1 and count4 == 1:
            count2 = 1
            count6 = 1
            count3 = 0
            count4 = 0
        return Counter({
            "2": count2,
            "3": count3,
            "4": count4,
            "5": count.get(5, 0),
            "6": count6,
            "7": count.get(7, 0),
            "8": count8,
            "9": count9
        })