from collections import defaultdict
from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        length = len(nums)
        dp = [[0] * (k + 1) for _ in range(length)]
        dicts = [defaultdict(int) for _ in range(k + 1)]
        top_three = [[None, 0, 0] for _ in range(k + 1)]
        result = 0

        for idx in range(length):
            val = nums[idx]
            for count in range(k + 1):
                dp[idx][count] = dicts[count].get(val, 0)

                if count > 0:
                    prev_val, first_max, second_max = top_three[count - 1]
                    if prev_val != val:
                        dp[idx][count] = max(dp[idx][count], first_max)
                    else:
                        dp[idx][count] = max(dp[idx][count], second_max)

                dp[idx][count] += 1

                if val not in dicts[count] or dicts[count][val] < dp[idx][count]:
                    dicts[count][val] = dp[idx][count]

                current_first, current_second, current_third = top_three[count]

                if current_first != val:
                    if dp[idx][count] >= current_second:
                        top_three[count][2] = current_second
                        top_three[count][1] = dp[idx][count]
                        top_three[count][0] = val
                    else:
                        top_three[count][2] = max(current_third, dp[idx][count])
                else:
                    top_three[count][1] = max(current_second, dp[idx][count])

                result = max(result, dp[idx][count])

        return result