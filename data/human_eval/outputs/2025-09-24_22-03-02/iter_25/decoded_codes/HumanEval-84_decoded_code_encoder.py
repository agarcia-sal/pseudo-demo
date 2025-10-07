def solve(N) -> str:
    digits_string = str(N)
    sum_of_digits = 0
    for index in range(len(digits_string)):
        current_character = digits_string[index]
        current_digit = int(current_character)
        sum_of_digits += current_digit
    binary_string = bin(sum_of_digits)
    result = ''
    for index in range(2, len(binary_string)):
        result += binary_string[index]
    return result