def solve(N: int) -> str:
    digit_sum = 0
    for i in str(N):
        digit_sum += int(i)
    binary_string = bin(digit_sum)[2:]
    return binary_string