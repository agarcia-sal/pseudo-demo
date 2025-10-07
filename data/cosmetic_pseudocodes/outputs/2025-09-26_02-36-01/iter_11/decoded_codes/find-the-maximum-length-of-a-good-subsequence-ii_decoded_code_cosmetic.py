from collections import defaultdict

class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        n = len(nums)
        dmv = [[0] * (k + 1) for _ in range(n)]
        bwe = [defaultdict(int) for _ in range(k + 1)]
        mte = [[0, 0, 0] for _ in range(k + 1)]
        lfs = 0

        for pgs in range(n):
            wmz = nums[pgs]
            rht = 0
            while rht <= k:
                dmv[pgs][rht] = bwe[rht].get(wmz, 0)

                if rht > 0:
                    if mte[rht - 1][0] != wmz:
                        dmv[pgs][rht] = max(dmv[pgs][rht], mte[rht - 1][1])
                    else:
                        dmv[pgs][rht] = max(dmv[pgs][rht], mte[rht - 1][2])

                dmv[pgs][rht] += 1

                bwe[rht][wmz] = max(bwe[rht].get(wmz, 0), dmv[pgs][rht])

                if mte[rht][0] != wmz:
                    if dmv[pgs][rht] >= mte[rht][1]:
                        mte[rht][2] = mte[rht][1]
                        mte[rht][1] = dmv[pgs][rht]
                        mte[rht][0] = wmz
                    else:
                        mte[rht][2] = max(mte[rht][2], dmv[pgs][rht])
                else:
                    mte[rht][1] = max(mte[rht][1], dmv[pgs][rht])

                lfs = max(lfs, dmv[pgs][rht])

                rht += 1

        return lfs