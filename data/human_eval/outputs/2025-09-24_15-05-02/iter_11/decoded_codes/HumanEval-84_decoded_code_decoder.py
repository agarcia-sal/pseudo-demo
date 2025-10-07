def solve(N):
    digit_sum = 0
    for character_digit in str(N):
        digit_sum += int(character_digit)
    binary_result = bin(digit_sum)[2:]
    return binary_result