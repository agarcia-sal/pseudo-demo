def solve(integer_N: int) -> str:
    total_sum: int = 0
    string_version: str = str(integer_N)
    index_counter: int = 0
    while index_counter < len(string_version):
        current_char: str = string_version[index_counter]
        digit_value: int = int(current_char)
        total_sum += digit_value
        index_counter += 1
    full_binary: str = bin(total_sum)
    trimmed_binary: str = full_binary[2:]
    return trimmed_binary