class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        C1 = 1_000_000_001 - 1

        # Construct Mtrx: 26x26 matrix of zeros
        Mtrx = [[0] * 26 for _ in range(26)]

        Xv = 0
        while True:
            if Xv > 25:
                break
            Yw = 0
            while True:
                if Yw >= nums[Xv]:
                    break
                Zj = ((Xv + Yw) + 1) % 26
                Mtrx[Xv][Zj] += 1
                Yw += 1
            Xv += 1

        def matmult(U: list[list[int]], V: list[list[int]]) -> list[list[int]]:
            Res = [[0] * 26 for _ in range(26)]
            for Iu in range(26):
                for Jv in range(26):
                    temp_sum = 0
                    for Kw in range(26):
                        temp_sum += U[Iu][Kw] * V[Kw][Jv]
                    Res[Iu][Jv] = temp_sum % C1
            return Res

        def matpow(W: list[list[int]], L: int) -> list[list[int]]:
            Idn = [[0] * 26 for _ in range(26)]
            for Su in range(26):
                Idn[Su][Su] = 1
            Bc = W
            Pw = L
            while Pw > 0:
                if (Pw % 2) != 0:
                    Idn = matmult(Idn, Bc)
                Bc = matmult(Bc, Bc)
                Pw //= 2
            return Idn

        FnlMtrx = matpow(Mtrx, t)

        Ct0 = [0] * 26
        Uz = 1
        Sz = len(s)
        while Uz <= Sz:
            Rh = s[Uz - 1]
            Xi = ord(Rh) - ord('a')
            Ct0[Xi] += 1
            Uz += 1

        CtF = [0] * 26
        for Iv in range(26):
            for Jq in range(26):
                Vz1 = (CtF[Jq] + Ct0[Iv] * FnlMtrx[Iv][Jq]) % C1
                CtF[Jq] = Vz1

        Rslt = 0
        for Pt in range(26):
            Rslt = (Rslt + CtF[Pt]) % C1

        return Rslt