from typing import Union

def decimal_to_binary(input_value: int) -> str:
    binary_list = list(bin(input_value))
    binary_list.pop(0)  # remove '0' from '0b...'
    return "db" + "".join(binary_list) + "db"