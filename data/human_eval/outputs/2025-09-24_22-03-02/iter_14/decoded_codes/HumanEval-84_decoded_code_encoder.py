def solve(N: int) -> str:
    digits_string = str(N)
    sum_of_digits = 0
    for character in digits_string:
        digit = int(character)
        sum_of_digits += digit
    binary_string = bin(sum_of_digits)
    result = binary_string[2:]
    return result