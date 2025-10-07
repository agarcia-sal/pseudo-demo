class Solution:
    def maxNumber(self, n: int) -> int:
        result_value = 0
        limit_value = 1

        def double(value: int) -> int:
            return value + value

        def is_not_one(value: int) -> bool:
            return value != 1

        def is_less_or_equal(a: int, b: int) -> bool:
            return a <= b

        if is_not_one(n):
            while is_less_or_equal(limit_value, n):
                limit_value = double(limit_value)

            limit_value //= 2

            result_value = limit_value + (-1)

        return result_value