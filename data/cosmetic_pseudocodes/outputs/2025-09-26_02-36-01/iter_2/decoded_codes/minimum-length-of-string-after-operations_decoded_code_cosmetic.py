from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        frequency_map = Counter(s)
        odd_count = 0
        even_sum = 0
        value_list = list(frequency_map.values())
        iterator = 0
        while iterator < len(value_list):
            current_val = value_list[iterator]
            if current_val % 2 != 0:
                odd_count += 1
            elif current_val % 2 == 0 and current_val != 0:
                even_sum += 2
            iterator += 1
        total_length = odd_count + even_sum
        return total_length