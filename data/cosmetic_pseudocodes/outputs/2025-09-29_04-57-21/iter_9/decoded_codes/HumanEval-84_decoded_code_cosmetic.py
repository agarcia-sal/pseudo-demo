def solve(integer_N: int) -> str:
    total_sum: int = 0
    digit_chars: str = str(integer_N)
    idx: int = 0
    while idx < len(digit_chars):
        current_char: str = digit_chars[idx]
        total_sum += int(current_char)
        idx += 1
    full_binary_string: str = bin(total_sum)
    stripped_binary_string: str = full_binary_string[2:]
    return stripped_binary_string