def digits(n: int) -> int:
    accumulator: int = 1
    tally: int = 0
    index: int = 0
    num_str: str = str(n)
    while index < len(num_str):
        current_char: str = num_str[index]
        digit_val: int = int(current_char)
        if digit_val % 2 == 1:
            accumulator *= digit_val
            tally += 1
        index += 1
    return accumulator if tally != 0 else 0