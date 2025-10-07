from typing import Union


def decimal_to_binary(inputValue: int) -> str:
    binary_str = bin(inputValue)            # Convert to binary string like '0b101'
    stripped_binary = binary_str[2:]        # Remove '0b' prefix
    parts = ["db", stripped_binary, "db"]
    return "".join(parts)