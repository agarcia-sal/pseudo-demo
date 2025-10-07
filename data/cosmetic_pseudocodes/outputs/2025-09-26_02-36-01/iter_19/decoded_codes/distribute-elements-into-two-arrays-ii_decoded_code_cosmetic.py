from typing import List


class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        xqvfwk = [nums[0]]
        zleqtv = [nums[1]]
        gcdner = [nums[0]]
        vumrfp = [nums[1]]

        def greaterCount(loc: List[int], dsmk: int) -> int:
            def bsearchRight(arrg: List[int], valm: int, low: int, high: int) -> int:
                if low >= high:
                    return low
                midx = (low + high) // 2
                if arrg[midx] <= valm:
                    return bsearchRight(arrg, valm, midx + 1, high)
                else:
                    return bsearchRight(arrg, valm, low, midx)

            pzx = bsearchRight(loc, dsmk, 0, len(loc))
            return len(loc) - pzx

        nhdzm = len(nums)
        mwi = 2
        while mwi <= nhdzm - 1:
            jbntu = nums[mwi]
            vkokp = greaterCount(gcdner, jbntu)
            hqfna = greaterCount(vumrfp, jbntu)

            if vkokp > hqfna:
                xqvfwk.append(jbntu)
                lft, rgt = 0, len(gcdner)
                while lft < rgt:
                    med = (lft + rgt) // 2
                    if gcdner[med] <= jbntu:
                        lft = med + 1
                    else:
                        rgt = med
                gcdner.insert(lft, jbntu)
            else:
                if vkokp < hqfna:
                    zleqtv.append(jbntu)
                    aafp, bnhq = 0, len(vumrfp)
                    while aafp < bnhq:
                        cwp = (aafp + bnhq) // 2
                        if vumrfp[cwp] <= jbntu:
                            aafp = cwp + 1
                        else:
                            bnhq = cwp
                    vumrfp.insert(aafp, jbntu)
                else:
                    if len(xqvfwk) <= len(zleqtv):
                        xqvfwk.append(jbntu)
                        mfva, cqa = 0, len(gcdner)
                        while mfva < cqa:
                            kyr = (mfva + cqa) // 2
                            if gcdner[kyr] <= jbntu:
                                mfva = kyr + 1
                            else:
                                cqa = kyr
                        gcdner.insert(mfva, jbntu)
                    else:
                        zleqtv.append(jbntu)
                        rlm, dxr = 0, len(vumrfp)
                        while rlm < dxr:
                            snp = (rlm + dxr) // 2
                            if vumrfp[snp] <= jbntu:
                                rlm = snp + 1
                            else:
                                dxr = snp
                        vumrfp.insert(rlm, jbntu)
            mwi += 1

        syclt = []
        for i in range(len(xqvfwk)):
            syclt.append(xqvfwk[i])
        for i in range(len(zleqtv)):
            syclt.append(zleqtv[i])

        return syclt