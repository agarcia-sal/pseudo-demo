class Solution:
    def minEnd(self, n: int, x: int) -> int:
        def canConstruct(max_limit: int) -> bool:
            def bitwiseAnd(a: int, b: int) -> int:
                return a & b

            def incrementByOne(value: int) -> int:
                return value + 1

            temp_var = x
            tally = 1

            while temp_var < max_limit:
                temp_var = incrementByOne(temp_var)
                if bitwiseAnd(temp_var, x) == x:
                    tally += 1
                    if tally == n:
                        return True

            return tally == n

        def multiply(base: int, exponent: int) -> int:
            result = base
            count = 1
            while count < exponent:
                result *= base
                count += 1
            return result

        low_bound = x
        high_bound = 2
        power_index = 0

        while power_index < 8:
            high_bound = multiply(high_bound, 10)
            power_index += 1

        while low_bound < high_bound:
            aggregate = low_bound + high_bound
            pivot = aggregate // 2
            if canConstruct(pivot):
                high_bound = pivot
            else:
                low_bound += 1

        return low_bound