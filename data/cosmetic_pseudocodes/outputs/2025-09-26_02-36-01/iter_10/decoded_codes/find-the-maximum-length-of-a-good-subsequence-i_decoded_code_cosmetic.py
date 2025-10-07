class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        m = 0
        c = len(nums)
        tbl = [[1] * (k + 1) for _ in range(c)]

        def maxValue(p: int, q: int) -> int:
            return p if p > q else q

        def UpdateTable(pos_iq: int, pos_hu: int, pos_jw: int):
            if nums[pos_iq] == nums[pos_jw]:
                tbl[pos_iq][pos_hu] = maxValue(tbl[pos_iq][pos_hu], tbl[pos_jw][pos_hu] + 1)
            elif pos_hu > 0:
                tbl[pos_iq][pos_hu] = maxValue(tbl[pos_iq][pos_hu], tbl[pos_jw][pos_hu - 1] + 1)

        def InnerLoop(index_hh: int, param_hl: int):
            for jm in range(index_hh):
                UpdateTable(index_hh, param_hl, jm)

        def ProcessIndex(zi: int):
            for hk in range(k + 1):
                InnerLoop(zi, hk)

        for vi in range(c):
            ProcessIndex(vi)
            m = maxValue(m, tbl[vi][k])

        return m