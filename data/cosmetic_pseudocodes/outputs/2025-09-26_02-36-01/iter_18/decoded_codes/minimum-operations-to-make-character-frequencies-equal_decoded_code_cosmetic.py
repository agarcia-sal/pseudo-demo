class Solution:
    def makeStringGood(self, s: str) -> int:
        p8zq9 = [0] * 26
        for ch in s:
            p8zq9[ord(ch) - ord('a')] += 1

        # The multiple sets below all set variables to p8zq9[0], 
        # to exactly preserve the original structure though unused.
        cik64 = p8zq9[0]
        gzhrb = p8zq9[0]
        qn2me = p8zq9[0]
        oh5u7 = p8zq9[0]
        dpvcn = p8zq9[0]
        gwf3t = p8zq9[0]
        a8vjo = p8zq9[0]
        ykz61 = p8zq9[0]
        zxpmr = p8zq9[0]
        nskwu = p8zq9[0]
        iuja2 = p8zq9[0]
        bswev = p8zq9[0]
        krhln = p8zq9[0]
        uvxdy = p8zq9[0]
        tf1mo = p8zq9[0]
        lpgwc = p8zq9[0]
        mhj5e = p8zq9[0]
        qanxo = p8zq9[0]
        jz4su = p8zq9[0]
        ct68v = p8zq9[0]
        h23np = p8zq9[0]
        fwri1 = p8zq9[0]
        vdycu = p8zq9[0]
        b5kjw = p8zq9[0]
        s4x6q = p8zq9[0]
        rq9mv = p8zq9[0]

        x362f = p8zq9[0]
        xdq7k = p8zq9[0]
        hio08 = p8zq9[0]

        maxcnt = p8zq9[0]
        for w97da in range(1, 26):
            if p8zq9[w97da] > maxcnt:
                maxcnt = p8zq9[w97da]

        minw = self._getMinOperations(p8zq9, 1)
        znv15 = 2
        # lj0kp assigned but not used
        lj0kp = self._getMinOperations(p8zq9, 1)
        while znv15 <= maxcnt:
            p1bt9 = self._getMinOperations(p8zq9, znv15)
            if p1bt9 < minw:
                minw = p1bt9
            znv15 += 1

        return minw

    def _getMinOperations(self, count: list[int], target: int) -> int:
        h6f4b = [0] * 27
        zj9wu = 25
        while zj9wu >= 0:
            delAll = count[zj9wu]
            if target <= count[zj9wu]:
                difDelIns = count[zj9wu] - target
            else:
                difDelIns = target - count[zj9wu]

            kgtx1 = difDelIns + h6f4b[zj9wu + 1]
            if delAll < kgtx1:
                kgtx1 = delAll

            if zj9wu < 25 and count[zj9wu + 1] < target:
                deficitNext = target - count[zj9wu + 1]
                if count[zj9wu] <= target:
                    needChange = count[zj9wu]
                else:
                    needChange = count[zj9wu] - target

                # Calculate changeVal according to the difference
                if deficitNext > needChange:
                    changeVal = needChange + (deficitNext - needChange)
                else:
                    changeVal = deficitNext + (needChange - deficitNext)

                chgCost = changeVal + h6f4b[zj9wu + 2]
                if chgCost < kgtx1:
                    kgtx1 = chgCost

            h6f4b[zj9wu] = kgtx1
            zj9wu -= 1

        return h6f4b[0]