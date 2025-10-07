def solve(N):
    digit_sum = 0
    for ch in str(N):
        digit_sum += int(ch)
    binary_string = bin(digit_sum)[2:]
    return binary_string