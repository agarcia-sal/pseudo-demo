def solve(N):
    sum_digits = 0
    string_N = str(N)
    length_string_N = len(string_N)
    index = 0
    while index < length_string_N:
        digit_character = string_N[index]
        digit_integer = int(digit_character)
        sum_digits += digit_integer
        index += 1
    binary_string = ""
    if sum_digits == 0:
        binary_string = "0"
    else:
        quotient = sum_digits
        remainder_stack = []
        while quotient > 0:
            remainder = quotient % 2
            remainder_stack.append(remainder)
            quotient = quotient // 2
        length_remainder_stack = len(remainder_stack)
        index = length_remainder_stack - 1
        while index >= 0:
            binary_string += str(remainder_stack[index])
            index -= 1
    return binary_string