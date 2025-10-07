def solve(N):
    digits_string = str(N)
    sum_digits = 0
    index = 0
    while index < len(digits_string):
        current_char = digits_string[index]
        current_digit = int(current_char)
        sum_digits += current_digit
        index += 1
    binary_string = bin(sum_digits)
    result = binary_string[2:]
    return result