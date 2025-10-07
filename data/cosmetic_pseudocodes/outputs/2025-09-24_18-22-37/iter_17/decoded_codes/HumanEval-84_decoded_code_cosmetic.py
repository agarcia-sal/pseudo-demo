def solve(param_m: int) -> str:
    accumulator: int = 0
    iterator_index: int = 1
    digits_str: str = str(param_m)
    while iterator_index <= len(digits_str):
        current_char: str = digits_str[iterator_index - 1]
        digit_val: int = int(current_char)
        accumulator += digit_val
        iterator_index += 1
    binary_form: str = bin(accumulator)
    result_str: str = binary_form[2:]
    return result_str