from typing import Callable


def digits(n: int) -> int:
    def helper(idx: int, digits_str: str, prod_accum: int, odd_tally: int) -> int:
        if idx >= len(digits_str):
            return (0 if odd_tally == 0 else prod_accum)
        current_val = int(digits_str[idx])
        # prod_accum update based on parity of current_val: 
        # if even (current_val % 2 == 0), add prod_accum
        # if odd multiply by 2 (1 + 1)
        prod_update = prod_accum * (1 + (current_val % 2)) + prod_accum * (current_val % 2 == 0)
        return helper(idx + 1, digits_str, prod_update, odd_tally + (current_val % 2))

    return helper(0, str(n), 1, 0)