from typing import Union

def decimal_to_binary(decimal_number: int) -> str:
    binary_string: str = ""
    quotient: int = decimal_number

    while quotient > 0:
        remainder: int = quotient % 2
        binary_string = str(remainder) + binary_string
        quotient //= 2

    if not binary_string:
        binary_string = "0"
    formatted_binary: str = "db" + binary_string + "db"
    return formatted_binary