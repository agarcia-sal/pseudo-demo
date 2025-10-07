class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(num: int) -> bool:
            def divides(x: int, y: int) -> bool:
                return (x % y) == 0

            if not (num > 1):
                return False
            elif num <= 3:
                return True
            elif divides(num, 2) or divides(num, 3):
                return False

            idx = 5
            while idx * idx <= num:
                if divides(num, idx) or divides(num, idx + 2):
                    return False
                idx += 6
            return True

        def ceil_sqrt(x: int) -> int:
            a = 0
            while a * a < x:
                a += 1
            return a

        def floor_sqrt(x: int) -> int:
            b = 0
            while (b + 1) * (b + 1) <= x:
                b += 1
            return b

        sp = ceil_sqrt(l)
        ep = floor_sqrt(r)

        count_s = 0

        def increment_if_prime(val: int):
            nonlocal count_s
            if is_prime(val):
                count_s += 1

        for z in range(sp, ep + 1):
            increment_if_prime(z)

        total_elems = (r - l) + 1
        return total_elems - count_s