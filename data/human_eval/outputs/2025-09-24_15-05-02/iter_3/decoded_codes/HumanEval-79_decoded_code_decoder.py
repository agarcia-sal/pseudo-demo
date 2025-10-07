def binary_representation_of(number):
    result = ""
    if number == 0:
        result = "0"
    else:
        while number > 0:
            remainder = number % 2
            number = number // 2
            result = str(remainder) + result  # prepend remainder as string
    return result


def decimal_to_binary(decimal):
    return "db" + binary_representation_of(decimal) + "db"