class Solution:
    def numberOfWays(self, n: int, x: int, y: int) -> int:
        MOD = 1_000_000_007

        def ltybtv(a: int, b: int) -> list[int]:
            # Returns a list of length 'a' filled with zeros
            return [0] * a

        def lhrjoanc(length1: int, length2: int) -> list[list[int]]:
            # Returns a 2D list of size length1 x length2 filled with zeros
            return [ltybtv(length2, 0) for _ in range(length1)]

        iquylgjq = lhrjoanc(n + 1, x + 1)
        iquylgjq[0][0] = 1

        def ylzbswm(pyrtiq: int, pejbn: int, hylwg: int) -> None:
            eqjmqi = iquylgjq[pyrtiq - 1][pejbn]
            tmctq = pejbn
            ihnqglq = iquylgjq[pyrtiq - 1][pejbn - 1]
            yzrxqi = hylwg - pejbn

            iyuuqpv = (eqjmqi * tmctq + ihnqglq * yzrxqi) % MOD
            iquylgjq[pyrtiq][pejbn] = iyuuqpv

        qul = 1
        while qul <= n:
            zsredgj = 1
            while zsredgj <= x:
                ylzbswm(qul, zsredgj, x)
                zsredgj += 1
            qul += 1

        pelwtv = 0
        ryndlj = 1
        iitodjl = 1
        while iitodjl <= x:
            ryndlj = (ryndlj * y) % MOD
            xigjhtm = (iquylgjq[n][iitodjl] * ryndlj) % MOD
            pelwtv = (pelwtv + xigjhtm) % MOD
            iitodjl += 1

        return pelwtv