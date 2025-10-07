def solve(N):
    digits_sum = 0
    for digit in str(N):
        digits_sum += int(digit)
    binary_string = bin(digits_sum)[2:]
    return binary_string