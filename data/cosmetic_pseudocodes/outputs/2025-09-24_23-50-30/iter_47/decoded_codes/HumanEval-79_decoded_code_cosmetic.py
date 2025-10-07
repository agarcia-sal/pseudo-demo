from typing import Union

def decimal_to_binary(input_value: Union[int, float]) -> str:
    binary_chars: list[str] = list(bin(int(input_value)))
    return "db" + "".join(binary_chars[1:-1]) + "db"