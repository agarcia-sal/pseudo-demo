class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(n: int) -> bool:
            if n <= 1:
                return False
            if n <= 3:
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            f = 5
            while f * f <= n:
                if n % f == 0 or n % (f + 2) == 0:
                    return False
                f += 6
            return True

        def calculate_sqrt(x: int) -> int:
            v = 0
            while v * v <= x:
                v += 1
            return v - 1

        y = calculate_sqrt(l)
        ceil_sqrt_l = y if y * y == l else y + 1
        floor_sqrt_r = calculate_sqrt(r)

        start_prime = ceil_sqrt_l
        end_prime = floor_sqrt_r

        special_count = 0
        idx = start_prime
        while idx <= end_prime:
            if is_prime(idx):
                special_count += 1
            idx += 1

        total_count = (r - l) + 1
        answer = total_count - special_count

        return answer