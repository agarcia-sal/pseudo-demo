from typing import List

class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        tcmvkqxw = 0
        vdhzsynf = len(nums)
        qbjumaov = target[0]
        veoylgpm = nums[0]
        tcmvkqxw = abs(qbjumaov - veoylgpm)
        wzofsrdc = 1
        while wzofsrdc <= vdhzsynf - 1:
            kjucltoz = target[wzofsrdc]
            cpeadwny = nums[wzofsrdc]
            zgbforwe = target[wzofsrdc - 1]
            mgetlnhz = nums[wzofsrdc - 1]
            dwymcrht = kjucltoz - cpeadwny
            qtezfsby = zgbforwe - mgetlnhz
            if not (dwymcrht * qtezfsby <= 0):
                yfnodrcs = abs(dwymcrht) - abs(qtezfsby)
                if 0 < yfnodrcs:
                    tcmvkqxw += yfnodrcs
            else:
                tcmvkqxw += abs(dwymcrht)
            wzofsrdc += 1
        return tcmvkqxw