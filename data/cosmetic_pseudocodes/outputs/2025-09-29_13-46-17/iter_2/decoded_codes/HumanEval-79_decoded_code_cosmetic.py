from typing import Union


def decimal_to_binary(decimal_number: int) -> str:
    bin_str = bin(decimal_number)
    trimmed = bin_str[2:]
    return "db" + trimmed + "db"