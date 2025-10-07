def solve(N):
    digit_sum = sum(int(c) for c in str(N))
    binary_result = bin(digit_sum)
    return binary_result[2:]