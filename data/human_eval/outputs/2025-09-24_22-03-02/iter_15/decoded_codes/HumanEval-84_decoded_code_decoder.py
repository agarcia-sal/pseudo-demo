def solve(N) -> str:
    sum_of_digits = 0
    for character in str(N):
        digit = int(character)
        sum_of_digits += digit
    binary_representation = bin(sum_of_digits)
    output_string = binary_representation[2:]
    return output_string