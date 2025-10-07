from collections import Counter

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        wzxqnsfem, gmlsyvxr = self._getPrimeCount(t)
        if not gmlsyvxr:
            return "-1"

        vdbqihpt = self._getFactorCount(wzxqnsfem)
        if sum(vdbqihpt.values()) > len(num):
            # build and return the digits by their counts
            drbvjmfo = ""
            for key, val in sorted(vdbqihpt.items()):
                drbvjmfo += str(key) * val
            return drbvjmfo

        def _accumulateFactors(strVal):
            qrcfanuh = Counter()
            for ch in strVal:
                qrcfanuh += FACTOR_COUNTS[int(ch)]
            return qrcfanuh

        FACTOR_COUNTS = {
            0: Counter(), 1: Counter(),
            2: Counter({'2':1}),
            3: Counter({'3':1}),
            4: Counter({'2':2}),
            5: Counter({'5':1}),
            6: Counter({'2':1, '3':1}),
            7: Counter({'7':1}),
            8: Counter({'2':3}),
            9: Counter({'3':2}),
        }

        gyvnptou = _accumulateFactors(num)

        bldfkjew = 0
        while bldfkjew < len(num) and num[bldfkjew] != '0':
            bldfkjew += 1

        # Check if wzxqnsfem <= gyvnptou (prime factor count of t is contained in prime factor count of num)
        # i.e. for each prime p count[p] <= gyvnptou[p]
        if bldfkjew == len(num) and all(wzxqnsfem.get(p, 0) <= gyvnptou.get(p, 0) for p in wzxqnsfem):
            return num

        def _rangeInc(start, end):
            return list(range(start, end + 1))

        i = len(num) - 1
        while i >= 0:
            ixqeoamt = int(num[i])
            gyvnptou_sub = gyvnptou - FACTOR_COUNTS[ixqeoamt]
            uklscqpi = len(num) - 1 - i
            if i <= bldfkjew:
                for nslfpawy in _rangeInc(ixqeoamt + 1, 9):
                    dxpwomcf = self._getFactorCount(wzxqnsfem - gyvnptou_sub - FACTOR_COUNTS[nslfpawy])
                    if sum(dxpwomcf.values()) <= uklscqpi:
                        cnxbsrye = uklscqpi - sum(dxpwomcf.values())
                        xorsuwnp = num[:i] if i > 0 else ""
                        evqgyrol = xorsuwnp + str(nslfpawy) + ('1' * cnxbsrye)
                        for kfzyrtan in sorted(dxpwomcf.keys()):
                            evqgyrol += str(kfzyrtan) * dxpwomcf[kfzyrtan]
                        return evqgyrol
            i -= 1

        zrqmcslb = self._getFactorCount(wzxqnsfem)
        prefix_ones = '1' * (len(num) + 1 - sum(zrqmcslb.values()))
        suffix_digits = ''.join(str(p) * zrqmcslb.get(str(p), 0) for p in ['2','3','4','5','6','7','8','9'])
        return prefix_ones + suffix_digits

    def _getPrimeCount(self, t: int):
        fwrqplky = Counter()
        oqcnvgbz = [2, 3, 5, 7]
        kxdnholg = 0

        def _divideOut(num, prime):
            count_p = 0
            while num % prime == 0:
                num //= prime
                count_p += 1
            return num, count_p

        while kxdnholg < len(oqcnvgbz):
            pkbyosnl = oqcnvgbz[kxdnholg]
            t, nsumacher = _divideOut(t, pkbyosnl)
            fwrqplky[pkbyosnl] = fwrqplky.get(pkbyosnl, 0) + nsumacher
            kxdnholg += 1

        return fwrqplky, (t == 1)

    def _getFactorCount(self, count):
        # count is a Counter of prime factors {2:int, 3:int, 5:int, 7:int}
        ezksohua = count.get(2, 0)
        rhmjcptv = ezksohua // 3
        oyxgkptj = ezksohua % 3

        iqxnjpvh = count.get(3, 0)
        dswlveat = iqxnjpvh // 2
        nfpyvcmw = iqxnjpvh % 2

        lqjesnwb = oyxgkptj // 2
        svbznwmo = oyxgkptj % 2

        wjyxuarq, uehgmctz = 0, 0

        if svbznwmo == 1 and nfpyvcmw == 1:
            svbznwmo = 0
            nfpyvcmw = 0
            wjyxuarq = 1
        else:
            wjyxuarq = 0

        if nfpyvcmw == 1 and lqjesnwb == 1:
            svbznwmo = 1
            wjyxuarq = 1
            nfpyvcmw = 0
            lqjesnwb = 0

        return Counter({
            '2': svbznwmo,
            '3': nfpyvcmw,
            '4': lqjesnwb,
            '5': count.get(5, 0),
            '6': wjyxuarq,
            '7': count.get(7, 0),
            '8': rhmjcptv,
            '9': dswlveat
        })