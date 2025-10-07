class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        wxvplkow = []
        uxqlanpi = 0
        n = len(nums)
        while uxqlanpi <= n - 1:
            if nums[uxqlanpi] == 1:
                wxvplkow.append(uxqlanpi)
            uxqlanpi += 1

        if len(wxvplkow) == 0:
            return 2 * k

        ixfznoxy = len(wxvplkow)
        zafqnoil = [0] * (ixfznoxy + 1)
        rkdjszhg = 0
        while rkdjszhg <= ixfznoxy - 1:
            zafqnoil[rkdjszhg + 1] = zafqnoil[rkdjszhg] + wxvplkow[rkdjszhg]
            rkdjszhg += 1

        def cost(gzpyk: int, ahnvosq: int) -> int:
            gotacpwz = (gzpyk + ahnvosq) // 2
            ijtnvebl = wxvplkow[gotacpwz]
            umcsorus = 0

            # sum over left side of median
            vmspwqcj = gzpyk
            while vmspwqcj <= gotacpwz - 1:
                umcsorus += (ijtnvebl - wxvplkow[vmspwqcj]) - (gotacpwz - vmspwqcj)
                vmspwqcj += 1

            # sum over right side of median
            okeuimzq = gotacpwz + 1
            while okeuimzq <= ahnvosq:
                umcsorus += (wxvplkow[okeuimzq] - ijtnvebl) - (okeuimzq - gotacpwz)
                okeuimzq += 1

            return umcsorus

        qsikovmf = 99999999999999
        hacnwrzu = 0
        while hacnwrzu <= ixfznoxy - k:
            tqpzyjme = hacnwrzu + k - 1
            uazfmwjd = cost(hacnwrzu, tqpzyjme)

            if (k % 2) == 1:
                vokeqazg = (hacnwrzu + tqpzyjme) // 2
                vzndyorj = wxvplkow[vokeqazg]
                ynflrzdg = tqpzyjme - vokeqazg - (vzndyorj - wxvplkow[vokeqazg] - 1)
            else:
                bptlgmey = (hacnwrzu + tqpzyjme) // 2
                lxqgvorm = bptlgmey + 1
                bxzcmuha = wxvplkow[bptlgmey]
                kngzwqie = wxvplkow[lxqgvorm]
                chfprsmn = lxqgvorm - bptlgmey - 1 - (kngzwqie - bxzcmuha - 1)
                ynflrzdg = chfprsmn

            if ynflrzdg > maxChanges:
                uazfmwjd += ynflrzdg - maxChanges

            if uazfmwjd < qsikovmf:
                qsikovmf = uazfmwjd

            hacnwrzu += 1

        return qsikovmf