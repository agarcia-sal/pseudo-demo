def decimal_to_binary(decimal) -> str:
    binary_string = "db"
    remainder_list = [""]
    number = decimal
    if number == 0:
        remainder_list = ["0"]
    else:
        remainder_list = []
        while number > 0:
            remainder = number % 2
            remainder_list.append(str(remainder))
            number //= 2
    reversed_binary = []
    index = len(remainder_list) - 1
    while index >= 0:
        reversed_binary.append(remainder_list[index])
        index -= 1
    binary_part = ""
    i = 0
    while i < len(reversed_binary):
        binary_part += reversed_binary[i]
        i += 1
    binary_string += binary_part
    binary_string += "db"
    return binary_string