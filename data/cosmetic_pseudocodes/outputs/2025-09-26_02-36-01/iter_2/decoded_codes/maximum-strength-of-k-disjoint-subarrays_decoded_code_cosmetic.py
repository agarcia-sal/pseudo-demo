from math import inf

class Solution:
    def maximumStrength(self, nums: list[int], k: int) -> int:
        total_elements = len(nums)
        dp_array = [[-inf] * (k + 1) for _ in range(total_elements + 1)]
        dp_array[0][0] = 0

        for outer_index in range(1, total_elements + 1):
            for inner_index in range(1, k + 1):
                sum_accumulator = 0
                backward_index = outer_index
                while backward_index >= 1:
                    sum_accumulator += nums[backward_index - 1]
                    if (inner_index % 2) != 0:
                        multiplier_sign = k - inner_index
                    else:
                        multiplier_sign = -(k - inner_index)

                    candidate_value = dp_array[backward_index - 1][inner_index - 1] + multiplier_sign * sum_accumulator
                    if candidate_value > dp_array[outer_index][inner_index]:
                        dp_array[outer_index][inner_index] = candidate_value

                    backward_index -= 1

                alternate_value = dp_array[outer_index - 1][inner_index]
                if alternate_value > dp_array[outer_index][inner_index]:
                    dp_array[outer_index][inner_index] = alternate_value

        return dp_array[total_elements][k]