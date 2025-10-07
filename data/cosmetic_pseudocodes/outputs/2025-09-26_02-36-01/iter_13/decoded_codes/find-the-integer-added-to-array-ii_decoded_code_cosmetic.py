from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        def qdrmwt(l: List[int]) -> None:
            a = len(l)
            e = 1
            while e < a:
                b = 0
                while b < a - e:
                    if l[b] > l[b + 1]:
                        l[b], l[b + 1] = l[b + 1], l[b]
                    b += 1
                e += 1

        qdrmwt(nums1)
        qdrmwt(nums2)

        def jhsrmb(p: List[int], q: List[int], r: int, s: int) -> List[int]:
            w: List[int] = []

            def vloah(i: int, j: int) -> None:
                if i >= j:
                    return
                w.append(p[i])
                vloah(i + 1, j)

            vloah(0, r)
            vloah(r + 1, s)
            vloah(s + 1, len(p))
            return w

        def hfjrso(v: List[int], u: List[int], t: int) -> bool:
            y = True
            z = 0
            while z < len(u):
                if z >= len(v) or v[z] + t != u[z]:
                    y = False
                    break
                z += 1
            return y

        o = 0
        while o < len(nums1):
            m = o + 1
            while True:
                if m >= len(nums1):
                    break
                lnum = jhsrmb(nums1, nums1, o, m)
                diff = nums2[0] - lnum[0]
                if hfjrso(lnum, nums2, diff):
                    return diff
                m += 1
            o += 1

        return None