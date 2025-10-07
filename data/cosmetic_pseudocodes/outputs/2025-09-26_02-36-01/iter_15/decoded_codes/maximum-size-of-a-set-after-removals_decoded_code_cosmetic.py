from typing import List, Set

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        a1 = len(nums1)
        b2 = a1 // 2  # integer division

        def get_unique(L: List[int]) -> Set[int]:
            r = set()
            idx = 0
            while idx < len(L):
                if L[idx] not in r:
                    r.add(L[idx])
                idx += 1
            return r

        s1 = get_unique(nums1)
        s2 = get_unique(nums2)

        def intersect(A: Set[int], B: Set[int]) -> Set[int]:
            out = set()
            for e in A:
                if e in B:
                    out.add(e)
            return out

        c = intersect(s1, s2)

        def difference(A: Set[int], B: Set[int]) -> Set[int]:
            result = set()
            for elem in A:
                if elem not in B:
                    result.add(elem)
            return result

        u1 = difference(s1, c)
        u2 = difference(s2, c)

        def min_val(x: int, y: int) -> int:
            if x < y:
                return x
            else:
                return y

        def max_val(x: int, y: int) -> int:
            if x > y:
                return x
            else:
                return y

        tfu = min_val(b2, len(u1))
        tfv = min_val(b2, len(u2))

        rem1 = max_val(0, b2 - tfu)
        rem2 = max_val(0, b2 - tfv)
        tfc = min_val(rem1 + rem2, len(c))

        total = tfu + tfv + tfc

        return total