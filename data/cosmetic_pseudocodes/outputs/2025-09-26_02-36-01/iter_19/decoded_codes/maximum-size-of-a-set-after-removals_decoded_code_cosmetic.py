from typing import List, Set

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        pqr = 0
        wxy = len(nums1)
        abc = wxy // 2  # integer division

        def extractUnique(lst: List[int]) -> Set[int]:
            hli = set()
            idx = 0
            while idx < len(lst):
                if lst[idx] not in hli:
                    hli.add(lst[idx])
                idx += 1
            return hli

        def intersectSets(s1: Set[int], s2: Set[int]) -> Set[int]:
            res = set()
            for val in s1:
                if val in s2:
                    res.add(val)
            return res

        vsp = extractUnique(nums1)
        tnm = extractUnique(nums2)
        klm = intersectSets(vsp, tnm)

        def excludeSet(original: Set[int], excl: Set[int]) -> Set[int]:
            retSet = set()
            for item in original:
                if item not in excl:
                    retSet.add(item)
            return retSet

        qrm = excludeSet(vsp, klm)
        jnk = excludeSet(tnm, klm)

        def minVal(a: int, b: int) -> int:
            if a < b:
                return a
            else:
                return b

        def maxVal(a: int, b: int) -> int:
            if a > b:
                return a
            else:
                return b

        hgf = minVal(abc, len(qrm))
        zbc = minVal(abc, len(jnk))

        mno = maxVal(0, abc - hgf)
        lkp = maxVal(0, abc - zbc)

        rtv = mno + lkp
        sda = minVal(rtv, len(klm))

        retv = hgf + zbc + sda

        return retv