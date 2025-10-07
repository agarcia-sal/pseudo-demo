from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        modulus = 10**9 + 7
        freq_map = defaultdict(int)
        sum_map = defaultdict(int)

        for elem in nums:
            freq_map[elem] = (freq_map[elem] + 1) % modulus
            sum_map[elem] = (sum_map[elem] + elem) % modulus

            prev_key1 = elem - 1
            val1 = sum_map[prev_key1]
            val2 = freq_map[prev_key1]
            mult_val = elem

            sum_map[elem] = (sum_map[elem] + val1 + val2 * mult_val) % modulus
            freq_map[elem] = (freq_map[elem] + freq_map[prev_key1]) % modulus

            next_key1 = elem + 1
            val3 = sum_map[next_key1]
            val4 = freq_map[next_key1]

            sum_map[elem] = (sum_map[elem] + val3 + val4 * mult_val) % modulus
            freq_map[elem] = (freq_map[elem] + freq_map[next_key1]) % modulus

        accumulator = 0
        for key in sum_map:
            accumulator += sum_map[key]

        output = accumulator % modulus
        return output