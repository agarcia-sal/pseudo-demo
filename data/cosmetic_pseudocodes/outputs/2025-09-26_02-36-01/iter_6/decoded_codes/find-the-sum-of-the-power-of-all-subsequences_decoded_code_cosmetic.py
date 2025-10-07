class Solution:
    def sumOfPower(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7
        len_nums = len(nums)

        # Initialize DP table with zeros: dimensions (len_nums + 1) x (k + 2)
        table = [[0] * (k + 2) for _ in range(len_nums + 1)]
        table[0][0] = 1

        for outer_counter in range(1, len_nums + 1):
            for inner_counter in range(k + 1):
                prev_val = table[outer_counter - 1][inner_counter]
                table[outer_counter][inner_counter] = prev_val
                if inner_counter >= nums[outer_counter - 1]:
                    index_to_use = inner_counter - nums[outer_counter - 1]
                    increment_val = table[outer_counter - 1][index_to_use]
                    table[outer_counter][inner_counter] += increment_val
                table[outer_counter][inner_counter] %= MOD

        final_answer = 0
        mask = 1
        full_mask = (1 << len_nums) - 1

        while mask <= full_mask:
            acc_sum = 0
            bits_set = 0
            for bit_idx in range(len_nums):
                if (mask >> bit_idx) & 1:
                    acc_sum += nums[bit_idx]
                    bits_set += 1
            if acc_sum == k:
                final_answer += pow(2, len_nums - bits_set, MOD)
                final_answer %= MOD
            mask += 1

        return final_answer