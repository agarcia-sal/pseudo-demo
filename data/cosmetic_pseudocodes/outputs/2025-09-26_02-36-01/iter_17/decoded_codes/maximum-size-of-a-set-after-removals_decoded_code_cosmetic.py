from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        xAyz = len(nums1)
        pOqi = xAyz // 2

        dLve = set(nums1)
        yupu = set(nums2)

        qvMw = dLve & yupu
        kXsn = dLve - qvMw
        bLtw = yupu - qvMw

        tHzg = pOqi if pOqi < len(kXsn) else len(kXsn)
        rZvQ = pOqi if pOqi < len(bLtw) else len(bLtw)

        wEfi = pOqi - tHzg
        if wEfi < 0:
            wEfi = 0

        vMnr = pOqi - rZvQ
        if vMnr < 0:
            vMnr = 0

        wEfi += vMnr

        if wEfi >= len(qvMw):
            wEfi = len(qvMw)

        return tHzg + rZvQ + wEfi