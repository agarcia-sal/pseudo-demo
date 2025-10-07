from collections import Counter

FACTOR_COUNTS = {
    0: Counter(),
    1: Counter(),
    2: Counter({2: 1}),
    3: Counter({3: 1}),
    4: Counter({2: 2}),
    5: Counter({5: 1}),
    6: Counter({2: 1, 3: 1}),
    7: Counter({7: 1}),
    8: Counter({2: 3}),
    9: Counter({3: 2}),
}

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        primeCount, isDivisible = self._getPrimeCount(t)
        if not isDivisible:
            return "-1"

        factorCount = self._getFactorCount(primeCount)
        totalFactors = sum(factorCount.values())
        if totalFactors > len(num):
            # If total factors exceed length of num, just return sorted digits by key ascending:
            resultStr = "".join(digit * freq for digit, freq in sorted(factorCount.items()))
            return resultStr

        primeCountPrefix = Counter()
        for char in num:
            d = int(char)
            primeCountPrefix += FACTOR_COUNTS[d]

        firstZeroIndex = len(num)
        for i, ch in enumerate(num):
            if ch == '0':
                firstZeroIndex = i
                break

        # Check if primeCount <= primeCountPrefix (all counts in primeCount less or equal to primeCountPrefix)
        if firstZeroIndex == len(num) and all(primeCount[p] <= primeCountPrefix.get(p, 0) for p in primeCount):
            return num

        for i in reversed(range(len(num))):
            c = num[i]
            d = int(c)
            primeCountPrefix -= FACTOR_COUNTS[d]
            spaceAfter = len(num) - 1 - i

            if i <= firstZeroIndex:
                for biggerDigit in range(d + 1, 10):
                    needed = primeCount - primeCountPrefix - FACTOR_COUNTS[biggerDigit]
                    # Check if negative counts exist; if negative counts, cannot form
                    if any(v < 0 for v in needed.values()):
                        continue
                    factorsAfter = self._getFactorCount(needed)
                    sum_factors_after = sum(factorsAfter.values())
                    if sum_factors_after <= spaceAfter:
                        fillOnes = spaceAfter - sum_factors_after
                        prefix = num[:i]
                        suffix = "".join(digit * freq for digit, freq in sorted(factorsAfter.items()))
                        return prefix + str(biggerDigit) + '1' * fillOnes + suffix

        # If no suitable replacement found
        factorCount = self._getFactorCount(primeCount)
        onesCount = len(num) + 1 - sum(factorCount.values())
        result = '1' * onesCount
        result += "".join(digit * freq for digit, freq in sorted(factorCount.items()))
        return result

    def _getPrimeCount(self, t: int) -> tuple[Counter, bool]:
        count = Counter()
        for prime in [2, 3, 5, 7]:
            while t % prime == 0:
                t //= prime
                count[prime] += 1
        return count, (t == 1)

    def _getFactorCount(self, count: Counter) -> Counter:
        count8, rem2 = divmod(count.get(2, 0), 3)
        count9, count3 = divmod(count.get(3, 0), 2)
        count4, count2 = divmod(rem2, 2)

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
            '2': count2,
            '3': count3,
            '4': count4,
            '5': count.get(5, 0),
            '6': count6,
            '7': count.get(7, 0),
            '8': count8,
            '9': count9,
        })