def solve(parameter_x: int) -> str:
    accumulator: int = 0
    iterator_index: int = 0
    digits_string: str = str(parameter_x)
    while iterator_index < len(digits_string):
        digit_char: str = digits_string[iterator_index]
        accumulator += int(digit_char)
        iterator_index += 1
    binary_str: str = bin(accumulator)  # e.g. '0b101'
    result_str: str = binary_str[2:]    # remove '0b' prefix
    return result_str