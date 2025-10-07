def solve(input_number: int) -> str:
    accumulator: int = 0
    digit_list_string: str = str(input_number)
    index_counter: int = 0
    while index_counter < len(digit_list_string):
        current_char: str = digit_list_string[index_counter]
        numeric_value: int = int(current_char)
        accumulator += numeric_value
        index_counter += 1
    full_binary_string: str = bin(accumulator)
    result_string: str = full_binary_string[2:]
    return result_string