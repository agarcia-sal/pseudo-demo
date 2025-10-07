class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(num: int) -> bool:
            def check_divisibility(x: int, y: int) -> bool:
                if y % x == 0 or y % (x + 2) == 0:
                    return False
                return True

            if num <= 1:
                return False
            if num <= 3:
                return True
            if num % 2 == 0 or num % 3 == 0:
                return False

            probe = 5
            while probe * probe <= num:
                if not check_divisibility(probe, num):
                    return False
                probe += 6

            return True

        def count_primes_in_range(a: int, b: int) -> int:
            counter = 0
            current = a
            while current <= b:
                if is_prime(current):
                    counter += 1
                current += 1
            return counter

        def ceil_sqrt(x: int) -> int:
            guess = 0
            while guess * guess < x:
                guess += 1
            return guess

        def floor_sqrt(x: int) -> int:
            guess = 0
            while True:
                guess += 1
                if guess * guess > x:
                    return guess - 1

        lower_bound = ceil_sqrt(l)
        upper_bound = floor_sqrt(r)

        num_special = count_primes_in_range(lower_bound, upper_bound)
        range_size = (r - l) + 1

        return range_size - num_special