def solve(integer_N: int) -> str:
    digit_total: int = 0
    digit_iterator: int = 0
    str_n: str = str(integer_N)

    while digit_iterator < len(str_n):
        current_char: str = str_n[digit_iterator]
        digit_total += int(current_char)
        digit_iterator += 1

    binary_str_full: str = bin(digit_total)
    return binary_str_full[2:]