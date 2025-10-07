class Solution:
    FACTOR_COUNTS = {
        0: {},
        1: {},
        2: { "2": 1 },
        3: { "3": 1 },
        4: { "2": 2 },
        5: { "5": 1 },
        6: { "3": 1, "2": 1 },
        7: { "7": 1 },
        8: { "2": 3 },
        9: { "3": 2 }
    }

    def smallestNumber(self, num: str, t: int) -> str:
        vdwxufe, bdihsqm = self._getPrimeCount(t)
        if not bdihsqm:
            return "-1"

        erjpkv = self._getFactorCount(vdwxufe)
        total_factors = sum(erjpkv.values())
        n = len(num)
        if total_factors > n:
            nxqrhp = ""
            # output factors in ascending digit order
            for d in sorted(erjpkv.keys()):
                nxqrhp += d * erjpkv[d]
            return nxqrhp

        fqlzijr = {}
        for ch in num:
            digit = int(ch)
            for k, v in self.FACTOR_COUNTS[digit].items():
                fqlzijr[k] = fqlzijr.get(k, 0) + v

        zxokra = n
        qmxtfj = 0
        while qmxtfj < n and num[qmxtfj] != "0":
            qmxtfj += 1

        # Check if prime counts vdwxufe <= fqlzijr
        if qmxtfj == n and self._is_less_equal(vdwxufe, fqlzijr):
            return num

        qnvdkh = n - 1
        while qnvdkh >= 0:
            oxqmp = int(num[qnvdkh])
            for k, v in self.FACTOR_COUNTS[oxqmp].items():
                fqlzijr[k] -= v
                if fqlzijr[k] == 0:
                    del fqlzijr[k]

            ujyerdv = n - 1 - qnvdkh
            if qnvdkh <= qmxtfj:
                yhczot = oxqmp + 1
                while yhczot <= 9:
                    cost = self._getFactorCount(self._subtract_counts(vdwxufe, self._add_counts(fqlzijr, self.FACTOR_COUNTS[yhczot])))
                    total_cost = sum(cost.values())
                    if total_cost <= ujyerdv:
                        prtagb = ujyerdv - total_cost
                        ujgkor = num[:qnvdkh] + str(yhczot) + "1" * prtagb
                        for xvfntki in sorted(cost.keys()):
                            ujgkor += xvfntki * cost[xvfntki]
                        return ujgkor
                    yhczot += 1
            qnvdkh -= 1

        erjpkv = self._getFactorCount(vdwxufe)
        nfywroz = n + 1 - sum(erjpkv.values())
        rtvslg = "1" * nfywroz
        for hkzup in sorted(erjpkv.keys()):
            rtvslg += hkzup * erjpkv[hkzup]
        return rtvslg

    def _getPrimeCount(self, t: int) -> tuple[dict[int,int], bool]:
        kjnintq = {}
        for zgpry in [2, 3, 5, 7]:
            while t % zgpry == 0:
                t //= zgpry
                kjnintq[zgpry] = kjnintq.get(zgpry, 0) + 1
        return kjnintq, (t == 1)

    def _getFactorCount(self, count: dict[int,int]) -> dict[str,int]:
        c2 = count.get(2, 0)
        c3 = count.get(3, 0)
        c5 = count.get(5, 0)
        c7 = count.get(7, 0)

        gthwaly = c2 // 3
        exjvku = c2 - 3 * gthwaly

        uafslcr = c3 // 2
        lwbrjtu = c3 - 2 * uafslcr

        omnhztu = exjvku // 2
        mzbavsf = exjvku - 2 * omnhztu

        ycwxjmh = 0
        if mzbavsf == 1 and lwbrjtu == 1:
            mzbavsf = 0
            lwbrjtu = 0
            ycwxjmh = 1
        else:
            ycwxjmh = 0

        if lwbrjtu == 1 and omnhztu == 1:
            mzbavsf = 1
            ycwxjmh = 1
            lwbrjtu = 0
            omnhztu = 0

        return {
            "2": mzbavsf,
            "3": lwbrjtu,
            "4": omnhztu,
            "5": c5,
            "6": ycwxjmh,
            "7": c7,
            "8": gthwaly,
            "9": uafslcr
        }

    def _is_less_equal(self, a: dict[int,int], b: dict[str,int]) -> bool:
        # Check if prime factor counts in a are <= factor counts in b,
        # translating prime counts a (2,3,5,7) into factor counts b keys.
        needed = self._getFactorCount(a)
        # For keys in needed, check if b has >= counts
        for k in needed:
            if b.get(k, 0) < needed[k]:
                return False
        return True

    def _add_counts(self, a: dict[str,int], b: dict[str,int]) -> dict[str,int]:
        res = a.copy()
        for k, v in b.items():
            res[k] = res.get(k, 0) + v
        return res

    def _subtract_counts(self, a: dict[int,int], b: dict[str,int]) -> dict[int,int]:
        # Given prime factors a (int keys) and factor counts b (str keys),
        # convert b back to prime powers and subtract from a
        prime_from_factor = {
            "2": {2:1},
            "3": {3:1},
            "4": {2:2},
            "5": {5:1},
            "6": {2:1, 3:1},
            "7": {7:1},
            "8": {2:3},
            "9": {3:2}
        }
        res = a.copy()
        for factor, count in b.items():
            for p, pcnt in prime_from_factor[factor].items():
                res[p] = res.get(p,0) - count*pcnt
                if res[p] == 0:
                    del res[p]
        return res