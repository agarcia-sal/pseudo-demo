def decimal_to_binary(decimal):
    binary_string = bin(decimal)[2:]
    return "db" + binary_string + "db"