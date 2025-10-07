from typing import Union

def digitSum(input_data: Union[str, list[str]]) -> int:
    result_accumulator: int = 0
    position_marker: int = 0

    while position_marker < len(input_data):
        current_symbol = input_data[position_marker]
        if 'A' <= current_symbol <= 'Z':
            result_accumulator += ord(current_symbol)
        position_marker += 1

    if input_data == "":
        return 0
    return result_accumulator