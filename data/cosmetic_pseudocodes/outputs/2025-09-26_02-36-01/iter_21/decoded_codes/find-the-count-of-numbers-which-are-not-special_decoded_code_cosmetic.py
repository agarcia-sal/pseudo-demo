class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(num: int) -> bool:
            def check_prime_recursive(x: int) -> bool:
                if x * x > num:
                    return True
                if num % x == 0:
                    return False
                if num % (x + 2) == 0:
                    return False
                return check_prime_recursive(x + 6)

            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False
            return check_prime_recursive(5)

        def sqrt_floor(x: int) -> int:
            result = 0
            while True:
                candidate = result + 1
                if candidate * candidate > x:
                    break
                result = candidate
            return result

        def sqrt_ceil(x: int) -> int:
            res = 0
            while res * res < x:
                res += 1
            if res * res == x:
                return res
            return res

        v3 = l
        v4 = r

        start_prime = sqrt_ceil(v3)
        end_prime = sqrt_floor(v4)

        def loop_increment(a: int, b: int, c: int) -> int:
            if a > b:
                return c
            if is_prime(a):
                c += 1
            return loop_increment(a + 1, b, c)

        counter = loop_increment(start_prime, end_prime, 0)
        total_count = (r - l) + 1

        return total_count - counter