from typing import List, Tuple

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[Tuple[int, int]]) -> List[bool]:
        parity = [num % 2 for num in nums]

        prefix_special = [0] * len(nums)
        for i in range(1, len(nums)):
            if parity[i] != parity[i - 1]:
                prefix_special[i] = prefix_special[i - 1]
            else:
                prefix_special[i] = prefix_special[i - 1] + 1

        result = []
        for start, end in queries:
            if start == end:
                result.append(True)
            else:
                diff = prefix_special[end] - (prefix_special[start] if start > 0 else 0)
                result.append(diff == 0)

        return result