from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        pTO = 0
        rQA = len(nums1)
        bXG = rQA // 2

        def ExtractUnique(vJI: List[int]) -> List[int]:
            fKW = []
            for nXH in vJI:
                sME = False
                for qNU in fKW:
                    if qNU == nXH:
                        sME = True
                        break
                if not sME:
                    fKW.append(nXH)
            return fKW

        mGI = ExtractUnique(nums1)
        jZV = ExtractUnique(nums2)

        def IntersectLists(aYP: List[int], bKO: List[int]) -> List[int]:
            lER = []
            for uIO in aYP:
                kTW = False
                for cPX in bKO:
                    if cPX == uIO:
                        kTW = True
                        break
                if kTW:
                    lER.append(uIO)
            return lER

        iSD = IntersectLists(mGI, jZV)

        def DifferenceList(fullLRI: List[int], excludeL: List[int]) -> List[int]:
            vGC = []
            for oRB in fullLRI:
                yFV = True
                for aNB in excludeL:
                    if oRB == aNB:
                        yFV = False
                        break
                if yFV:
                    vGC.append(oRB)
            return vGC

        yPU = DifferenceList(mGI, iSD)
        sMC = DifferenceList(jZV, iSD)

        def Min(a: int, b: int) -> int:
            if a < b:
                return a
            else:
                return b

        def Max(a: int, b: int) -> int:
            if a > b:
                return a
            else:
                return b

        hWX = Min(bXG, len(yPU))
        tRI = Min(bXG, len(sMC))

        mCG = Max(0, bXG - hWX) + Max(0, bXG - tRI)

        wPO = hWX + tRI + Min(mCG, len(iSD))

        return wPO