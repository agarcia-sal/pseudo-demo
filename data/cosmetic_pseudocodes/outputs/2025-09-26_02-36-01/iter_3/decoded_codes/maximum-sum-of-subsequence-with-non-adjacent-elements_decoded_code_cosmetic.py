class Solution:
    def maximumSumSubsequence(self, nums, queries):
        modulus = 10**9 + 1
        length_of_nums = len(nums)
        list_take = [0] * length_of_nums
        list_skip = [0] * length_of_nums

        list_take[0] = nums[0] if nums[0] > 0 else 0
        list_skip[0] = 0

        for counter in range(1, length_of_nums):
            prev_skip = list_skip[counter - 1]
            current_num = nums[counter]
            candidate_take = prev_skip + current_num
            if candidate_take < 0:
                candidate_take = 0
            list_take[counter] = candidate_take

            prev_take = list_take[counter - 1]
            prev_skip_val = list_skip[counter - 1]
            list_skip[counter] = prev_skip_val if prev_skip_val > prev_take else prev_take

        accumulator = 0
        for pos, val in queries:
            nums[pos] = val

            if pos == 0:
                list_take[0] = nums[0] if nums[0] > 0 else 0
                list_skip[0] = 0
            else:
                left_skip = list_skip[pos - 1]
                val_at_pos = nums[pos]
                calc_take = left_skip + val_at_pos
                if calc_take < 0:
                    calc_take = 0
                list_take[pos] = calc_take

                left_skip_val = list_skip[pos - 1]
                left_take_val = list_take[pos - 1]
                list_skip[pos] = left_skip_val if left_skip_val > left_take_val else left_take_val

            j = pos + 1
            while j < length_of_nums:
                prev_skip_j = list_skip[j - 1]
                num_j = nums[j]
                temp_take = prev_skip_j + num_j
                if temp_take < 0:
                    temp_take = 0
                list_take[j] = temp_take

                prev_skip_j_val = list_skip[j - 1]
                prev_take_j_val = list_take[j - 1]
                list_skip[j] = prev_skip_j_val if prev_skip_j_val > prev_take_j_val else prev_take_j_val
                j += 1

            last_take = list_take[length_of_nums - 1]
            last_skip = list_skip[length_of_nums - 1]
            max_last = last_take if last_take > last_skip else last_skip
            accumulator = (accumulator + max_last + modulus) % modulus

        return accumulator