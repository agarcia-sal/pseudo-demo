class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(x: int) -> bool:
            def check_divisor(j: int) -> bool:
                if j * j > x:
                    return True
                if x % j == 0 or x % (j + 2) == 0:
                    return False
                return check_divisor(j + 6)

            if x <= 1:
                return False
            if x <= 3:
                return True
            if x % 2 == 0 or x % 3 == 0:
                return False
            return check_divisor(5)

        def ceil_sqrt_val(val: int) -> int:
            def helper(n: int, k: int) -> int:
                if k * k >= n:
                    return k
                return helper(n, k + 1)
            return helper(val, 0)

        def floor_sqrt_val(val: int) -> int:
            def helper(n: int, k: int) -> int:
                if (k + 1) * (k + 1) > n:
                    return k
                return helper(n, k + 1)
            return helper(val, 0)

        alpha = ceil_sqrt_val(l)
        beta = floor_sqrt_val(r)

        def count_primes_in_range(m: int, n: int, acc: int) -> int:
            if m > n:
                return acc
            if is_prime(m):
                return count_primes_in_range(m + 1, n, acc + 1)
            return count_primes_in_range(m + 1, n, acc)

        diff_total = r - l + 1
        prime_found = count_primes_in_range(alpha, beta, 0)
        diff_final = diff_total - prime_found

        return diff_final