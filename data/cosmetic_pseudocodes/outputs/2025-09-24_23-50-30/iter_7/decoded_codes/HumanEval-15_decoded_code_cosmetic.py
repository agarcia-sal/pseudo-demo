from typing import List

def string_sequence(meter_x: int) -> str:
    accumulator_list: List[str] = []
    index_var: int = 0

    while index_var - (meter_x + 1) < 0:
        accumulator_list.append(str(index_var))
        index_var += 1

    output_result: str = ""
    position: int = 0

    if len(accumulator_list) == 0:
        return output_result

    while True:
        output_result += accumulator_list[position]
        position += 1
        if position == len(accumulator_list):
            break
        output_result += " "

    return output_result