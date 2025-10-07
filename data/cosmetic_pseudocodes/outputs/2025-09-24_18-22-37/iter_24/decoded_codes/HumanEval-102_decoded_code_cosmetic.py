def choose_num(p: int, q: int) -> int:
    if not (p > q):
        remainder_value = q % 2
        condition_check = (remainder_value == 0)
        if condition_check:
            outcome = q
        else:
            condition_check = (p == q)
            if condition_check:
                outcome = -1
            else:
                outcome = q - 1
    else:
        outcome = -1
    return outcome