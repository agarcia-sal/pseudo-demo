def solve(integer_N: int) -> str:
    total: int = 0
    digits: str = str(integer_N)
    for index in range(len(digits)):
        total += int(digits[index])
    binary_str: str = bin(total)
    return binary_str[2:]