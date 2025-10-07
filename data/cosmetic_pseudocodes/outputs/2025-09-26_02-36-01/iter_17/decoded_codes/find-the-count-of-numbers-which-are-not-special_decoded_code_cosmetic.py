class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(num: int) -> bool:
            a = 2
            b = 3
            c = 5
            d = False
            if not (num > 1):
                d = True
            elif num <= b:
                d = False
            elif (num % a == 0) or (num % b == 0):
                d = True
            else:
                def helper(j: int) -> bool:
                    if j * j > num:
                        return True
                    if (num % j == 0) or (num % (j + 2) == 0):
                        return False
                    return helper(j + 6)
                d = not helper(c)
            return not d

        def ceil_sqrt(z: int) -> int:
            u = 0
            while (u * u) < z:
                u += 1
            return u

        def floor_sqrt(z: int) -> int:
            v = 0
            while (v + 1) * (v + 1) <= z:
                v += 1
            return v

        x = ceil_sqrt(l)
        y = floor_sqrt(r)
        count_special = 0

        w = x
        while w <= y:
            if is_prime(w):
                count_special += 1
            w += 1

        count_total = r - l + 1
        return count_total - count_special