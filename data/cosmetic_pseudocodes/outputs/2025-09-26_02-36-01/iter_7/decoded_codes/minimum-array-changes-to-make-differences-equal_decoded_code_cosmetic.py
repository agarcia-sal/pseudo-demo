from typing import List

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        length = len(nums)
        half_cnt = (length // 2) - 1
        arr_size = k + 2
        counts = [0] * arr_size

        cursor = 0
        while cursor <= half_cnt:
            first_val = nums[cursor]
            second_val = nums[length - cursor - 1]

            if first_val > second_val:
                first_val, second_val = second_val, first_val

            counts[0] += 1
            diff = second_val - first_val
            counts[diff] -= 1
            counts[diff + 1] += 1

            M = max(second_val, k - first_val)
            counts[M + 1] -= 1
            counts[M + 2] += 1

            cursor += 1

        result = counts[0]
        for position in range(1, len(counts)):
            counts[position] += counts[position - 1]
            if counts[position] < result:
                result = counts[position]

        return result