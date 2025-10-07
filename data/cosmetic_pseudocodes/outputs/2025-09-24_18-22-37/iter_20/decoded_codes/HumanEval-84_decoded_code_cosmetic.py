def solve(integer_N: int) -> str:
    accumulated_sum: int = 0
    digit_string: str = str(integer_N)

    current_position: int = 0
    length_of_digits: int = len(digit_string)

    while current_position < length_of_digits:
        current_char: str = digit_string[current_position]
        current_value: int = int(current_char)
        accumulated_sum += current_value
        current_position += 1

    full_binary_form: str = bin(accumulated_sum)
    trimmed_binary_result: str = full_binary_form[2:]

    return trimmed_binary_result