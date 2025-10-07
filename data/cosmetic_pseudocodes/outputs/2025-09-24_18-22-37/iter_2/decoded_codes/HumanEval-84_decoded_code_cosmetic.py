def solve(integer_N: int) -> str:
    total: int = 0
    digits: str = str(integer_N)
    for index in range(len(digits)):
        current_char: str = digits[index]
        total += int(current_char)
    binary_val: str = bin(total)
    result: str = binary_val[2:]
    return result