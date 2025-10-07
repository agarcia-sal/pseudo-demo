import math

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(num: int) -> bool:
            if not (num > 1):
                return False
            if num <= 3:
                return True
            if (num % 2 == 0) or (num % 3 == 0):
                return False

            f = 5
            while f * f <= num:
                if (num % f == 0) or (num % (f + 2) == 0):
                    return False
                f += 6

            return True

        i = 0
        while True:
            j = math.ceil(math.sqrt(l))
            start_prime = j
            if (j * j) >= l:
                break
            i += 1  # Incremented but unused as in pseudocode

        k = math.floor(math.sqrt(r))
        end_prime = k

        special_count = 0
        m = start_prime
        while m <= end_prime:
            if is_prime(m):
                special_count += 1
            m += 1

        n = r - l + 1
        result = n - special_count
        return result