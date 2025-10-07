def decimal_to_binary(decimal) -> str:
    binary_string = bin(decimal)
    trimmed_binary = ""
    for index in range(2, len(binary_string)):
        current_character = binary_string[index]
        trimmed_binary += current_character
    result = "db" + trimmed_binary
    result += "db"
    return result