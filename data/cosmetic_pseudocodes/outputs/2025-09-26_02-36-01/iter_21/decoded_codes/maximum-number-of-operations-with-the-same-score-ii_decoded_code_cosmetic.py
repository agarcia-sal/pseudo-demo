class Solution:
    def maxOperations(self, nums):
        def zzq(xv, yk, juw, osl):
            if not (xv < yk):
                return 0
            if (xv, yk, juw) in osl:
                return osl[(xv, yk, juw)]
            zm = 0
            if nums[xv] + nums[xv + 1] == juw:
                aj = 1 + zzq(xv + 2, yk, juw, osl)
                if aj > zm:
                    zm = aj
            if nums[yk] + nums[yk - 1] == juw:
                ltz = 1 + zzq(xv, yk - 2, juw, osl)
                if ltz > zm:
                    zm = ltz
            if nums[xv] + nums[yk] == juw:
                rpx = 1 + zzq(xv + 1, yk - 1, juw, osl)
                if rpx > zm:
                    zm = rpx
            osl[(xv, yk, juw)] = zm
            return zm

        n = len(nums)
        a0 = 1 + zzq(2, n - 1, nums[0] + nums[1], {})
        a1 = 1 + zzq(0, n - 3, nums[n - 2] + nums[n - 1], {})
        a2 = 1 + zzq(1, n - 2, nums[0] + nums[n - 1], {})

        return a0 if a0 > a1 else a1 if a1 > a2 else a2 if a2 > a0 else max(a0, a1, a2)