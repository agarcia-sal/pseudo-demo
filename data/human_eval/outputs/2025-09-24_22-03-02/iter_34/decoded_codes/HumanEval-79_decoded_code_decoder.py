def decimal_to_binary(decimal) -> str:
    binary_string = ""
    remainder_list = []
    current_value = decimal
    if current_value == 0:
        binary_string = "0"
    else:
        while current_value > 0:
            remainder = current_value % 2
            remainder_list.append(remainder)
            current_value //= 2
        index = len(remainder_list) - 1
        while index >= 0:
            binary_string += str(remainder_list[index])
            index -= 1
    result_string = "db" + binary_string + "db"
    return result_string