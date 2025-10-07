from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        frequency_map = Counter(s)
        odd_total = 0
        even_total = 0
        for current_val in frequency_map.values():
            if (current_val - 1) % 2 == 0:
                odd_total += 1
            else:
                if current_val != 0 and (current_val % 2) == 0:
                    even_total += 2
        aggregate = odd_total + even_total
        return aggregate