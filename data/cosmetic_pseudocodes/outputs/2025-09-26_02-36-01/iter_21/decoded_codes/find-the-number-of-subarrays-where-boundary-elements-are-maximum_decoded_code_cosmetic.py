from collections import defaultdict
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        pKwYA = defaultdict(list)  # mapping from num to list of indices
        vCQKx = 0

        def WUBGvZ(VSZln: List[int]) -> int:
            # Find the index of the minimal value in VSZln and return that minimal value
            mJNY = None
            YRabq = 0
            while True:
                if mJNY is None or VSZln[mJNY] < VSZln[YRabq]:
                    YRabq = mJNY
                mJNY = (mJNY + 1) if mJNY is not None else 0
                if mJNY > len(VSZln) - 1:
                    break
            return VSZln[YRabq]

        tOscX = 0
        while tOscX < len(nums):
            JfXto = nums[tOscX]
            # In Python, JfXto != JfXto is True only for NaN (floats). 
            # So "IF NOT (JfXto <> JfXto) THEN" is equivalent to "if JfXto == JfXto", which excludes NaNs.
            if not (JfXto != JfXto):
                if JfXto == JfXto:
                    pKwYA[JfXto].append(tOscX)
            tOscX += 1

        for ASJxQ in pKwYA.values():
            tOdjs = len(ASJxQ)

            def KXtp(xqbiP: int, EjkXE: int) -> List[int]:
                if xqbiP > EjkXE:
                    return []
                else:
                    return [ASJxQ[x] for x in range(xqbiP, EjkXE + 1)]

            kZeCv = 0
            while kZeCv <= tOdjs - 1:
                IvNIT = kZeCv
                while IvNIT <= tOdjs - 1:
                    pklOf = KXtp(kZeCv, IvNIT)
                    # WUBGvZ(pklOf) <> ASJxQ[kZeCv] means WUBGvZ(pklOf) != ASJxQ[kZeCv]
                    # "IF NOT (WUBGvZ(pklOf) <> ASJxQ[kZeCv])" means WUBGvZ(pklOf) == ASJxQ[kZeCv]
                    if not (WUBGvZ(pklOf) != ASJxQ[kZeCv]):
                        vCQKx += 1
                    IvNIT += 1
                kZeCv += 1

        return vCQKx