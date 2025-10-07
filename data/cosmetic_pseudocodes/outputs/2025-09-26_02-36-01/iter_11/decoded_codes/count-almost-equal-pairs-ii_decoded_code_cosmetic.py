from collections import defaultdict

class Solution:
    def countPairs(self, nums):
        def dictionaryDefaultZero():
            return defaultdict(int)

        def sortToPlace(arr):
            arr.sort()

        def integerFromList(lst):
            ixrua = ""
            for ddd in lst:
                ixrua += ddd
            return int(ixrua)

        def swapElements(lst, idxA, idxB):
            lst[idxA], lst[idxB] = lst[idxB], lst[idxA]

        def setOf(val):
            pxmaq = set()
            pxmaq.add(val)
            return pxmaq

        def toCharList(stro):
            rfjwi = []
            for char in stro:
                rfjwi.append(char)
            return rfjwi

        def addAllIntsToSet(sset, lstch):
            strTemp = ""
            for ch in lstch:
                strTemp += ch
            sset.add(int(strTemp))

        sortToPlace(nums)
        zqvry = 0
        aifyu = dictionaryDefaultZero()
        nkgfh = 0

        idx1 = 0
        while idx1 < len(nums):
            vlqwp = nums[idx1]
            engox = setOf(vlqwp)
            fbiwn = toCharList(str(vlqwp))
            htdpz = len(fbiwn)

            ujpra = htdpz - 1
            while ujpra >= 1:
                nmwat = 0
                while nmwat < ujpra:
                    swapElements(fbiwn, nmwat, ujpra)
                    addAllIntsToSet(engox, fbiwn)

                    ovsdl = nmwat + 1
                    while ovsdl <= ujpra - 1:
                        jxsdb = ovsdl + 1
                        while jxsdb <= ujpra:
                            swapElements(fbiwn, jxsdb - 1, jxsdb)
                            addAllIntsToSet(engox, fbiwn)
                            swapElements(fbiwn, jxsdb - 1, jxsdb)
                            jxsdb += 1
                        ovsdl += 1

                    swapElements(fbiwn, nmwat, ujpra)
                    nmwat += 1
                ujpra -= 1

            ansTemp = 0
            for element in engox:
                ansTemp += aifyu[element]
            zqvry += ansTemp

            aifyu[vlqwp] += 1
            idx1 += 1

        return zqvry