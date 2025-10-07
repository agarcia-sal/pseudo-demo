from collections import Counter

class Solution:
    FACTOR_COUNTS = {
        0: Counter(), 1: Counter(),
        2: Counter({"2": 1}),
        3: Counter({"3": 1}),
        4: Counter({"2": 2}),
        5: Counter({"5": 1}),
        6: Counter({"3": 1, "2": 1}),
        7: Counter({"7": 1}),
        8: Counter({"2": 3}),
        9: Counter({"3": 2}),
    }

    def smallestNumber(self, num: str, t: int) -> str:
        prCnt, divFlag = self._getPrimeCount(t)
        if not divFlag:
            return "-1"

        fctCnt = self._getFactorCount(prCnt)
        sumFctCnt = sum(fctCnt.values())
        if sumFctCnt > len(num):
            ans = ""
            for k in sorted(fctCnt.keys(), key=int):
                ans += k * fctCnt[k]
            return ans

        prefixCount = Counter()
        for ch in num:
            prefixCount += self.FACTOR_COUNTS[int(ch)]

        zeroPos = len(num)
        for i, ch in enumerate(num):
            if ch == '0':
                zeroPos = i
                break

        # Check if prime counts fit in prefixCount, return num if so and no zero
        if zeroPos == len(num) and all(prCnt.get(p, 0) <= prefixCount.get(str(p), 0) for p in prCnt):
            return num

        idx = len(num) - 1
        while idx >= 0:
            curDigit = int(num[idx])
            prefixCount -= self.FACTOR_COUNTS[curDigit]
            freeSpace = (len(num) - 1) - idx
            if idx <= zeroPos:
                nextDigit = curDigit + 1
                while nextDigit <= 9:
                    needed = prCnt.copy()
                    # Subtract prefixCount from prCnt to find what remains to fulfill
                    for k in prefixCount:
                        if k.isdigit():
                            needed[int(k)] = needed.get(int(k), 0) - prefixCount[k]
                    # After deduction needed might have negative values which we ignore
                    for k in list(needed.keys()):
                        if needed[k] <= 0:
                            needed.pop(k)
                    # Add the factors of nextDigit to prefixCount for testing different nextDigits
                    testCount = prefixCount + self.FACTOR_COUNTS[nextDigit]
                    # Compare needed with testCount to decide feasibility:
                    # Actually, pseudocode calls _getFactorCount(prCnt - prefixCount - FACTOR_COUNTS[nextDigit])
                    # Implement that: combine prCnt - prefixCount - FACTOR_COUNTS[nextDigit]

                    # Compute remaining prime factors after removing prefixCount and nextDigit's prime factors
                    # prCnt - prefixCount - FACTOR_COUNTS[nextDigit]
                    # We'll compute primeFactorsNeeded as prCnt minus prefixCount minus nextDigit factors, all in Counter form

                    def counter_subtract(c1, c2):
                        res = Counter()
                        for k in c1:
                            v = c1.get(k, 0) - c2.get(k, 0)
                            if v > 0:
                                res[k] = v
                        return res

                    nextFactors = self._getFactorCount(counter_subtract(counter_subtract(prCnt, prefixCount), self.FACTOR_COUNTS[nextDigit]))
                    sumNextFactors = sum(nextFactors.values())

                    if sumNextFactors <= freeSpace:
                        fillOnesCount = freeSpace - sumNextFactors
                        resultStr = ""
                        if idx > 0:
                            resultStr += num[:idx]
                        resultStr += str(nextDigit)
                        resultStr += '1' * fillOnesCount
                        for factor in sorted(nextFactors.keys(), key=int):
                            resultStr += factor * nextFactors[factor]
                        return resultStr
                    nextDigit += 1
            idx -= 1

        finalFactors = self._getFactorCount(prCnt)
        remainCount = len(num) + 1 - sum(finalFactors.values())
        result = '1' * remainCount
        for k in sorted(finalFactors.keys(), key=int):
            result += k * finalFactors[k]
        return result

    def _getPrimeCount(self, t: int) -> tuple[Counter, bool]:
        primeFactors = Counter()
        primes = [2, 3, 5, 7]
        index = 0
        while index < len(primes):
            while t % primes[index] == 0:
                t //= primes[index]
                primeFactors[primes[index]] = primeFactors.get(primes[index], 0) + 1
            index += 1
        flag = (t == 1)
        return primeFactors, flag

    def _getFactorCount(self, count: Counter) -> Counter:
        # Ensure counts for primes 2,3,5,7 exist in count for easier operations
        getc = lambda x: count.get(x, 0)
        two_count = getc(2)
        three_count = getc(3)
        five_count = getc(5)
        seven_count = getc(7)

        twoCountThreeDiv = two_count // 3
        twoCountRem = two_count % 3
        threeCountTwoDiv = three_count // 2
        threeCountRem = three_count % 2
        fourCountDiv = twoCountRem // 2
        twoCountRemFinal = twoCountRem % 2

        sixCount = 0
        if twoCountRemFinal == 1 and threeCountRem == 1:
            twoCountRemFinal = 0
            threeCountRem = 0
            sixCount = 1

        if threeCountRem == 1 and fourCountDiv == 1:
            twoCountRemFinal = 1
            sixCount = 1
            threeCountRem = 0
            fourCountDiv = 0

        resultCounter = Counter()
        if twoCountRemFinal > 0:
            resultCounter["2"] = twoCountRemFinal
        if threeCountRem > 0:
            resultCounter["3"] = threeCountRem
        if fourCountDiv > 0:
            resultCounter["4"] = fourCountDiv
        if five_count > 0:
            resultCounter["5"] = five_count
        if sixCount > 0:
            resultCounter["6"] = sixCount
        if seven_count > 0:
            resultCounter["7"] = seven_count
        if twoCountThreeDiv > 0:
            resultCounter["8"] = twoCountThreeDiv
        if threeCountTwoDiv > 0:
            resultCounter["9"] = threeCountTwoDiv
        return resultCounter