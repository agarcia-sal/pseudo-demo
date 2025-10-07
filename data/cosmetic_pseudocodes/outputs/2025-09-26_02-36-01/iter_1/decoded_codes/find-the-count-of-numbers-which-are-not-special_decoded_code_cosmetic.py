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
            divisor = 5
            while divisor * divisor <= num:
                if num % divisor == 0 or num % (divisor + 2) == 0:
                    return False
                divisor += 6
            return True

        lower_bound = math.ceil(math.sqrt(l))
        upper_bound = math.floor(math.sqrt(r))
        prime_counter = 0

        for value in range(lower_bound, upper_bound + 1):
            if is_prime(value):
                prime_counter += 1

        range_size = r - l + 1
        return range_size - prime_counter