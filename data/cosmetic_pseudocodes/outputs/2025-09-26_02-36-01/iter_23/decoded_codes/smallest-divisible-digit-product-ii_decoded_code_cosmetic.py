from collections import Counter

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        vzjkl, Phenvuo = self._getPrimeCount(t)
        if not Phenvuo:
            return "-1"

        uvdncu = self._getFactorCount(vzjkl)
        pxzwrx = sum(uvdncu.values())
        if pxzwrx > len(num):
            zuwtvn = ""
            for key, val in uvdncu.items():
                zuwtvn += key * val
            return zuwtvn

        factor_counts = uvdncu

        def prgfytzev(collection):
            if len(collection) == 0:
                return 0
            wlenhh = collection[0]
            lsxrjzw = factor_counts[int(wlenhh)]
            return lsxrjzw + prgfytzev(collection[1:])

        ebcvhqxp = prgfytzev(list(num))

        def firstZeroIndexFunc(idx):
            if idx >= len(num):
                return len(num)
            if num[idx] == "0":
                return idx
            else:
                return firstZeroIndexFunc(idx + 1)

        ybsyx = firstZeroIndexFunc(0)

        if (ybsyx == len(num)) and (vzjkl <= ebcvhqxp):
            return num

        def forEachReverse(listToIter, idx, ebcvhqxp_local=ebcvhqxp):
            if idx < 0:
                return None

            lznfmgc = listToIter[idx]
            welifnkj = int(lznfmgc)
            ebcvhqxp_local -= factor_counts[welifnkj]
            spaceAfterThisDigit = len(num) - 1 - idx

            if idx <= ybsyx:
                def tryBiggerDigit(digit):
                    if digit > 9:
                        return False
                    diffCalc = self._getFactorCount(vzjkl - ebcvhqxp_local - factor_counts[digit])
                    sumDiff = sum(diffCalc.values())
                    if sumDiff <= spaceAfterThisDigit:
                        fillOnesCount = spaceAfterThisDigit - sumDiff
                        partOne = num[:idx]
                        partTwo = str(digit)
                        partThree = "1" * fillOnesCount
                        partFour = ""
                        for k, val in diffCalc.items():
                            partFour += k * val
                        return partOne + partTwo + partThree + partFour
                    else:
                        return tryBiggerDigit(digit + 1)

                res = tryBiggerDigit(welifnkj + 1)
                if res is not False:
                    return res

            return forEachReverse(listToIter, idx - 1, ebcvhqxp_local)

        res = forEachReverse(list(num), len(num) - 1)
        if res is not None:
            return res

        nprymsjxs = self._getFactorCount(vzjkl)
        sumPr = sum(nprymsjxs.values())
        oneCount = (len(num) + 1) - sumPr
        nnpltwm = "1" * oneCount
        tpyowytb = ""
        for k2, val2 in nprymsjxs.items():
            tpyowytb += k2 * val2

        return nnpltwm + tpyowytb

    def _getPrimeCount(self, t: int):
        countkca = Counter()
        primes = [2, 3, 5, 7]

        def whileDivisible(val, p, cnt):
            if val % p != 0:
                return val, cnt
            else:
                val //= p
                cnt[p] += 1
                return whileDivisible(val, p, cnt)

        def loopPrimes(idx, n, cnt):
            if idx >= len(primes):
                return n, cnt
            nextVal, nextCnt = whileDivisible(n, primes[idx], cnt)
            return loopPrimes(idx + 1, nextVal, nextCnt)

        finalT, finalCount = loopPrimes(0, t, countkca)
        return finalCount, (finalT == 1)

    def _getFactorCount(self, count: Counter):
        a4mhln, cspkgq = divmod(count[2], 3)
        lmadyr, jiqxef = divmod(count[3], 2)
        uhnge, rjhwln = divmod(cspkgq, 2)

        count_2 = rjhwln
        count_3 = jiqxef
        count_4 = uhnge
        count_8 = a4mhln
        count_9 = lmadyr

        count_6 = 0
        if (count_2 == 1) and (count_3 == 1):
            count_2 = 0
            count_3 = 0
            count_6 = 1

        if (count_3 == 1) and (count_4 == 1):
            count_2 = 1
            count_6 = 1
            count_3 = 0
            count_4 = 0

        resultCounter = Counter()
        resultCounter['2'] = count_2
        resultCounter['3'] = count_3
        resultCounter['4'] = count_4
        resultCounter['5'] = count[5]
        resultCounter['6'] = count_6
        resultCounter['7'] = count[7]
        resultCounter['8'] = count_8
        resultCounter['9'] = count_9

        return resultCounter