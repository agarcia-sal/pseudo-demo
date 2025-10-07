class Solution:
    def maximumSumSubsequence(self, nums, queries):
        MODULO = 10**9 + 1
        length = len(nums)
        dp_take = [0] * length
        dp_skip = [0] * length

        dp_take[0] = max(0, nums[0])
        dp_skip[0] = 0

        for current_index in range(1, length):
            prev_skip = dp_skip[current_index - 1]
            value_num = nums[current_index]
            dp_take[current_index] = max(0, prev_skip + value_num)

            prev_take = dp_take[current_index - 1]
            dp_skip[current_index] = max(prev_skip, prev_take)

        accumulated_result = 0

        for position, new_value in queries:
            nums[position] = new_value

            if position == 0:
                dp_take[0] = max(0, nums[0])
                dp_skip[0] = 0
            else:
                previous_skip = dp_skip[position - 1]
                current_val = nums[position]
                dp_take[position] = max(0, previous_skip + current_val)

                previous_take = dp_take[position - 1]
                dp_skip[position] = max(previous_skip, previous_take)

            for idx in range(position + 1, length):
                prev_s = dp_skip[idx - 1]
                curr_num = nums[idx]
                dp_take[idx] = max(0, prev_s + curr_num)

                prev_t = dp_take[idx - 1]
                dp_skip[idx] = max(prev_s, prev_t)

            best_val = dp_take[-1] if dp_take[-1] > dp_skip[-1] else dp_skip[-1]
            accumulated_result = (accumulated_result + best_val) % MODULO

        return accumulated_result