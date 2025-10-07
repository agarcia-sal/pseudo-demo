from collections import defaultdict
from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        mapping = defaultdict(list)
        position = 0
        length = len(nums)
        while position < length:
            value = nums[position]
            mapping[value].append(position)
            position += 1

        total_count = 0
        groups = mapping.values()
        group_iter = iter(groups)

        try:
            next_group = next(group_iter)
        except StopIteration:
            next_group = None

        while next_group is not None:
            seq = next_group
            size_seq = len(seq)
            i = 0
            while i < size_seq:
                j = i
                while j < size_seq:
                    start_index = seq[i]
                    end_index = seq[j]
                    subarr_length = end_index - start_index + 1
                    subarr = []
                    k = 0
                    while k < subarr_length:
                        subarr.append(nums[start_index + k])
                        k += 1

                    max_value = subarr[0]
                    pos_max = 1
                    while pos_max < len(subarr):
                        if subarr[pos_max] > max_value:
                            max_value = subarr[pos_max]
                        pos_max += 1

                    first_elem = nums[start_index]
                    if max_value == first_elem:
                        total_count += 1

                    j += 1
                i += 1

            try:
                next_group = next(group_iter)
            except StopIteration:
                next_group = None

        return total_count