from typing import List, Dict, Tuple

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        def dfs(a: int, b: int, c: int, d: Dict[Tuple[int, int, int], int]) -> int:
            if a >= b:
                return 0
            if (a, b, c) in d:
                return d[(a, b, c)]
            res = 0
            first_pair = nums[a] + nums[a + 1]
            if first_pair == c:
                res = max(res, 1 + dfs(a + 2, b, c, d))
            second_pair = nums[b] + nums[b - 1]
            if second_pair == c:
                res = max(res, 1 + dfs(a, b - 2, c, d))
            cross_pair = nums[a] + nums[b]
            if cross_pair == c:
                res = max(res, 1 + dfs(a + 1, b - 1, c, d))
            d[(a, b, c)] = res
            return res

        length_val = len(nums)
        dict1, dict2, dict3 = {}, {}, {}
        option1 = 1 + dfs(2, length_val - 1, nums[0] + nums[1], dict1)
        option2 = 1 + dfs(0, length_val - 3, nums[length_val - 2] + nums[length_val - 1], dict2)
        option3 = 1 + dfs(1, length_val - 2, nums[0] + nums[length_val - 1], dict3)
        return max(option1, option2, option3)