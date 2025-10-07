def decimal_to_binary(decimal) -> str:
    binary_string = ""
    number = decimal
    if number == 0:
        binary_string = "0"
    else:
        while number > 0:
            remainder = number % 2
            binary_character = str(remainder)
            binary_string = binary_character + binary_string
            number = number // 2
    result = "db" + binary_string + "db"
    return result