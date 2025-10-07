def decimal_to_binary(decimal: int) -> str:
    binary_string = ""
    number = decimal
    if number == 0:
        binary_string = "0"
    else:
        while number > 0:
            remainder = number % 2
            if remainder == 0:
                bit = "0"
            else:
                bit = "1"
            binary_string = bit + binary_string
            number = number // 2
    result = "db" + binary_string
    result = result + "db"
    return result