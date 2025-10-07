def decimal_to_binary(decimal: int) -> str:
    binary_string = ""
    quotient = decimal
    while quotient > 0:
        remainder = quotient % 2
        quotient //= 2
        binary_string = str(remainder) + binary_string
    if binary_string == "":
        binary_string = "0"
    result = "db" + binary_string + "db"
    return result