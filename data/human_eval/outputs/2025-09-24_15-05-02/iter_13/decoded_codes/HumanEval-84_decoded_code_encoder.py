def solve(N):
    digit_sum = 0
    for digit in str(N):
        digit_sum += int(digit)
    binary_representation = bin(digit_sum)[2:]
    return binary_representation