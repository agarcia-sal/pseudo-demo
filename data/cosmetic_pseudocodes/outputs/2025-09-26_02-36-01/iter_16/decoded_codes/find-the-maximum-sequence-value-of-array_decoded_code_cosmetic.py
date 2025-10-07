from typing import List

class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        C8u = 1 << 7  # 128
        Cdy = len(nums)
        # Initialize 3D DP array for forward pass
        r6Z = [[[False] * C8u for _ in range(k + 2)] for __ in range(Cdy + 1)]
        r6Z[0][0][0] = True

        for aDf in range(Cdy):
            for WcQ in range(k + 1):
                for GxE in range(C8u):
                    if r6Z[aDf][WcQ][GxE]:
                        # not pick nums[aDf]
                        r6Z[aDf + 1][WcQ][GxE] = True
                        # pick nums[aDf]
                        if WcQ + 1 <= k:
                            A7M = GxE | nums[aDf]
                            r6Z[aDf + 1][WcQ + 1][A7M] = True

        # Initialize 3D DP array for backward pass
        YlH = [[[False] * C8u for _ in range(k + 2)] for __ in range(Cdy + 1)]
        YlH[Cdy][0][0] = True

        for mHx in range(Cdy, 0, -1):
            for vGd in range(k + 1):
                for euE in range(C8u):
                    if YlH[mHx][vGd][euE]:
                        # not pick nums[mHx - 1]
                        YlH[mHx - 1][vGd][euE] = True
                        # pick nums[mHx - 1]
                        if vGd + 1 <= k:
                            Bzh = euE | nums[mHx - 1]
                            YlH[mHx - 1][vGd + 1][Bzh] = True

        oUW = 0
        for atO in range(k, Cdy - k + 1):
            for LKq in range(C8u):
                if r6Z[atO][k][LKq]:
                    for xkY in range(C8u):
                        if YlH[atO][k][xkY]:
                            val = LKq ^ xkY
                            if val > oUW:
                                oUW = val
        return oUW