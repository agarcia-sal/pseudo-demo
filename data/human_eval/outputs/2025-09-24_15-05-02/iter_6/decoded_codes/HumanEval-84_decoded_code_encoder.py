def solve(N):
    digit_sum = 0
    for character in str(N):
        digit_sum += int(character)
    binary_result = bin(digit_sum)[2:]
    return binary_result