import math

class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        def is_prime(value: int) -> bool:
            if value <= 1:
                return False
            if value <= 3:
                return True
            if value % 2 == 0 or value % 3 == 0:
                return False
            index = 5
            while index * index <= value:
                if value % index == 0 or value % (index + 2) == 0:
                    return False
                index += 6
            return True

        lower_bound = math.ceil(math.sqrt(l))
        upper_bound = math.floor(math.sqrt(r))

        prime_counter = 0
        current_num = lower_bound
        while current_num <= upper_bound:
            if is_prime(current_num):
                prime_counter += 1
            current_num += 1

        range_span = (r - l) + 1
        result = range_span - prime_counter
        return result