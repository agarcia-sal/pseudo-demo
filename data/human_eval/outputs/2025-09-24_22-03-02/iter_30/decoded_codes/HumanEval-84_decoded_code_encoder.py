def solve(N):
    digits_string = str(N)
    sum_digits = 0
    index = 0
    while index < len(digits_string):
        char_digit = digits_string[index]
        digit_integer = int(char_digit)
        sum_digits += digit_integer
        index += 1
    binary_string = bin(sum_digits)
    result_string = ""
    index = 2
    while index < len(binary_string):
        result_string += binary_string[index]
        index += 1
    return result_string