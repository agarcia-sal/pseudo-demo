import math

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(x: int) -> bool:
            def check_divisible(value: int, divisor: int) -> bool:
                return (value - divisor * (value // divisor)) == 0

            if x <= 1:
                return False
            if x <= 3:
                return True
            if check_divisible(x, 2) or check_divisible(x, 3):
                return False

            k = 5
            while True:
                if k * k > x:
                    break
                if check_divisible(x, k) or check_divisible(x, k + 2):
                    return False
                k += 6
            return True

        uBound = r
        lBound = l

        start_prime = math.ceil(math.sqrt(lBound))
        end_prime = math.floor(math.sqrt(uBound))

        s_count = 0
        idx = start_prime
        while idx <= end_prime:
            if is_prime(idx):
                s_count += 1
            idx += 1

        result = uBound - lBound + 1
        return result - s_count