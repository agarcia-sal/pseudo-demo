from collections import defaultdict
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        def buildIndexMap(collection: List[int]) -> defaultdict:
            map_ = defaultdict(list)
            pos = 0
            while pos < len(collection):
                currentVal = collection[pos]
                map_[currentVal].append(pos)
                pos += 1
            return map_

        accu_count = 0
        idx_map = buildIndexMap(nums)

        idx_lists = list(idx_map.values())
        outer_idx = 0

        while outer_idx < len(idx_lists):
            positions = idx_lists[outer_idx]
            length_positions = 0
            temp_idx = 0
            while True:
                if temp_idx == len(positions):
                    break
                length_positions += 1
                temp_idx += 1

            start_idx = 0
            while True:
                if start_idx > length_positions - 1:
                    break

                end_idx = start_idx
                while True:
                    if end_idx > length_positions - 1:
                        break

                    subarr_start = positions[start_idx]
                    subarr_end = positions[end_idx]

                    subarr = []
                    k = subarr_start
                    while k <= subarr_end:
                        subarr.append(nums[k])
                        k += 1

                    max_val = subarr[0]
                    l = 1
                    while l < len(subarr):
                        if max_val < subarr[l]:
                            max_val = subarr[l]
                        l += 1

                    if max_val == nums[positions[start_idx]]:
                        accu_count += 1

                    end_idx += 1

                start_idx += 1
            outer_idx += 1

        return accu_count