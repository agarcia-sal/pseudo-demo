def solve(integer_N: int) -> str:
    total_digits_sum: int = 0
    str_n: str = str(integer_N)
    for index in range(1, len(str_n) + 1):
        current_char: str = str_n[index - 1]
        digit_val: int = int(current_char)
        total_digits_sum += digit_val
    full_binary_str: str = bin(total_digits_sum)
    trimmed_binary_str: str = full_binary_str[3:]
    return trimmed_binary_str