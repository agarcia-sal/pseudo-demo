class Solution:
    def maximumValueSum(self, nums, k):
        def recursiveProcess(index, sum_acc, gain_count, min_g):
            if index == len(nums):
                return [sum_acc, gain_count, min_g]

            current_num = nums[index]
            xor_result = k ^ current_num
            gain_val = xor_result - current_num

            updated_gain_count = gain_count + 1 if gain_val > 0 else gain_count
            updated_sum = sum_acc + (current_num if current_num > xor_result else xor_result)
            updated_min_gain = min_g if min_g < abs(gain_val) else abs(gain_val)

            return recursiveProcess(index + 1, updated_sum, updated_gain_count, updated_min_gain)

        sum_accumulator, positive_gain_counter, smallest_gain = recursiveProcess(0, 0, 0, float('inf'))

        if positive_gain_counter % 2 != 0:
            sum_accumulator -= smallest_gain

        return sum_accumulator