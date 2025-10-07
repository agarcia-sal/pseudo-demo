def solve(integer_N: int) -> str:
    accumulator: int = 0
    digit_list: str = str(integer_N)
    index: int = 0
    while index < len(digit_list):
        current_char: str = digit_list[index]
        numeric_value: int = int(current_char)
        accumulator += numeric_value
        index += 1
    full_binary_string: str = bin(accumulator)
    result_str: str = full_binary_string[3:]
    return result_str