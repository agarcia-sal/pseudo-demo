def solve(N):
    sum_digits = 0
    string_N = str(N)
    for index in range(len(string_N)):
        current_character = string_N[index]
        integer_digit = int(current_character)
        sum_digits += integer_digit
    binary_string = ""
    if sum_digits == 0:
        binary_string = "0"
    else:
        quotient = sum_digits
        remainder_list = []
        while quotient > 0:
            remainder = quotient % 2
            remainder_list.append(str(remainder))
            quotient //= 2
        index = len(remainder_list) - 1
        while index >= 0:
            binary_string += remainder_list[index]
            index -= 1
    return binary_string