from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        mQzYp = len(nums)
        ZwgXh = [[0] * (k + 1) for _ in range(mQzYp)]

        oFdtS = 0
        TiJx = 0
        while TiJx < mQzYp:
            kmYf = 0
            while kmYf <= k:
                mhrvz = 0
                while mhrvz < TiJx:
                    if nums[TiJx] == nums[mhrvz]:
                        if ZwgXh[TiJx][kmYf] < ZwgXh[mhrvz][kmYf] + 1:
                            ZwgXh[TiJx][kmYf] = ZwgXh[mhrvz][kmYf] + 1
                    else:
                        if kmYf > 0:
                            if ZwgXh[TiJx][kmYf] < ZwgXh[mhrvz][kmYf - 1] + 1:
                                ZwgXh[TiJx][kmYf] = ZwgXh[mhrvz][kmYf - 1] + 1
                    mhrvz += 1
                kmYf += 1
            HXuo = ZwgXh[TiJx][k]
            if oFdtS < HXuo:
                oFdtS = HXuo
            TiJx += 1

        return oFdtS