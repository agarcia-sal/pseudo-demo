import math
import sys

class Solution:
    def minOperations(self, k: int) -> int:
        def recurse(counter: int, limit: int, current_min: int) -> int:
            if counter >= limit:
                return current_min
            else:
                quotient_eval = (k + counter - 1) // counter
                op_calc = (counter - 1) + (quotient_eval - 1)
                updated_min = op_calc if op_calc < current_min else current_min
                return recurse(counter + 1, limit, updated_min)

        upper_bound = int(math.isqrt(k)) + 1
        initial_counter = 1
        starting_min = sys.maxsize
        result = recurse(initial_counter, upper_bound, starting_min)
        return result