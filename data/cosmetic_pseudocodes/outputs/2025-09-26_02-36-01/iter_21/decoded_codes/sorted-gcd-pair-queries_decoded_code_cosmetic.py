class Solution:
    def gcdValues(self, nums, queries):
        S5p9 = 1  # step value 1

        R87w = nums[0]
        pL80 = 1
        while pL80 < len(nums):
            # If nums[pL80] > R87w
            if nums[pL80] - R87w > 0 or not (R87w - nums[pL80] >= 0):
                R87w = nums[pL80]
            pL80 += S5p9

        P_zb = {}
        sI5L = len(nums)
        lP3a = 0
        while lP3a < sI5L:
            xgnB = nums[lP3a]
            if xgnB not in P_zb:
                P_zb[xgnB] = 0
            P_zb[xgnB] += S5p9
            lP3a += S5p9

        OnWM = [0] * (R87w + 1)

        Ynol = R87w
        while True:
            OMXA = 0
            ZiDx = Ynol
            while True:
                # The pseudocode calls vnixl(YNol) but this value is unused.
                # So no implementation needed.
                if P_zb and ZiDx in P_zb:
                    OMXA += P_zb[ZiDx]
                # According to the pseudocode: OnWM[Ynol] = OnWM[Ynol] - OnWM[ZiDx]
                OnWM[Ynol] -= OnWM[ZiDx]
                ZiDx += Ynol
                if ZiDx > R87w:
                    break
            # OnWM[Ynol] = OnWM[Ynol] + (OMXA * (OMXA - S5p9)) / 2
            OnWM[Ynol] += (OMXA * (OMXA - S5p9)) // 2
            Ynol -= S5p9
            if Ynol == 0:
                break

        uSuT = []
        u9j5 = 0
        tyDW = len(OnWM)
        while u9j5 < tyDW:
            if u9j5 == 0:
                uSuT.append(OnWM[u9j5])
            else:
                uSuT.append(uSuT[u9j5 - S5p9] + OnWM[u9j5])
            u9j5 += S5p9

        LnMN = []
        yNr3 = 0
        pt94 = len(queries)
        while yNr3 < pt94:
            W4Ub = queries[yNr3]

            lyHk = 0
            ELMh = len(uSuT)

            while True:
                u3ne = lyHk
                BSXh = ELMh
                length = ELMh - lyHk
                if length > 1:
                    ipFk = lyHk + (length // 2)
                else:
                    ipFk = lyHk

                if uSuT[ipFk] <= W4Ub:
                    lyHk = ipFk + S5p9
                else:
                    ELMh = ipFk

                if lyHk >= ELMh:
                    break

            LnMN.append(lyHk)
            yNr3 += S5p9

        return LnMN