def digits(k: int) -> int:
    accumulator: int = 1
    tally: int = 0
    index: int = 0
    sequence: str = str(k)
    while index < len(sequence):
        current_char: str = sequence[index]
        current_num: int = int(current_char)
        if current_num % 2 == 1:
            accumulator *= current_num
            tally += 1
        index += 1
    return accumulator if tally != 0 else 0