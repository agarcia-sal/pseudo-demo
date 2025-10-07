class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        MOD = 10**9 + 7

        wJZKlOSb = (n * n) * ((m**3) - m) // 6
        VSoBzxir = (m * m) * ((n**3) - n) // 6

        def CqReapui(a: int, b: int) -> int:
            if b == 0:
                return 1
            return (a * CqReapui(a - 1, b - 1)) // b

        RUtjnDpN = CqReapui((m * n) - 2, k - 2)
        VGUOIrzl = (wJZKlOSb + VSoBzxir) * RUtjnDpN

        # Return VGUOIrzl mod MOD
        return VGUOIrzl % MOD