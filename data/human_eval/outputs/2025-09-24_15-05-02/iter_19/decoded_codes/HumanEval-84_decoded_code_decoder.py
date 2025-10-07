def solve(N: int) -> str:
    digit_sum: int = 0
    for character_digit in str(N):
        digit_sum += int(character_digit)
    binary_string: str = bin(digit_sum)[2:]
    return binary_string