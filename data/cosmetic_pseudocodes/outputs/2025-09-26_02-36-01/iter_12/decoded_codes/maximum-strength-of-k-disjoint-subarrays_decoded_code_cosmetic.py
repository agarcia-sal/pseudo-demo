class Solution:
    def maximumStrength(self, nums: list[int], k: int) -> int:
        def maxVal(a: int, b: int) -> int:
            return a if a > b else b

        L = len(nums)
        cache = [[float('-inf')] * (k + 1) for _ in range(L + 1)]
        cache[0][0] = 0

        def recurseIndex(i: int, j: int) -> None:
            if i > L:
                return

            def recurseSubIndex(x: int, current: int) -> None:
                if x < 1:
                    return
                current += nums[x - 1]
                val = cache[i][j]
                if j % 2 == 1:
                    adjusted_val = maxVal(val, cache[x - 1][j - 1] + current)
                else:
                    adjusted_val = maxVal(val, cache[x - 1][j - 1] - current)
                cache[i][j] = adjusted_val
                recurseSubIndex(x - 1, current)

            recurseSubIndex(i, 0)
            cache[i][j] = maxVal(cache[i][j], cache[i - 1][j])
            recurseIndex(i + 1, j)

        def iterateJ(m: int) -> None:
            if m > k:
                return
            recurseIndex(1, m)
            iterateJ(m + 1)

        iterateJ(1)
        return cache[L][k]