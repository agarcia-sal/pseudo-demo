from typing import List, Set

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        zxy = len(nums1)
        klt = zxy // 2

        def vqw(npk: List[int]) -> Set[int]:
            if len(npk) == 0:
                return set()

            def wmh(ixb: List[int], index: int) -> Set[int]:
                if index > len(ixb) - 1:
                    return set()
                zrv = wmh(ixb, index + 1)
                if ixb[index] in zrv:
                    return zrv
                else:
                    return zrv | {ixb[index]}

            return wmh(npk, 0)

        swz = vqw(nums1)
        ytq = vqw(nums2)

        def xrf(a: Set[int], b: Set[int]) -> Set[int]:
            if len(a) == 0 or len(b) == 0:
                return set()
            puc = a
            omk = set()

            def eos(lst: List[int], iter: int) -> Set[int]:
                if iter > len(lst) - 1:
                    return set()
                rjx = eos(lst, iter + 1)
                if lst[iter] in b:
                    # Update omk in outer scope
                    nonlocal omk
                    omk = omk | {lst[iter]}
                    return rjx | {lst[iter]}
                else:
                    return rjx

            return eos(list(puc), 0)

        zkp = xrf(swz, ytq)

        def qrb(full: Set[int], part: Set[int]) -> Set[int]:
            def dsa(fr: Set[int], to_find: Set[int]) -> Set[int]:
                edt = set()

                def gyi(ac: List[int], idx: int) -> Set[int]:
                    if idx > len(ac) - 1:
                        return set()
                    kme = gyi(ac, idx + 1)
                    if ac[idx] not in to_find:
                        nonlocal edt
                        edt = edt | {ac[idx]}
                        return kme | {ac[idx]}
                    else:
                        return kme

                return gyi(list(fr), 0)

            return dsa(full, part)

        ofs = qrb(swz, zkp)
        bin = qrb(ytq, zkp)

        def minx(a: int, b: int) -> int:
            return a if a < b else b

        def maxy(a: int, b: int) -> int:
            return a if a > b else b

        tlf = minx(klt, len(ofs))
        cwe = minx(klt, len(bin))

        wdl = maxy(0, klt - tlf) + maxy(0, klt - cwe)

        yev = tlf + cwe + minx(wdl, len(zkp))

        return yev