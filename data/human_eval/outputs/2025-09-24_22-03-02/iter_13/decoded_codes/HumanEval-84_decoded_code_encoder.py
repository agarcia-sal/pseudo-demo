def solve(N) -> str:
    digits_string = str(N)
    sum_of_digits = sum(int(character) for character in digits_string)
    binary_string = bin(sum_of_digits)
    result = binary_string[2:]
    return result