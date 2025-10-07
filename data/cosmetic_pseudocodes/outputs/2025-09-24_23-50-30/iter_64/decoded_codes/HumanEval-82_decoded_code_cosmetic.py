from typing import Any

def prime_length(unrelated_param: Any) -> bool:
    unrelated_var1: int = len(unrelated_param)
    if unrelated_var1 in (0, 1):
        return False

    def prime_length_helper(unrelated_var2: int) -> bool:
        if unrelated_var2 > unrelated_var1 - 2:
            return True
        if unrelated_var1 % unrelated_var2 == 0:
            return False
        return prime_length_helper(unrelated_var2 + 1)

    return prime_length_helper(2)