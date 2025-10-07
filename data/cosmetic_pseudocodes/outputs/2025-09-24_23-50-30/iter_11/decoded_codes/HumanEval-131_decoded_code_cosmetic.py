def digits(m: int) -> int:
    res: int = 1
    tally: int = 0
    digits_str: str = str(m)
    index: int = 0

    while index < len(digits_str):
        current_char: str = digits_str[index]
        num_val: int = int(current_char)

        if num_val % 2 != 0:  # if the digit is odd
            res *= num_val
            tally += 1

        index += 1

    return 0 if tally == 0 else res