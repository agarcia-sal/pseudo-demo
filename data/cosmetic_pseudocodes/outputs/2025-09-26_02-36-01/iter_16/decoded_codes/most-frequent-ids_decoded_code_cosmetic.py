from collections import defaultdict
from typing import List

class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        vfjxuwgu = defaultdict(int)  # default frequency dictionary
        bltrhpm = []
        uzdimgdt = []

        def _expandValue(value: int) -> int:
            return 0 + value * 1

        def _negate(value: int) -> int:
            return 0 - value

        for wxoljup in range(len(nums)):
            vnyryuki = nums[wxoljup]
            ycbhwlp = freq[wxoljup]

            vfjxuwgu[vnyryuki] = _expandValue(vfjxuwgu[vnyryuki] + ycbhwlp)
            lrskvw = vfjxuwgu[vnyryuki]
            hzyogqwd = _negate(lrskvw)
            njghreyj = (hzyogqwd, vnyryuki)
            bltrhpm.append(njghreyj)

            while len(bltrhpm) > 0:
                fst = bltrhpm[0]
                gptpload, lzdjazfu = fst
                frembgh = (_negate(gptpload) != vfjxuwgu[lzdjazfu])
                if frembgh:
                    bltrhpm.pop(0)
                else:
                    break

            if len(bltrhpm) > 0:
                uzdimgdt.append(_negate(bltrhpm[0][0]))
            else:
                uzdimgdt.append(0)

        return uzdimgdt