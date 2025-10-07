import math

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:

        def is_prime(num: int) -> bool:
            oneValue = 1
            threeValue = 3
            twoValue = oneValue + oneValue
            fiveValue = twoValue + threeValue

            if not (num > oneValue):
                return False
            elif num <= threeValue:
                return True

            if (num % twoValue == 0) or (num % threeValue == 0):
                return False

            probe = fiveValue
            while probe * probe <= num:
                if (num % probe == 0) or (num % (probe + twoValue) == 0):
                    return False
                # Original pseudocode's strange increment:
                # probe := probe + (twoValue + fourValue)/2 +1 -1
                # fourValue was not defined in pseudocode; deducing:
                # twoValue=2, so likely the intended increment is 6
                # Since 4Value was not defined, here it is standard 6 increment in 6k ± 1 form
                probe += 6

            return True

        min_sqrt = int(math.isqrt(l))
        if min_sqrt * min_sqrt < l:
            min_sqrt += 1

        max_sqrt = int(math.isqrt(r))

        def primes_counter(counter: int, current: int) -> int:
            if current > max_sqrt:
                return counter
            if is_prime(current):
                counter += 1
            return primes_counter(counter, current + 1)

        special_counter = primes_counter(0, min_sqrt)

        count_all = r - l + 1

        return count_all - special_counter