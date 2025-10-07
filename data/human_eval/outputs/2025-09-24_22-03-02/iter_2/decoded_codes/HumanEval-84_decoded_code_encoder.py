def solve(N):
    digit_sum = 0
    for character in str(N):
        digit_sum += int(character)
    binary_string = bin(digit_sum)
    return binary_string[2:]