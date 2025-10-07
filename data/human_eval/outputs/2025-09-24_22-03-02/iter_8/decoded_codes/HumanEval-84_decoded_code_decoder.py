def solve(N: int) -> str:
    digit_sum = 0
    for character in str(N):
        digit_sum += int(character)
    binary_result = bin(digit_sum)
    return binary_result[2:]