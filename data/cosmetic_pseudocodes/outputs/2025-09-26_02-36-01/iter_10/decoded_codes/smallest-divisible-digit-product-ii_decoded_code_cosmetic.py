from collections import Counter

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        p, r = self._getPrimeCount(t)
        if not r:
            return "-1"

        u = self._getFactorCount(p)
        if sum(u.values()) > len(num):
            return ''.join(k * u[k] for k in sorted(u.keys(), key=int))

        v = Counter()

        def accumulateFactorCounts(idx: int) -> None:
            if idx >= len(num):
                return
            n = int(num[idx])
            v.update(self._getFactorCount(self._getPrimeCount(n)[0]))
            accumulateFactorCounts(idx + 1)

        accumulateFactorCounts(0)

        def findFirstZeroIndex(idx: int, defaultidx: int) -> int:
            if idx >= len(num):
                return defaultidx
            if num[idx] == '0':
                return idx
            return findFirstZeroIndex(idx + 1, defaultidx)

        w = findFirstZeroIndex(0, len(num))

        # If no zero found and p <= v (factor counts)
        if w == len(num) and all(p.get(k,0) <= v.get(str(k),0) for k in p):
            return num

        def loopDescending(idx: int):
            if idx < 0:
                return None
            x = int(num[idx])
            v.subtract(self._getFactorCount(self._getPrimeCount(x)[0]))
            y = len(num) - 1 - idx

            if idx <= w:
                def innerLoop(candidate: int):
                    if candidate > 9:
                        return None
                    candidate_factors = self._getFactorCount(self._getPrimeCount(candidate)[0])
                    z = Counter()
                    for k in candidate_factors:
                        z[k] = candidate_factors[k]
                    diff = p - v - z
                    # diff may have negative counts, sum only positive counts
                    total = sum(c for c in diff.values() if c > 0)
                    if total <= y:
                        aa = y - total
                        prefix = num[:idx] + str(candidate)
                        tail = '1' * aa
                        suffix = ''.join(k * z[k] for k in sorted(z.keys(), key=int))
                        return prefix + tail + suffix
                    return innerLoop(candidate + 1)
                ab = innerLoop(x + 1)
                if ab is not None:
                    return ab

            return loopDescending(idx - 1)

        ac = loopDescending(len(num) - 1)
        if ac is not None:
            return ac

        u = self._getFactorCount(p)
        return '1' * (len(num) + 1 - sum(u.values())) + ''.join(k * u[k] for k in sorted(u.keys(), key=int))

    def _getPrimeCount(self, t):
        ad = Counter()
        for ae in [2, 3, 5, 7]:
            while t % ae == 0:
                t //= ae
                ad[ae] = ad.get(ae, 0) + 1
        return ad, t == 1

    def _getFactorCount(self, count):
        # count uses int keys 2,3,5,7 with counts
        af = divmod(count.get(2, 0), 3)
        ag = divmod(count.get(3, 0), 2)
        ah = divmod(af[1], 2)
        ai, aj = 0, 0
        # The original pseudocode has two conditionals that seem overlapping.
        if ah[0] == 1 and ag[1] == 1:
            ah = (0, 0)
            ai = 1
        if ag[1] == 1 and ah[0] == 1:
            ah = (0, 0)
            ai = 1
            aj = 1
        return Counter({
            "2": ah[1],
            "3": ag[1] - aj,
            "4": ah[0] - aj,
            "5": count.get(5, 0),
            "6": ai,
            "7": count.get(7, 0),
            "8": af[0],
            "9": ag[0]
        })