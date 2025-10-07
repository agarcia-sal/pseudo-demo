def decimal_to_binary(decimal: int) -> str:
    binary_string = ""
    number = decimal
    if number == 0:
        binary_string = "0"
    else:
        while number > 0:
            remainder = number % 2
            number = number // 2
            digit = ""
            if remainder == 0:
                digit = "0"
            else:
                digit = "1"
            binary_string = digit + binary_string
    result = "db" + binary_string + "db"
    return result