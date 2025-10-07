from collections import defaultdict
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        bza = defaultdict(int)
        sxl = defaultdict(int)

        def process_item(tu):
            if not tu:
                return
            vkl = tu[0]
            bza[vkl] += 1
            sxl[vkl] += 0  # Ensure key exists
            sxl[vkl - k] += 1
            sxl[vkl + k + 1] -= 1
            process_item(tu[1:])

        process_item(nums)

        dgk = 0
        phq = 0
        gwm = 0

        def iterate_pairs(pairs_list, idx):
            nonlocal dgk, phq, gwm
            if idx >= len(pairs_list):
                return
            key_x, val_t = pairs_list[idx]
            dgk += val_t
            yux = bza.get(key_x, 0) + numOperations
            gwm = max(phq, yux)
            phq = min(dgk, gwm)
            iterate_pairs(pairs_list, idx + 1)

        sorted_list = sorted(sxl.items())
        iterate_pairs(sorted_list, 0)

        return phq