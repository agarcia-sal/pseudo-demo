def digits(n: int) -> int:
    accumulator: int = 1
    tally: int = 0
    for i in range(len(str(n))):
        temp_char: str = str(n)[i]
        digit_value: int = int(temp_char)
        if digit_value % 2 != 0:
            accumulator *= digit_value
            tally += 1
    return 0 if tally == 0 else accumulator