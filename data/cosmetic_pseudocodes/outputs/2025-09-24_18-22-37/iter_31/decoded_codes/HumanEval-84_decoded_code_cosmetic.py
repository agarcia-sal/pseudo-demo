def solve(input_number: int) -> str:
    accumulator: int = 0
    digits_string: str = str(input_number)
    idx: int = 0
    while idx < len(digits_string):
        current_char: str = digits_string[idx]
        numeric_value: int = int(current_char)
        accumulator += numeric_value
        idx += 1

    full_binary: str = bin(accumulator)
    trimmed_binary: str = full_binary[2:]
    return trimmed_binary