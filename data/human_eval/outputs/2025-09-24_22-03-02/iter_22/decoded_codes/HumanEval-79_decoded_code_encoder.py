def decimal_to_binary(decimal) -> str:
    binary_string = bin(decimal)
    binary_substring = ""
    for index in range(2, len(binary_string)):
        binary_substring += binary_string[index]
    result = "db" + binary_substring + "db"
    return result