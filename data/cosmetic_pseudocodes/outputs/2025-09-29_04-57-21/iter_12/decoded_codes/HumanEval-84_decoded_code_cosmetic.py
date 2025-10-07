def solve(integer_N: int) -> str:
    total_sum: int = 0
    chars: str = str(integer_N)
    index: int = 0
    while index < len(chars):
        char: str = chars[index]
        total_sum += int(char)
        index += 1
    binary_str: str = bin(total_sum)
    result: str = binary_str[2:]
    return result