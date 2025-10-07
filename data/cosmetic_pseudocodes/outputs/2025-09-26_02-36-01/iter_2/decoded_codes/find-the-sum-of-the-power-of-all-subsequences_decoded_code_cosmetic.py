class Solution:
    def sumOfPower(self, nums, k):
        MODULUS = 10**9 + 7
        length = len(nums)
        dp_matrix = [[0] * (k + 1) for _ in range(length + 1)]
        dp_matrix[0][0] = 1

        for idx_outer in range(1, length + 1):
            for idx_inner in range(k + 1):
                dp_matrix[idx_outer][idx_inner] = dp_matrix[idx_outer - 1][idx_inner]
                val = nums[idx_outer - 1]
                if idx_inner >= val:
                    dp_matrix[idx_outer][idx_inner] += dp_matrix[idx_outer - 1][idx_inner - val]
                dp_matrix[idx_outer][idx_inner] %= MODULUS

        aggregate_power = 0
        max_subset_bitmask = (1 << length) - 1
        bitmask_counter = 1
        while bitmask_counter <= max_subset_bitmask:
            subset_sum = 0
            subset_len = 0
            position = 0
            while position < length:
                if (bitmask_counter >> position) & 1:
                    subset_sum += nums[position]
                    subset_len += 1
                position += 1
            if subset_sum == k:
                complement_len = length - subset_len
                aggregate_power += pow(2, complement_len, MODULUS)
                aggregate_power %= MODULUS
            bitmask_counter += 1

        return aggregate_power