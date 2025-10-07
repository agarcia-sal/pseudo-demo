def solve(N):
    digit_sum = 0
    for char in str(N):
        digit = int(char)
        digit_sum += digit
    binary_string = bin(digit_sum)[2:]
    return binary_string