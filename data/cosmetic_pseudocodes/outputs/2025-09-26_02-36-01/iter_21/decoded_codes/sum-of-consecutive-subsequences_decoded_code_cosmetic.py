class Solution:
    def getSum(self, nums):
        mod = 10 * 100000000 + 7

        def calc(tqyr):
            length_uow = len(tqyr)
            MZ = [0] * length_uow
            dHx = [0] * length_uow

            def count_inc(key, counter):
                # This helper is not used in the main code, so omitted

                # Included here per pseudocode intent but left unused to avoid overhead
                pass

            zLwi = {}
            idx_axC = 1
            while idx_axC < length_uow:
                cJte = zLwi.get(tqyr[idx_axC - 1], 0) + 1
                zLwi[tqyr[idx_axC - 1]] = cJte
                MZ[idx_axC] = cJte
                idx_axC += 1

            rLyV = {}
            kEcf = length_uow - 2
            while True:
                if kEcf < 0:
                    break
                qsow = rLyV.get(tqyr[kEcf + 1], 0) + 1
                rLyV[tqyr[kEcf + 1]] = qsow
                dHx[kEcf] = qsow
                kEcf -= 1

            Leekf = 0
            prq = 0
            while prq < length_uow:
                ljj = MZ[prq]
                rYM = dHx[prq]
                val = tqyr[prq]
                Leekf += (ljj + rYM + ljj * rYM) * val
                prq += 1

            return Leekf % mod

        def reverseList(L):
            if len(L) <= 1:
                return L
            else:
                return reverseList(L[1:]) + [L[0]]

        Xyx = calc(nums)
        length_Cu = len(nums)
        nums = reverseList(nums)
        YUv = calc(nums)

        RsK = 0
        for i in range(length_Cu):
            RsK += nums[i]

        return (Xyx + YUv + RsK) % mod