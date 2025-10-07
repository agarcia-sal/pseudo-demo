class Solution:
    def minimumValueSum(self, nums, andValues):
        from math import inf
        length_nums = len(nums)
        length_and = len(andValues)

        from functools import lru_cache

        @lru_cache(None)
        def dp(index_nums, index_and):
            if index_and < 0:
                return 0 if index_nums < 0 else inf
            if index_nums < 0:
                return inf

            minimal_sum = inf
            accumulated_and = None

            for pos in range(index_nums, -1, -1):
                if accumulated_and is None:
                    accumulated_and = nums[pos]
                else:
                    accumulated_and &= nums[pos]

                if accumulated_and == andValues[index_and]:
                    candidate_sum = dp(pos - 1, index_and - 1) + nums[index_nums]
                    if candidate_sum < minimal_sum:
                        minimal_sum = candidate_sum

            return minimal_sum

        answer = dp(length_nums - 1, length_and - 1)
        return answer if answer != inf else -1