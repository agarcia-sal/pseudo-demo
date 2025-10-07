import math

class Solution:
    def nonSpecialCount(self, a: int, b: int) -> int:
        def is_prime(p: int) -> bool:
            if p <= 1:
                return False
            if p <= 3:
                return True
            if p % 2 == 0 or p % 3 == 0:
                return False
            i = 5
            while i * i <= p:
                if p % i == 0 or p % (i + 2) == 0:
                    return False
                i += 6
            return True

        x = math.ceil(math.sqrt(a))
        y = math.floor(math.sqrt(b))

        countSpecial = 0
        z = x
        while z <= y:
            if is_prime(z):
                countSpecial += 1
            z += 1

        fullRange = b - a + 1
        result = fullRange - countSpecial

        return result