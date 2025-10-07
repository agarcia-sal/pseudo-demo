from typing import Union


def decimal_to_binary(input_value: Union[int, float]) -> str:
    # Convert integer input to binary string without '0b' prefix; handle floats by converting to int first
    if isinstance(input_value, float):
        input_value = int(input_value)
    binary_string: str = bin(input_value)
    start_substring: int = 2
    result_parts: list[str] = ["db", binary_string[start_substring:], "db"]
    return "".join(result_parts)