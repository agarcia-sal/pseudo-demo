def solve(input_number: int) -> str:
    digit_sum: int = 0
    digit_list: str = str(input_number)
    index: int = 0
    while index < len(digit_list):
        current_character: str = digit_list[index]
        numeric_value: int = int(current_character)
        digit_sum += numeric_value
        index += 1
    full_binary_string: str = bin(digit_sum)
    binary_representation: str = full_binary_string[2:]
    return binary_representation