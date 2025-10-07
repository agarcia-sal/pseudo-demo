class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(num: int) -> bool:
            def check_divisor(divisor: int, limit: int) -> bool:
                if divisor * divisor > limit:
                    return True
                else:
                    if (num % divisor == 0) or (num % (divisor + 2) == 0):
                        return False
                    else:
                        return check_divisor(divisor + 6, limit)

            if num <= 1:
                prime_flag = False
            elif num <= 3:
                prime_flag = True
            elif (num % 2 == 0) or (num % 3 == 0):
                prime_flag = False
            else:
                prime_flag = check_divisor(5, num)
            return prime_flag

        lower_bound = 0
        while lower_bound * lower_bound < l:
            lower_bound += 1

        upper_bound = l
        while upper_bound * upper_bound < r:
            upper_bound += 1
        if upper_bound * upper_bound > r:
            upper_bound -= 1

        prime_tally = 0

        def count_primes(current: int, target: int) -> None:
            nonlocal prime_tally
            if current > target:
                return
            if is_prime(current):
                prime_tally += 1
            count_primes(current + 1, target)

        count_primes(lower_bound, upper_bound)

        range_span = r - l + 1
        result = range_span - prime_tally

        return result