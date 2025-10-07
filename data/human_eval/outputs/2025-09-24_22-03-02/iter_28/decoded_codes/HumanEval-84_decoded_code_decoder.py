def solve(N) -> str:
    sum_of_digits = 0
    string_representation = ''
    index = 0
    length = len(str(N))
    while index < length:
        character = str(N)[index]
        digit = int(character)
        sum_of_digits += digit
        index += 1
    binary_string = ''
    if sum_of_digits == 0:
        binary_string = "0"
    else:
        quotient = sum_of_digits
        while quotient > 0:
            remainder = quotient % 2
            digit_char = str(remainder)
            binary_string = digit_char + binary_string
            quotient = quotient // 2
    return binary_string