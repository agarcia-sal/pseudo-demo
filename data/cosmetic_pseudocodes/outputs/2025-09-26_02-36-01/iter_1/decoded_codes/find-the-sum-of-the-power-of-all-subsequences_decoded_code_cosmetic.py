class Solution:
    def sumOfPower(self, nums, k):
        MODULUS = 10**9 + 7
        length = len(nums)
        dp_table = [[0] * (k + 1) for _ in range(length + 1)]
        dp_table[0][0] = 1

        for index in range(1, length + 1):
            num = nums[index - 1]
            for sum_val in range(k + 1):
                dp_table[index][sum_val] = dp_table[index - 1][sum_val]
                if sum_val >= num:
                    dp_table[index][sum_val] += dp_table[index - 1][sum_val - num]
                dp_table[index][sum_val] %= MODULUS

        final_result = 0
        for subset_mask in range(1, 1 << length):
            subset_sum = 0
            elements_count = 0
            for pos in range(length):
                if (subset_mask >> pos) & 1 == 1:
                    subset_sum += nums[pos]
                    elements_count += 1
            if subset_sum == k:
                final_result += pow(2, length - elements_count, MODULUS)
                final_result %= MODULUS

        return final_result