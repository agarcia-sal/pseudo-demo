class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        BASE_MODULUS = 10**9 + 7
        Q = [1] * n

        def iterateIndex(pos: int):
            if pos >= n:
                return
            Q[pos] = (Q[pos] + Q[pos - 1]) % BASE_MODULUS
            iterateIndex(pos + 1)

        def iterateStep(count: int):
            if count == k:
                return
            iterateIndex(1)
            iterateStep(count + 1)

        iterateStep(0)
        return Q[-1]