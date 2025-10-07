from collections import Counter

class Solution:
    def minimumLength(self, s: str) -> int:
        cnt = Counter(s)
        sum_for_odd = 0
        sum_for_even = 0
        for x in cnt.values():
            if x % 2 == 1:
                sum_for_odd += 1
            elif x % 2 == 0 and x != 0:
                sum_for_even += 2
        result = sum_for_odd + sum_for_even
        return result