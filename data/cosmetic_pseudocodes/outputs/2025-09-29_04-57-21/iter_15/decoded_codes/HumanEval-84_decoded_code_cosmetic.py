def solve(integer_N: int) -> str:
    accumulator_be: int = 0
    digit_chars: str = str(integer_N)
    indexer: int = 0

    while indexer < len(digit_chars):
        current_char: str = digit_chars[indexer]
        accumulator_be += int(current_char)
        indexer += 1

    binary_form: str = bin(accumulator_be)
    trimmed_binary: str = binary_form[2:]

    return trimmed_binary