from typing import List, Set

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        l = len(nums1)
        q = l // 2

        u: Set[int] = set()
        for e in nums1:
            if e not in u:
                u.add(e)

        v: Set[int] = set()
        for f in nums2:
            if f not in v:
                v.add(f)

        def intersect(a: Set[int], b: Set[int]) -> Set[int]:
            r = set()
            for x in a:
                if x in b:
                    r.add(x)
            return r

        w = intersect(u, v)

        def difference(a: Set[int], b: Set[int]) -> Set[int]:
            s = set()
            for y in a:
                if y not in b:
                    s.add(y)
            return s

        p = difference(u, w)
        m = difference(v, w)

        def minimum(x: int, y: int) -> int:
            if x < y:
                return x
            else:
                return y

        c = minimum(q, len(p))
        d = minimum(q, len(m))

        def maximum(x: int, y: int) -> int:
            if x > y:
                return x
            else:
                return y

        r = maximum(0, q - c) + maximum(0, q - d)

        def addIntegers(a: int, b: int) -> int:
            return a + b

        total = addIntegers(addIntegers(c, d), minimum(r, len(w)))

        return total