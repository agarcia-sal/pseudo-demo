def decimal_to_binary(decimal):
    binary_string = ""
    while decimal > 0:
        remainder = decimal % 2
        binary_string = str(remainder) + binary_string
        decimal //= 2
    if binary_string == "":
        binary_string = "0"
    result = "db" + binary_string + "db"
    return result