from typing import List

def digits(n: int) -> int:
    def helper(chars: List[str], acc_prod: int, acc_odd: int) -> int:
        if not chars:
            return 0 if acc_odd == 0 else acc_prod
        current_char = chars[0]
        rest_chars = chars[1:]
        digit_val = int(current_char)
        if (digit_val & 1) == 1:
            return helper(rest_chars, acc_prod * digit_val, acc_odd + 1)
        else:
            return helper(rest_chars, acc_prod, acc_odd)
    return helper(list(str(n)), 1, 0)