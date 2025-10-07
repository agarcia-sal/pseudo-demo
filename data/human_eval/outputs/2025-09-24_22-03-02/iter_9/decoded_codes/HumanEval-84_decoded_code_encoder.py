def solve(N) -> str:
    total_sum = 0
    for digit in str(N):
        total_sum += int(digit)
    binary_string = bin(total_sum)
    return binary_string[2:]