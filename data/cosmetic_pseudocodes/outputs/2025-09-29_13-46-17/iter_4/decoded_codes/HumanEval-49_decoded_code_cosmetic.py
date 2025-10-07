from typing import Callable

def modp(integer_n: int, integer_p: int) -> int:
    def helper(accumulator: int, counter: int, modulus: int, limit: int) -> int:
        if counter == limit:
            return accumulator
        else:
            return helper((accumulator + accumulator) % modulus, counter + 1, modulus, limit)
    return helper(1, 0, integer_p, integer_n)