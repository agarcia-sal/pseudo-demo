import math

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(num: int) -> bool:
            if num <= 1:
                return False
            elif num < 4:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            factor = 5
            while factor * factor <= num:
                if num % factor == 0 or num % (factor + 2) == 0:
                    return False
                factor += 6
            return True

        low_limit = math.ceil(math.sqrt(l))
        high_limit = math.floor(math.sqrt(r))
        count_special = 0
        current = low_limit
        while current <= high_limit:
            if is_prime(current):
                count_special += 1
            current += 1
        interval = r - l + 1
        return interval - count_special