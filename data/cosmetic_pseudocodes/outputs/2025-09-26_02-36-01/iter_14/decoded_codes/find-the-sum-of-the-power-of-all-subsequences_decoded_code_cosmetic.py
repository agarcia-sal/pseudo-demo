class Solution:
    def sumOfPower(self, nums: list[int], k: int) -> int:
        modulus = 10**9 + 7
        size = len(nums)
        table = [[0] * (k + 1) for _ in range(size + 1)]
        table[0][0] = 1

        for index_outer in range(1, size + 1):
            for index_inner in range(k + 1):
                table[index_outer][index_inner] = table[index_outer - 1][index_inner]
                if index_inner >= nums[index_outer - 1]:
                    table[index_outer][index_inner] += table[index_outer - 1][index_inner - nums[index_outer - 1]]
                table[index_outer][index_inner] %= modulus

        accumulated_power = 0
        limit = (1 << size) - 1

        for iterator in range(1, limit + 1):
            sum_elements = 0
            count_ones = 0
            pos = 0
            while pos < size:
                if (iterator >> pos) & 1 == 1:
                    sum_elements += nums[pos]
                    count_ones += 1
                pos += 1
            if sum_elements == k:
                accumulated_power += pow(2, size - count_ones, modulus)
                accumulated_power %= modulus

        return accumulated_power