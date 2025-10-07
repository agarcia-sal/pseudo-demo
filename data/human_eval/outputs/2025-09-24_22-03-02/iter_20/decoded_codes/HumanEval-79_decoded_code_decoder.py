from typing import List

def decimal_to_binary(decimal: int) -> str:
    binary_string: List[str] = []
    temp_decimal = decimal
    if temp_decimal == 0:
        binary_string.append("0")
    else:
        while temp_decimal > 0:
            remainder = temp_decimal % 2
            remainder_character = "0" if remainder == 0 else "1"
            binary_string.append(remainder_character)
            temp_decimal //= 2
        binary_string.reverse()
    result = "db"
    for ch in binary_string:
        result += ch
    result += "db"
    return result