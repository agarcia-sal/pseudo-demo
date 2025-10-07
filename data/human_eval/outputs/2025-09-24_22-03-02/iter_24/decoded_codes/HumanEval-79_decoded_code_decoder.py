def decimal_to_binary(decimal):
    binary_string = ""
    remainder_list = [""]
    number = decimal
    while number > 0:
        remainder = number % 2
        remainder_list.append(remainder)
        number = number // 2
    index = len(remainder_list) - 1
    while index >= 0:
        binary_string += str(remainder_list[index])
        index -= 1
    return "db" + binary_string + "db"