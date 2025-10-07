def solve(input_value: int) -> str:
    total: int = 0
    digits_string: str = str(input_value)
    idx: int = 0
    while idx < len(digits_string):
        current_char: str = digits_string[idx]
        numeric_digit: int = int(current_char)
        total += numeric_digit
        idx += 1

    raw_binary: str = bin(total)
    trimmed_binary: str = raw_binary[2:]  # Slice off the '0b' prefix
    return trimmed_binary