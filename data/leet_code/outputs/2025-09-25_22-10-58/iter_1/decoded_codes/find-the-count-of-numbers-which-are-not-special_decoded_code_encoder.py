import math

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(num: int) -> bool:
            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            i = 5
            while i * i <= num:
                if num % i == 0 or num % (i + 2) == 0:
                    return False
                i += 6
            return True

        start_prime = math.ceil(math.sqrt(l))
        end_prime = math.floor(math.sqrt(r))

        special_count = 0
        for num in range(start_prime, end_prime + 1):
            if is_prime(num):
                special_count += 1

        total_count = r - l + 1
        return total_count - special_count