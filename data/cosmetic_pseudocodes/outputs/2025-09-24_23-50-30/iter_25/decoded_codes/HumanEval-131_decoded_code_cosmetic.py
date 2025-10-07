def digits(m: int) -> int:
    mul_result: int = 1
    tally_odds: int = 0
    str_num: str = str(m)
    index: int = 0
    while index < len(str_num):
        char_digit: str = str_num[index]
        digit_val: int = int(char_digit)
        if digit_val % 2 != 0:
            mul_result *= digit_val
            tally_odds += 1
        index += 1
    if tally_odds == 0:
        return 0
    return mul_result