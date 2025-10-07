def solve(integer_N: int) -> str:
    digit_sum: int = 0
    digits: str = str(integer_N)
    index: int = 0
    while index < len(digits):
        current_char: str = digits[index]
        numeric_value: int = int(current_char)
        digit_sum += numeric_value
        index += 1
    binary_str: str = bin(digit_sum)
    return binary_str[2:]