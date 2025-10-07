def digits(param: object) -> int:
    accumulator: int = 1
    tally: int = 0
    index: int = 0
    s: str = str(param)
    while index < len(s):
        temp_char: str = s[index]
        num_val: int = int(temp_char)
        if num_val % 2 != 0:
            accumulator *= num_val
            tally += 1
        index += 1
    return accumulator if tally != 0 else 0