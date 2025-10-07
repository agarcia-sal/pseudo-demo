def solve(number_input: int) -> str:
    accumulated_sum: int = 0
    digit_list: str = str(number_input)

    idx: int = 0
    while idx < len(digit_list):
        current_char: str = digit_list[idx]
        numeric_val: int = int(current_char)
        accumulated_sum += numeric_val
        idx += 1

    full_binary: str = bin(accumulated_sum)
    trim_index: int = 2
    binary_trimmed: str = full_binary[trim_index:]

    return binary_trimmed