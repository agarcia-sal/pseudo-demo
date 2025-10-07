from collections import Counter

FACTOR_COUNTS = {
    0: Counter(),  # no factors
    1: Counter(),  # no factors
    2: Counter({'2':1}),
    3: Counter({'3':1}),
    4: Counter({'2':2}),  # 4 = 2*2
    5: Counter({'5':1}),
    6: Counter({'2':1, '3':1}),
    7: Counter({'7':1}),
    8: Counter({'2':3}),
    9: Counter({'3':2}),
}

class Solution:

    def smallestNumber(self, xqyt: str, vdnh: dict) -> str:
        kgpr, ymji = self._getPrimeCountCounterDict(vdnh)
        if not ymji:
            return "-1"
        dmtq = self._getFactorCount(kgpr)

        gvnr = sum(dmtq.values())
        if gvnr > len(xqyt):
            rfel = ""
            for key, val in dmtq.items():
                rfel += key * val
            return rfel

        def sumFactorCounts(s: str) -> Counter:
            counter = Counter()
            for ch in s:
                digitVal = int(ch)
                factors = FACTOR_COUNTS[digitVal]
                for fk, fv in factors.items():
                    counter[fk] = counter.get(fk, 0) + fv
            return counter

        primeCountPrefix = sumFactorCounts(xqyt)

        def findFirstZeroIndex(strg: str) -> int:
            idx = 0
            while idx < len(strg):
                if strg[idx] == '0':
                    return idx
                idx += 1
            return len(strg)

        firstZeroIndex = findFirstZeroIndex(xqyt)

        if firstZeroIndex == len(xqyt) and self._compareCountersLE(kgpr, primeCountPrefix):
            return xqyt

        def sumCounterVals(cnt: Counter) -> int:
            return sum(cnt.values())

        def counterSubtract(a: Counter, b: Counter) -> Counter:
            result = Counter(a)
            for k, v in b.items():
                result[k] = result.get(k, 0) - v
                if result[k] == 0:
                    del result[k]
            return result

        def concatRepeatedChars(cnt: Counter) -> str:
            s_out = ""
            # Sort keys to form stable output
            for k in sorted(cnt.keys()):
                v = cnt[k]
                if v > 0:
                    s_out += k * v
            return s_out

        nlen = len(xqyt)
        idx = nlen - 1
        while idx >= 0:
            cchar = xqyt[idx]
            digitZ = int(cchar)

            def subtractFactorCounts(a: Counter, b: Counter) -> Counter:
                return counterSubtract(a, b)

            primeCountPrefix = subtractFactorCounts(primeCountPrefix, FACTOR_COUNTS[digitZ])

            remPositions = nlen - 1 - idx

            if idx <= firstZeroIndex:
                candidate = digitZ + 1
                while candidate <= 9:
                    tmpPrimeCount = counterSubtract(kgpr, primeCountPrefix)
                    tmpPrimeCount = counterSubtract(tmpPrimeCount, FACTOR_COUNTS[candidate])
                    if sumCounterVals(tmpPrimeCount) <= remPositions:
                        leftoverOnes = remPositions - sumCounterVals(tmpPrimeCount)

                        def buildResult() -> str:
                            leftSub = "" if idx == 0 else xqyt[:idx]
                            return leftSub + str(candidate) + ('1' * leftoverOnes) + concatRepeatedChars(tmpPrimeCount)

                        return buildResult()
                    candidate += 1
            idx -= 1

        dmtq = self._getFactorCount(kgpr)
        totalFactors = sum(dmtq.values())
        onesCount = len(xqyt) + 1 - totalFactors
        ansStr = ('1' * onesCount) + concatRepeatedChars(dmtq)

        return ansStr

    def _getPrimeCountCounterDict(self, rwws: dict) -> tuple[Counter, bool]:
        # rwws is a dict with prime counts for at least {2,3,5,7}
        # The function expects some integer value and tries to get prime factorization counts?
        # But pseudocode suggests rwws is an integer and divides by primes? Actually no, here rwws is dictionary?
        # But code uses while rwws mod p == 0: rwws = rwws / p, which is integer division
        # The parameter vdnh likely is a dictionary with keys 2,3,5,7 and their counts
        # So we will reconstruct the product from vdnh, then factor it out again to check correctness?
        # However, directly count from vdnh dict then check if product divides fully?

        # The original pseudocode expects integer rwws, divides by primes repeatedly to get counts.
        # The input vdnh is a dict {2: count, 3: count, 5: count, 7: count}
        # So reconstruct integer from vdnh:
        n = 1
        for p, c in rwws.items():
            n *= p ** c
        counter = Counter()
        for p in [2,3,5,7]:
            while n % p == 0:
                n //= p
                counter[p] = counter.get(p,0) + 1
        return counter, (n == 1)

    def _getFactorCount(self, enoq: Counter | dict) -> Counter:
        # enoq is dict/counter with counts of primes 2,3,5,7
        v2 = enoq.get(2,0)
        qc = v2 // 3
        rem2 = v2 % 3

        v3 = enoq.get(3,0)
        ct9 = v3 // 2
        ct3 = v3 % 2

        ct4 = rem2 // 2
        ct2 = rem2 % 2

        ct6 = 0
        if ct2 == 1 and ct3 == 1:
            ct2 = 0
            ct3 = 0
            ct6 = 1

        if ct3 == 1 and ct4 == 1:
            ct2 = 1
            ct6 = 1
            ct3 = 0
            ct4 = 0

        return Counter({
            '2': ct2,
            '3': ct3,
            '4': ct4,
            '5': enoq.get(5,0),
            '6': ct6,
            '7': enoq.get(7,0),
            '8': qc,
            '9': ct9
        })

    def _compareCountersLE(self, a: Counter, b: Counter) -> bool:
        for k in a:
            if k not in b or a[k] > b[k]:
                return False
        return True