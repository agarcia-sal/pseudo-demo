import math

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(num: int) -> bool:
            if num <= 1:
                return False
            elif num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            x = 5
            while x * x <= num:
                if num % x == 0 or num % (x + 2) == 0:
                    return False
                x += 6
            return True

        a = math.ceil(math.sqrt(l))
        b = math.floor(math.sqrt(r))

        c = 0
        d = a
        while d <= b:
            if is_prime(d):
                c += 1
            d += 1

        e = r - l + 1
        return e - c