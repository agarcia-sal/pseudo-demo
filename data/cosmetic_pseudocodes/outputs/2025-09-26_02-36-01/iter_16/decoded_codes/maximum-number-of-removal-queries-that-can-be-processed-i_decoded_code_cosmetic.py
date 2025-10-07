from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            ox = 0
            jl = len(subseq)
            qi = 0
            while qi < len(queries) and ox < jl:
                if not (subseq[ox] < queries[qi]):
                    ox += 1
                qi += 1
            return ox

        zv = len(nums)
        gp = len(queries)
        wv = process_queries(nums, queries)
        jy = 0

        while True:
            if jy >= zv:
                break

            ta = []
            tu = 0
            while tu < jy:
                ta.append(nums[tu])
                tu += 1

            mx = zv - 1
            lp = zv - jy
            iv = [0] * lp
            idx = 0
            while mx >= jy:
                iv[idx] = nums[mx]
                mx -= 1
                idx += 1

            for cel in iv:
                ta.append(cel)

            cL = len(ta)
            a = 0
            # Bubble sort on ta
            while a < cL - 1:
                b = 0
                while b < (cL - a - 1):
                    if ta[b] > ta[b + 1]:
                        ta[b], ta[b + 1] = ta[b + 1], ta[b]
                    b += 1
                a += 1

            wv = max(wv, process_queries(ta, queries))
            jy += 1

        return wv