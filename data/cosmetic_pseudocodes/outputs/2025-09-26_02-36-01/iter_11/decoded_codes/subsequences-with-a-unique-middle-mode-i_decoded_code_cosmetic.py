from collections import Counter
from typing import List

class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        ALPHA = 10**9 + 7
        BETA = len(nums)
        if BETA < 5:
            return 0

        def generateCombinations(arr: List[int], k: int) -> List[List[int]]:
            res = []

            def innerComb(idx: int, path: List[int]) -> None:
                if len(path) == k:
                    res.append(path)
                    return
                if idx >= len(arr):
                    return
                innerComb(idx + 1, path)
                innerComb(idx + 1, path + [arr[idx]])

            innerComb(0, [])
            return res

        GAMMA = generateCombinations(nums, 5)
        DELTA = 0

        def freqCount(lst: List[int]) -> Counter:
            # Using Counter for frequency counting
            return Counter(lst)

        for OMEGA in GAMMA:
            PHI = freqCount(OMEGA)
            MIDDLE_IDX = 2
            MIDDLE_VAL = OMEGA[MIDDLE_IDX]
            MIDDLE_FREQ = PHI[MIDDLE_VAL]
            UNIQUE_MODE_FLAG = True

            KEYS = list(PHI.keys())
            for KEY_VAL in KEYS:
                CNT_VAL = PHI[KEY_VAL]
                if KEY_VAL != MIDDLE_VAL and CNT_VAL >= MIDDLE_FREQ:
                    UNIQUE_MODE_FLAG = False
                    break

            if UNIQUE_MODE_FLAG:
                DELTA += 1

        return DELTA % ALPHA