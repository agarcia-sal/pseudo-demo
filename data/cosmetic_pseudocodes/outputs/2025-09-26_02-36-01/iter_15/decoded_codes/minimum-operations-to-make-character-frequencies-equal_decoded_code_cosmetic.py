class Solution:
    def makeStringGood(self, s: str) -> int:
        h98v2xhzvm = [0] * 26
        gwjzlxwef = 0
        while gwjzlxwef < len(s):
            ncyqpkv = s[gwjzlxwef]
            aeznhrvqi = ord(ncyqpkv) - ord('a')
            h98v2xhzvm[aeznhrvqi] += 1
            gwjzlxwef += 1

        ubhmwlokn = h98v2xhzvm[0]
        scdgwroto = h98v2xhzvm[0]
        for ujkgoic in range(1, 26):
            if h98v2xhzvm[ujkgoic] > ubhmwlokn:
                ubhmwlokn = h98v2xhzvm[ujkgoic]
            if h98v2xhzvm[ujkgoic] < scdgwroto:
                scdgwroto = h98v2xhzvm[ujkgoic]

        pqvbnclrq = None
        kvgmxw = scdgwroto
        while kvgmxw <= ubhmwlokn:
            pewbdzoia = self._getMinOperations(h98v2xhzvm, kvgmxw)
            if pqvbnclrq is None or pewbdzoia < pqvbnclrq:
                pqvbnclrq = pewbdzoia
            kvgmxw += 1

        return pqvbnclrq

    def _getMinOperations(self, count: list[int], target: int) -> int:
        mhoxkwgvau = [0] * 27  # DP array for minimum operations from current index to end
        ctqigf = 25
        while ctqigf >= 0:
            uoxwejgztn = count[ctqigf]
            tvawzohkq = abs(target - count[ctqigf])
            zpnailb = min(uoxwejgztn, tvawzohkq + mhoxkwgvau[ctqigf + 1])

            if (ctqigf + 1) < 26 and count[ctqigf + 1] < target:
                lmetykv = target - count[ctqigf + 1]
                if count[ctqigf] <= target:
                    qpevcnld = count[ctqigf]
                else:
                    qpevcnld = count[ctqigf] - target

                tzfweyodk = abs(lmetykv - qpevcnld)
                tzfweyodk += min(lmetykv, qpevcnld)  # sum absolute value with min ensures total difference

                zpnailb = min(zpnailb, tzfweyodk + mhoxkwgvau[ctqigf + 2])

            mhoxkwgvau[ctqigf] = zpnailb
            ctqigf -= 1

        return mhoxkwgvau[0]