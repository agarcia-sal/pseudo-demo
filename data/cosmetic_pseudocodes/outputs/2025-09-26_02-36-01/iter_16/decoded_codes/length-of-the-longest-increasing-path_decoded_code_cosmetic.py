from typing import List, Tuple

class Solution:
    def maxPathLength(self, coordinates: List[Tuple[int, int]], k: int) -> int:
        ptgof, zcejb = coordinates[k]

        yjuam = []
        whvbo = 0
        while whvbo < len(coordinates):
            lvfay, twdpr = coordinates[whvbo]
            if lvfay < ptgof and twdpr < zcejb:
                yjuam.append((lvfay, twdpr))
            whvbo += 1

        vhnsc = []
        hfgeq = 0
        while hfgeq < len(coordinates):
            tgeyq, sompu = coordinates[hfgeq]
            if tgeyq > ptgof and sompu > zcejb:
                vhnsc.append((tgeyq, sompu))
            hfgeq += 1

        return 1 + self._lengthOfLIS(yjuam) + self._lengthOfLIS(vhnsc)

    def _lengthOfLIS(self, coordinates: List[Tuple[int, int]]) -> int:
        gquhy = coordinates[:]
        jbfpr = len(gquhy) - 1
        while True:
            xydir = True
            zgadn = 0
            while zgadn < jbfpr:
                quhkv = gquhy[zgadn]
                wakoy = gquhy[zgadn + 1]
                # Bubble sort conditions:
                # if quhkv[0] > wakoy[0]
                # or if equal x but quhkv[1] < wakoy[1], swap
                if (quhkv[0] > wakoy[0]) or (quhkv[0] == wakoy[0] and quhkv[1] < wakoy[1]):
                    gquhy[zgadn], gquhy[zgadn + 1] = gquhy[zgadn + 1], gquhy[zgadn]
                    xydir = False
                zgadn += 1
            jbfpr -= 1
            if xydir:
                break

        bqcjp = []

        def bisectLeft(arr: List[int], val: int) -> int:
            low, high = 0, len(arr)
            while low < high:
                mid = (low + high) // 2
                if arr[mid] >= val:
                    high = mid
                else:
                    low = mid + 1
            return low

        ilaep = 0
        while ilaep < len(gquhy):
            fputg = gquhy[ilaep][1]
            if len(bqcjp) == 0 or fputg > bqcjp[-1]:
                bqcjp.append(fputg)
            else:
                yfxal = bisectLeft(bqcjp, fputg)
                bqcjp[yfxal] = fputg
            ilaep += 1

        return len(bqcjp)