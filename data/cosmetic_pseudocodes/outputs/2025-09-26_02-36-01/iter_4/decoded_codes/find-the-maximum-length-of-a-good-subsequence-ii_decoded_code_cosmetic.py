from collections import defaultdict
from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        length_of_nums = len(nums)
        dp = [[0] * (k + 1) for _ in range(length_of_nums)]
        map_list = [defaultdict(int) for _ in range(k + 1)]
        top_values = [[0, 0, 0] for _ in range(k + 1)]  # Each row: [num, highest, second_highest]
        maximum_answer = 0
        pos_be = 0

        while pos_be < length_of_nums:
            current_num = nums[pos_be]
            counter = 0
            while counter <= k:
                dp_value = map_list[counter][current_num]
                dp[pos_be][counter] = dp_value
                if counter > 0:
                    prev_index = counter - 1
                    if top_values[prev_index][0] != nums[pos_be]:
                        if dp[pos_be][counter] < top_values[prev_index][1]:
                            dp[pos_be][counter] = top_values[prev_index][1]
                    else:
                        if dp[pos_be][counter] < top_values[prev_index][2]:
                            dp[pos_be][counter] = top_values[prev_index][2]

                dp[pos_be][counter] += 1

                if current_num not in map_list[counter] or map_list[counter][current_num] < dp[pos_be][counter]:
                    map_list[counter][current_num] = dp[pos_be][counter]

                if top_values[counter][0] != current_num:
                    if dp[pos_be][counter] >= top_values[counter][1]:
                        top_values[counter][2] = top_values[counter][1]
                        top_values[counter][1] = dp[pos_be][counter]
                        top_values[counter][0] = current_num
                    elif top_values[counter][2] < dp[pos_be][counter]:
                        top_values[counter][2] = dp[pos_be][counter]
                else:
                    if top_values[counter][1] < dp[pos_be][counter]:
                        top_values[counter][1] = dp[pos_be][counter]

                if maximum_answer < dp[pos_be][counter]:
                    maximum_answer = dp[pos_be][counter]

                counter += 1
            pos_be += 1

        return maximum_answer