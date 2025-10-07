class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(a1: int) -> bool:
            def check_divisible(x: int, y: int) -> bool:
                return x % y == 0

            if a1 <= 1:
                return False
            elif a1 <= 3:
                return True

            if check_divisible(a1, 2) or check_divisible(a1, 3):
                return False

            def incr_by_six(z: int) -> int:
                return z + 6

            def composite_check(val: int, offset: int) -> bool:
                return check_divisible(val, offset) or check_divisible(val, offset + 2)

            z_val = 5
            while z_val * z_val <= a1:
                if composite_check(a1, z_val):
                    return False
                z_val = incr_by_six(z_val)

            return True

        def ceil_sqrt(x: int) -> int:
            base = 0
            while base * base < x:
                base += 1
            return base

        def floor_sqrt(y: int) -> int:
            base = y
            while base * base > y:
                base -= 1
            return base

        def count_primes_in_range(start_val: int, end_val: int) -> int:
            if start_val > end_val:
                return 0
            if is_prime(start_val):
                return 1 + count_primes_in_range(start_val + 1, end_val)
            return count_primes_in_range(start_val + 1, end_val)

        v1 = ceil_sqrt(l)
        v2 = floor_sqrt(r)
        c_accum = count_primes_in_range(v1, v2)
        full_range = (r - l) + 1
        result_final = full_range - c_accum

        return result_final