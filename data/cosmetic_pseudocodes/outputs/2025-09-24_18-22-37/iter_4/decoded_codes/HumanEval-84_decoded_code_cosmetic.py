def solve(integer_N: int) -> str:
    accumulator: int = 0
    digits_string: str = str(integer_N)
    index: int = 0
    while index < len(digits_string):
        current_char: str = digits_string[index]
        numeric_value: int = int(current_char)
        accumulator += numeric_value
        index += 1
    full_binary: str = bin(accumulator)
    trimmed_binary: str = full_binary[3:]
    return trimmed_binary