def solve(N):
    sum_of_digits = 0
    string_N = str(N)
    for index in range(len(string_N)):
        character = string_N[index]
        digit = int(character)
        sum_of_digits += digit
    binary_string = ""
    if sum_of_digits == 0:
        binary_string = "0"
    else:
        remainder_list = [""]
        quotient = sum_of_digits
        while quotient > 0:
            remainder = quotient % 2
            quotient = quotient // 2
            remainder_list.append(str(remainder))
        index = len(remainder_list) - 1
        while index >= 0:
            binary_string += remainder_list[index]
            index -= 1
    return binary_string