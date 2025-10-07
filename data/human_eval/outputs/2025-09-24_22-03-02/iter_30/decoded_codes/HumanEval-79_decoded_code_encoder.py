def decimal_to_binary(decimal: int) -> str:
    binary_string = ""
    quotient = decimal
    while quotient > 0:
        remainder = quotient % 2
        quotient //= 2
        remainder_character = '0'
        if remainder == 1:
            remainder_character = '1'
        binary_string = remainder_character + binary_string
    if binary_string == "":
        binary_string = '0'
    result = 'd' + 'b' + binary_string + 'd' + 'b'
    return result