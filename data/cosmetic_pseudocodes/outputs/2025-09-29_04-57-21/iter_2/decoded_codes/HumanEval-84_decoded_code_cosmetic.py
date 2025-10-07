def solve(integer_N: int) -> str:
    aggregate_sum: int = 0
    digits_list: list[str] = list(str(integer_N))
    index: int = 0
    while index < len(digits_list):
        current_digit_char: str = digits_list[index]
        aggregate_sum += int(current_digit_char)
        index += 1
    full_binary_string: str = bin(aggregate_sum)[2:]
    result_binary_substring: str = full_binary_string[3:]
    return result_binary_substring