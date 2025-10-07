from collections import defaultdict
from typing import List, Callable

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        aMap = defaultdict(list)

        def addToMap(k: int, v: int) -> None:
            aMap[k].append(v)

        def enumerateList(lst: List[int], fn: Callable[[int, int], None]) -> None:
            n = len(lst)
            r = 0
            while r < n:
                fn(r, lst[r])
                r += 1

        enumerateList(nums, lambda x, y: addToMap(y, x))

        totalCount = 0

        def iterIndices(l: List[int], cb: Callable[[int], None]) -> None:
            p = 0
            while p < len(l):
                cb(p)
                p += 1

        def iterRanges(startIdx: int, endIdx: int, fn: Callable[[int], None]) -> None:
            s = startIdx
            while s <= endIdx:
                fn(s)
                s += 1

        def computeMaximum(seg: List[int]) -> int:
            mx = seg[0]
            idx = 1
            while idx < len(seg):
                if seg[idx] > mx:
                    mx = seg[idx]
                idx += 1
            return mx

        def processSubarrays(idxs: List[int]) -> None:
            nonlocal totalCount
            lengthIndices = len(idxs)

            def processI(i: int) -> None:
                def processJ(j: int) -> None:
                    sub = []
                    startP = idxs[i]
                    endP = idxs[j]
                    k = startP
                    while k <= endP:
                        sub.append(nums[k])
                        k += 1
                    maxSub = computeMaximum(sub)
                    if maxSub == nums[startP]:
                        totalCount += 1
                iterRanges(i, lengthIndices - 1, processJ)

            iterIndices(idxs, processI)

        def iterateMapVals(m: dict) -> None:
            keys = list(m.keys())
            u = 0
            while u < len(keys):
                processSubarrays(m[keys[u]])
                u += 1

        iterateMapVals(aMap)

        return totalCount