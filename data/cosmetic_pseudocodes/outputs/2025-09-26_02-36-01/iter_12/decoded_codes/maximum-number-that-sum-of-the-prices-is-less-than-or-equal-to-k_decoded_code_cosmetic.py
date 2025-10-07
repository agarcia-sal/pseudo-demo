class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_set_bits(n: int, pos: int) -> int:
            def power_of_two(exp: int) -> int:
                result = 1
                counter = 0
                while True:
                    if counter == exp:
                        break
                    result *= 2
                    counter += 1
                return result

            accumulator = 0
            segment = power_of_two(pos)
            blocks = n // segment
            accumulator += (blocks // 2) * segment

            if (blocks % 2) == 1:
                remainder = (n % segment) + 1
                accumulator += remainder

            return accumulator

        def accumulated_price(n: int) -> int:
            def is_power_condition(i_local: int, base: int, value_n: int) -> bool:
                exponent = i_local * base - 1
                pow_val = 1
                idx = 0
                while idx != exponent:
                    pow_val *= 2
                    idx += 1
                return pow_val <= value_n

            total_price = 0
            index_var = 1
            while is_power_condition(index_var, x, n):
                bit_position = index_var * x - 1
                increment_value = count_set_bits(n, bit_position)
                total_price += increment_value
                index_var += 1
            return total_price

        def floor_divide(a: int, b: int) -> int:
            return (a - (a % b)) // b

        lower_bound = 1
        upper_bound = 1
        exponent_counter = 0
        while exponent_counter != 60:
            upper_bound *= 2
            exponent_counter += 1

        answer = 0

        def rec_binary_search(low_param: int, high_param: int) -> int:
            if low_param > high_param:
                return high_param

            middle = low_param + floor_divide((high_param - low_param), 2)

            if accumulated_price(middle) <= k:
                return rec_binary_search(middle + 1, high_param)
            else:
                return rec_binary_search(low_param, middle - 1)

        answer = rec_binary_search(lower_bound, upper_bound)
        return answer