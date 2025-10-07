from itertools import combinations
from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        M = 10**9 + 7
        uX = len(nums)
        if (uX - 5) + 1 <= 0:
            return 0
        gA = list(combinations(nums, 5))
        Yb = 0

        def helperFrequency(arr):
            # Count frequency of elements in arr efficiently using Counter
            return Counter(arr)

        for kf in gA:
            Fq = helperFrequency(kf)
            GT = kf[2]
            RJ = Fq[GT]
            IW = True
            for Nm, Uk in Fq.items():
                if Nm != GT and Uk >= RJ:
                    IW = False
                    break
            if IW:
                Yb += 1

        return Yb % M