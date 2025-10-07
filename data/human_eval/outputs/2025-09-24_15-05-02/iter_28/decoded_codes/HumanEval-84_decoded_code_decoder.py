def solve(N: int) -> str:
    digit_sum: int = 0
    for character in str(N):
        digit_sum += int(character)
    binary_result: str = bin(digit_sum)[2:]
    return binary_result