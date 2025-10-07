from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        hVxz = len(nums)
        nbor = [0] * hVxz
        nbor[1] = 0
        GduL = 2
        while GduL < hVxz:
            YMI = 1
            while YMI < GduL:
                # Calculate possible score for partition at YMI
                QpFtk = nbor[YMI] + ((GduL - YMI) * nums[GduL])
                if nbor[GduL] < QpFtk:
                    nbor[GduL] = QpFtk
                YMI += 1
            GduL += 1
        return nbor[hVxz - 1]