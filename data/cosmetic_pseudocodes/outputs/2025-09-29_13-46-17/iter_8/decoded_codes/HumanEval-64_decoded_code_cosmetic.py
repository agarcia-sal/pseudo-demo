from typing import Callable

def vowels_count(string_input: str) -> int:
    def rho(n: int, e: int, c: int) -> int:
        if c >= n:
            return e
        S = "aeiouAEIOU"
        u = 1 if string_input[c] in S else 0
        return rho(n, e + u, c + 1)

    YFlag = 1 if string_input and string_input[-1] in ('y', 'Y') else 0
    total_length = len(string_input)
    return rho(total_length, 0, 0) + YFlag