from math import factorial
from collections import Counter

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        factorials = []
        for index in range(n + 1):
            factorials.append(factorial(index))

        result = 0
        encountered = set()
        half_base = 10 ** ((n - 1) // 2)

        iterator = half_base
        upper_bound = half_base * 10
        while iterator < upper_bound:
            num_str = str(iterator)
            reversed_str = num_str[::-1]
            suffix_start_pos = n % 2
            suffix = reversed_str[suffix_start_pos:]
            full_str = num_str + suffix

            full_int = int(full_str)
            if full_int % k != 0:
                iterator += 1
                continue

            sorted_str = ''.join(sorted(full_str))
            if sorted_str in encountered:
                iterator += 1
                continue
            encountered.add(sorted_str)

            freq_map = Counter(sorted_str)

            if '0' in freq_map and freq_map['0'] > 0:
                zero_count = freq_map['0']
                adjusted_value = n - zero_count
                numerator = factorials[adjusted_value] * zero_count
                res = numerator - factorials[n - 1]
            else:
                res = factorials[n]

            for count_value in freq_map.values():
                res //= factorials[count_value]

            result += res
            iterator += 1

        return result