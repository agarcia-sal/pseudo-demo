from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        modulus = 10**9 + 7
        f_map = defaultdict(int)
        g_map = defaultdict(int)

        for current_element in nums:
            g_map[current_element] = (g_map[current_element] + 1) % modulus
            f_map[current_element] = (f_map[current_element] + current_element) % modulus

            prev_key1 = current_element - 1
            temp1 = f_map[prev_key1]
            temp2 = g_map[prev_key1] * current_element
            sum1 = temp1 + temp2
            f_map[current_element] = (f_map[current_element] + sum1) % modulus

            g_map[current_element] = (g_map[current_element] + g_map[prev_key1]) % modulus

            next_key1 = current_element + 1
            temp3 = f_map[next_key1]
            temp4 = g_map[next_key1] * current_element
            sum2 = temp3 + temp4
            f_map[current_element] = (f_map[current_element] + sum2) % modulus

            g_map[current_element] = (g_map[current_element] + g_map[next_key1]) % modulus

        accumulator = 0
        for val in f_map.values():
            accumulator += val

        final_answer = accumulator % modulus
        return final_answer