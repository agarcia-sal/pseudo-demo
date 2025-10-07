class Solution:
    FACTOR_COUNTS = {
        0: {},
        1: {},
        2: {"2": 1},
        3: {"3": 1},
        4: {"2": 2},
        5: {"5": 1},
        6: {"2": 1, "3": 1},
        7: {"7": 1},
        8: {"2": 3},
        9: {"3": 2},
    }

    def smallestNumber(self, num: str, t: int) -> str:
        NEG_ONE_STR = "-1"
        ONE_CHAR = "1"
        ZERO_CHAR = "0"

        primeCounter, divisibleFlag = self._getPrimeCount(t)
        if not divisibleFlag:
            return NEG_ONE_STR

        factorFrequency = self._getFactorCount(primeCounter)
        sumFactors = sum(factorFrequency.values())
        if sumFactors > len(num):
            assembledString = ""
            for key in factorFrequency:
                assembledString += key * factorFrequency[key]
            return assembledString

        def sumPrefixFactors(stringVal):
            aggregateCounter = {}
            for digitChar in stringVal:
                digitVal = int(digitChar)
                factorCountMap = self.FACTOR_COUNTS.get(digitVal, {})
                for factorKey in factorCountMap:
                    aggregateCounter[factorKey] = aggregateCounter.get(factorKey, 0) + factorCountMap[factorKey]
            return aggregateCounter

        primeCounterPrefix = sumPrefixFactors(num)

        def findFirstZeroIndex(s):
            for pos, ch in enumerate(s):
                if ch == ZERO_CHAR:
                    return pos
            return len(s)

        idxFirstZero = findFirstZeroIndex(num)

        def countersum(counterMap):
            return sum(counterMap.values())

        def compareCounters(c1, c2):
            sum1 = countersum(c1)
            sum2 = countersum(c2)
            return sum1 - sum2

        def addCounters(c1, c2):
            res = c1.copy()
            for k, v in c2.items():
                res[k] = res.get(k, 0) + v
            return res

        def subtractCounters(c1, c2):
            res = c1.copy()
            for k, v in c2.items():
                res[k] = res.get(k, 0) - v
            # clean zero or negative entries (not strictly needed but safer)
            keys_to_del = [k for k, v in res.items() if v <= 0]
            for k in keys_to_del:
                if res[k] == 0:
                    del res[k]
            return res

        if idxFirstZero == len(num) and compareCounters(primeCounter, primeCounterPrefix) <= 0:
            return num

        n = len(num)
        idx = n - 1
        while idx >= 0:
            currentDigit = int(num[idx])
            for factorKey in primeCounterPrefix:
                primeCounterPrefix[factorKey] = primeCounterPrefix.get(factorKey,0) - self.FACTOR_COUNTS.get(currentDigit, {}).get(factorKey, 0)
                if primeCounterPrefix[factorKey] == 0:
                    del primeCounterPrefix[factorKey]
            positionsAfter = (n - 1) - idx

            if idx <= idxFirstZero:
                nextDigit = currentDigit + 1
                while nextDigit <= 9:
                    sum_prefix_plus = addCounters(primeCounterPrefix, self.FACTOR_COUNTS.get(nextDigit, {}))
                    residueCounter = self._getFactorCount(subtractCounters(primeCounter, sum_prefix_plus))
                    if countersum(residueCounter) <= positionsAfter:
                        onesCount = positionsAfter - countersum(residueCounter)
                        prefixString = num[:idx]
                        onesString = ONE_CHAR * onesCount
                        residualString = ""
                        for factorDigit in sorted(residueCounter.keys()):
                            residualString += factorDigit * residueCounter[factorDigit]
                        return prefixString + str(nextDigit) + onesString + residualString
                    nextDigit += 1
            idx -= 1

        factorCountFinal = self._getFactorCount(primeCounter)
        totalFinalCount = countersum(factorCountFinal)
        finalOnesCount = len(num) + 1 - totalFinalCount
        returnOnes = ONE_CHAR * finalOnesCount
        returnResidual = ""
        for factorDigit in sorted(factorCountFinal.keys()):
            returnResidual += factorDigit * factorCountFinal[factorDigit]
        return returnOnes + returnResidual

    def _getPrimeCount(self, t: int):
        primes = [2, 3, 5, 7]
        primeCountMap = {}
        for eachPrime in primes:
            while t % eachPrime == 0:
                t //= eachPrime
                primeCountMap[eachPrime] = primeCountMap.get(eachPrime, 0) + 1
        return primeCountMap, (t == 1)

    def _getFactorCount(self, counterMap):
        count2val = counterMap.get(2, 0)
        count3val = counterMap.get(3, 0)
        count5val = counterMap.get(5, 0)
        count7val = counterMap.get(7, 0)

        c8, rem2 = divmod(count2val, 3)
        c9, rem3 = divmod(count3val, 2)
        c4, c2 = divmod(rem2, 2)

        c6 = 0
        if c2 == 1 and rem3 == 1:
            c2 = 0
            rem3 = 0
            c6 = 1

        if rem3 == 1 and c4 == 1:
            c2 = 1
            c6 = 1
            rem3 = 0
            c4 = 0

        return {
            "2": c2,
            "3": rem3,
            "4": c4,
            "5": count5val,
            "6": c6,
            "7": count7val,
            "8": c8,
            "9": c9,
        }