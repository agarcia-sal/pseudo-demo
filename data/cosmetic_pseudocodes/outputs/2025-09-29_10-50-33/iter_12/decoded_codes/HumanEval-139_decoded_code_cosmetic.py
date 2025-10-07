from typing import Callable

def special_factorial(integer_n: int) -> int:
    def helper_factorial(
        accumulated_factorial: int,
        iterator: int,
        limit: int,
        accumulated_result: int,
    ) -> int:
        if iterator > limit:
            return accumulated_result
        updated_factorial = accumulated_factorial * iterator
        updated_result = accumulated_result * updated_factorial
        return helper_factorial(updated_factorial, iterator + 1, limit, updated_result)

    return helper_factorial(1, 1, integer_n, 1)