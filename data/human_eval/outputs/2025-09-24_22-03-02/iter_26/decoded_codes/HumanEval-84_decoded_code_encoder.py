def solve(N):
    digit_sum = 0
    N_string = str(N)
    for index in range(len(N_string)):
        character = N_string[index]
        digit_value = int(character)
        digit_sum += digit_value
    binary_string = bin(digit_sum)
    result = binary_string[2:]
    return result