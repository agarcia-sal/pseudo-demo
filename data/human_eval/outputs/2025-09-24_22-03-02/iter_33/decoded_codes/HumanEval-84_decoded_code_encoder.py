def solve(N: int) -> str:
    digits_string = str(N)
    sum_of_digits = 0
    for index in range(len(digits_string)):
        char_digit = digits_string[index]
        digit_integer = int(char_digit)
        sum_of_digits += digit_integer
    binary_string = bin(sum_of_digits)
    result_string = binary_string[2:]
    return result_string