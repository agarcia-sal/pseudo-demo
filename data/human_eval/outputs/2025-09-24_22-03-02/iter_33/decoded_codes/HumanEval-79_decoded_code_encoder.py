def decimal_to_binary(decimal) -> str:
    binary_representation = ""
    quotient = decimal
    while quotient > 0:
        remainder = quotient % 2
        remainder_character = str(remainder)
        binary_representation = remainder_character + binary_representation
        quotient //= 2
    if binary_representation == "":
        binary_representation = "0"
    result = "db" + binary_representation + "db"
    return result