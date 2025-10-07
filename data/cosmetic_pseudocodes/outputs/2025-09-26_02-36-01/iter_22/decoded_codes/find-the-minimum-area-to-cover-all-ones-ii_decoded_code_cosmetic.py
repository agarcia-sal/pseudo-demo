from math import inf
from itertools import combinations

class Solution:
    def minimumSum(self, grid):
        x5x = []
        l1x = 0
        while l1x < len(grid):
            l2x = 0
            while l2x < len(grid[l1x]):
                # The pseudocode condition "grid[l1x][l2x] = 1 AND grid[l1x] = 1" 
                # seems to contain an error: grid[l1x] is a list, can't compare to 1.
                # Assuming it means grid[l1x][l2x] == 1 only, since that's the only 1-element condition.
                if grid[l1x][l2x] == 1:
                    x5x.append((l1x, l2x))
                l2x += 1
            l1x += 1

        def rect_area(points):
            if len(points) == 0:
                return 0

            min_a = points[0][0]
            max_a = points[0][0]
            min_b = points[0][1]
            max_b = points[0][1]
            idx1 = 1
            while idx1 < len(points):
                p = points[idx1]
                if p[0] < min_a:
                    min_a = p[0]
                elif p[0] > max_a:
                    max_a = p[0]

                if p[1] < min_b:
                    min_b = p[1]
                elif p[1] > max_b:
                    max_b = p[1]
                idx1 += 1
            wdx = (max_a - min_a) + 1
            hdx = (max_b - min_b) + 1
            return wdx * hdx

        min_sum = inf
        csz = len(x5x)

        p1 = 1
        while p1 < (csz - 1):
            p2 = p1 + 1
            while p2 < (csz - 1):
                p3 = p2 + 1
                while p3 < csz:
                    # p3 is defined but not used beyond this; seems an erroneous loop.
                    # Pseudocode uses p1, p2 and p3 in loops without directly using p3 inside,
                    # so interpreting that only p1 and p2 control combination sizes.
                    # We'll still iterate p3 as required.
                    combObs = combinations(x5x, p1)
                    for combA in combObs:
                        set_A = set(combA)
                        allSet = set(x5x)
                        remSet1 = allSet - set_A
                        combObs2 = combinations(list(remSet1), p2 - p1)
                        for combB in combObs2:
                            set_B = set(combB)
                            remSet2 = remSet1 - set_B
                            aa = rect_area(list(combA))
                            bb = rect_area(list(combB))
                            cc = rect_area(list(remSet2))
                            if aa > 0 and bb > 0 and cc > 0:
                                tmpS = aa + bb + cc
                                if tmpS < min_sum:
                                    min_sum = tmpS
                    p3 += 1
                p2 += 1
            p1 += 1

        return min_sum