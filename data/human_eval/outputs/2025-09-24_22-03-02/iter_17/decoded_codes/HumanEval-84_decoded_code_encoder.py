def solve(N):
    total_sum = 0
    string_representation = str(N)
    for character in string_representation:
        digit = int(character)
        total_sum += digit
    binary_string = bin(total_sum)
    result = binary_string[2:]
    return result