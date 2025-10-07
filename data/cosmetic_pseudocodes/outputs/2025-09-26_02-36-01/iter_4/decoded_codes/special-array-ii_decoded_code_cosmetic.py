from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        parity = []
        for num in nums:
            parity.append(num % 2)

        prefix_special = [0] * len(nums)
        for pos in range(1, len(nums)):
            if parity[pos] == parity[pos - 1]:
                prefix_special[pos] = prefix_special[pos - 1] + 1
            else:
                prefix_special[pos] = prefix_special[pos - 1]

        results = []
        for start_pos, end_pos in queries:
            if start_pos == end_pos:
                results.append(True)
            else:
                value_start = prefix_special[start_pos] if start_pos > 0 else 0
                diff_val = prefix_special[end_pos] - value_start
                results.append(diff_val == 0)

        return results