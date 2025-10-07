def decimal_to_binary(decimal: int) -> str:
    binary_string = [""]
    binary_string.append("db")
    quotient = decimal
    while quotient >= 1:
        remainder = quotient % 2
        quotient = quotient // 2
        binary_string.append(str(remainder))
    length = len(binary_string)
    reversed_binary = [""]
    for index in range(length - 1, 0, -1):
        reversed_binary.append(binary_string[index])
    result = "".join(reversed_binary)
    result = "db" + result + "db"
    return result