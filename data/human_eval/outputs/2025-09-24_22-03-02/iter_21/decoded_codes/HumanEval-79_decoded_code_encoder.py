def decimal_to_binary(decimal) -> str:
    binary_string = ""
    remainder_list = [""]
    quotient = decimal
    while quotient > 0:
        remainder = quotient % 2
        quotient = quotient // 2
        remainder_list.insert(0, remainder)
    for index in range(len(remainder_list)):
        binary_string += str(remainder_list[index])
    result_string = "db" + binary_string + "db"
    return result_string