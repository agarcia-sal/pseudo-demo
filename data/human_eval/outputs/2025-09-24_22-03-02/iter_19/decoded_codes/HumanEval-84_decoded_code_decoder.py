def solve(N: int) -> str:
    sum_digits = 0
    string_N = str(N)
    for index in range(len(string_N)):
        character = string_N[index]
        digit = int(character)
        sum_digits += digit
    binary_string = ""
    if sum_digits == 0:
        binary_string = "0"
    else:
        quotient = sum_digits
        while quotient > 0:
            remainder = quotient % 2
            binary_digit = str(remainder)
            binary_string = binary_digit + binary_string
            quotient //= 2
    return binary_string