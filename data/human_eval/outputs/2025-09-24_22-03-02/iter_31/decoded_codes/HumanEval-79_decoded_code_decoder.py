def decimal_to_binary(decimal: int) -> str:
    binary_string = ""
    quotient = decimal
    while quotient > 0:
        remainder = quotient % 2
        digit = str(remainder)
        binary_string = digit + binary_string
        quotient //= 2
    if binary_string == "":
        binary_string = "0"
    result_string = "db" + binary_string + "db"
    return result_string