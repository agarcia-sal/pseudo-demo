def decimal_to_binary(decimal: int) -> str:
    binary_string = ""
    number = decimal
    while number >= 1:
        remainder = number % 2
        digit_string = str(remainder)
        binary_string = digit_string + binary_string
        number = number // 2
    if binary_string == "":
        binary_string = "0"
    result = "db" + binary_string + "db"
    return result