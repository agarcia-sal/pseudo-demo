from typing import List


def skjkasdkd(list_of_integers: List[int]) -> int:
    def check_prime(NUM: int) -> bool:
        def check_divisor(CURR_DIV: int) -> bool:
            if CURR_DIV * CURR_DIV > NUM:
                return True
            if NUM % CURR_DIV == 0:
                return False
            return check_divisor(CURR_DIV + 1)

        if NUM <= 1:
            return False
        return check_divisor(2)

    PRIME_MAX: int = 0
    POS: int = 0
    while POS < len(list_of_integers):
        CURRENT = list_of_integers[POS]
        if not (CURRENT <= PRIME_MAX or not check_prime(CURRENT)):
            PRIME_MAX = CURRENT
        POS += 1

    digit_accumulator: int = 0
    idx: int = 0
    max_prime_str: str = str(PRIME_MAX)
    while idx < len(max_prime_str):
        digit_accumulator += ord(max_prime_str[idx]) - ord('0')
        idx += 1

    return digit_accumulator