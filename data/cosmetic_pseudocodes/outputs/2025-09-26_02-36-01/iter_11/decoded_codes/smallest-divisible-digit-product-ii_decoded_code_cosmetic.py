from collections import Counter

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        def helperIsDivisible(dividend: int, divisor: int) -> bool:
            while dividend % divisor == 0:
                dividend //= divisor
            return dividend == 1

        def helperGetPrimeCount(value: int):
            tally = Counter()
            primeArray = [2, 3, 5, 7]
            tempVal = value
            idx = 0
            while True:
                if idx >= len(primeArray):
                    break
                currentPrime = primeArray[idx]
                while tempVal % currentPrime == 0:
                    tempVal //= currentPrime
                    tally[currentPrime] += 1
                idx += 1
            return tally, (tempVal == 1)

        def helperGetFactorCount(inputCounter: Counter) -> Counter:
            div2_quot, div2_rem = divmod(inputCounter[2], 3)
            div3_quot, div3_rem = divmod(inputCounter[3], 2)
            div4_quot, div2_val = divmod(div2_rem, 2)
            valCount2 = div2_val
            valCount3 = div3_rem
            valCount4 = div4_quot
            valCount8 = div2_quot
            valCount9 = div3_quot

            if valCount2 == 1 and valCount3 == 1:
                valCount2 = 0
                valCount3 = 0
                valCount6 = 1
            else:
                valCount6 = 0

            if valCount3 == 1 and valCount4 == 1:
                valCount2 = 1
                valCount6 = 1
                valCount3 = 0
                valCount4 = 0

            return Counter({
                "2": valCount2,
                "3": valCount3,
                "4": valCount4,
                "5": inputCounter[5],
                "6": valCount6,
                "7": inputCounter[7],
                "8": valCount8,
                "9": valCount9
            })

        primeCountInternal, flagDivisible = helperGetPrimeCount(t)
        if not flagDivisible:
            return "-1"

        factorCountLocal = helperGetFactorCount(primeCountInternal)
        sumFactors = sum(factorCountLocal.values())
        if sumFactors > len(num):
            resultStr = ""
            for keyIndex in factorCountLocal:
                resultStr += keyIndex * factorCountLocal[keyIndex]
            return resultStr

        prefixCounter = Counter()
        for charItem in num:
            cnt, _ = self._getPrimeCount(int(charItem))
            prefixCounter += helperGetFactorCount(cnt)

        posFirstZero = len(num)
        for idxP, ch in enumerate(num):
            if ch == '0':
                posFirstZero = idxP
                break

        if posFirstZero == len(num) and all(primeCountInternal[k] <= prefixCounter[k] for k in primeCountInternal):
            return num

        def recurIterate(idxR: int):
            if idxR < 0:
                return None
            digitVal = int(num[idxR])
            cnt, _ = self._getPrimeCount(digitVal)
            prefixCounter.subtract(helperGetFactorCount(cnt))
            remSpace = len(num) - 1 - idxR

            if idxR <= posFirstZero:
                def tryBiggerDigit(testDigit: int):
                    if testDigit > 9:
                        return None
                    cnt_test, _ = self._getPrimeCount(testDigit)
                    remainFactors = helperGetFactorCount(primeCountInternal - prefixCounter - helperGetFactorCount(cnt_test))
                    sumRemain = sum(remainFactors.values())
                    if sumRemain <= remSpace:
                        extraOnes = remSpace - sumRemain
                        frontPart = num[:idxR]
                        midPart = str(testDigit)
                        onesPart = "1" * extraOnes
                        backPart = ""
                        for keyK in remainFactors:
                            backPart += keyK * remainFactors[keyK]
                        return frontPart + midPart + onesPart + backPart
                    return tryBiggerDigit(testDigit + 1)
                return tryBiggerDigit(digitVal + 1)

            return recurIterate(idxR - 1)

        valResult = recurIterate(len(num) - 1)
        if valResult is not None:
            return valResult

        factorCountLocal = helperGetFactorCount(primeCountInternal)
        sumF = sum(factorCountLocal.values())

        def buildKeyString():
            outStr = ""
            for kPart in factorCountLocal:
                outStr += kPart * factorCountLocal[kPart]
            return outStr

        return "1" * (len(num) + 1 - sumF) + buildKeyString()

    def _getPrimeCount(self, t: int):
        cnt = Counter()
        for p in [2, 3, 5, 7]:
            while t % p == 0:
                t //= p
                cnt[p] += 1
        return cnt, (t == 1)

    def _getFactorCount(self, count: Counter) -> Counter:
        a1, a2 = divmod(count[2], 3)
        b1, b2 = divmod(count[3], 2)
        c1, c2 = divmod(a2, 2)
        valTwo = c2
        valThree = b2
        valFour = c1
        valEight = a1
        valNine = b1
        if valTwo == 1 and valThree == 1:
            valTwo = 0
            valThree = 0
            valSix = 1
        else:
            valSix = 0
        if valThree == 1 and valFour == 1:
            valTwo = 1
            valSix = 1
            valThree = 0
            valFour = 0
        return Counter({
            "2": valTwo,
            "3": valThree,
            "4": valFour,
            "5": count[5],
            "6": valSix,
            "7": count[7],
            "8": valEight,
            "9": valNine
        })