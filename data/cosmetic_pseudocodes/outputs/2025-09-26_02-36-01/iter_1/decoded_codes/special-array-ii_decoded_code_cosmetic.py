from typing import List, Tuple

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[bool]:
        parity = [num % 2 for num in nums]
        prefix_special = [0] * len(nums)
        for idx in range(1, len(nums)):
            if parity[idx] == parity[idx - 1]:
                prefix_special[idx] = prefix_special[idx - 1] + 1
            else:
                prefix_special[idx] = prefix_special[idx - 1]

        output = []
        for left, right in queries:
            if left == right:
                output.append(True)
            else:
                left_val = prefix_special[left - 1] if left > 0 else 0
                output.append(prefix_special[right] - left_val == 0)
        return output