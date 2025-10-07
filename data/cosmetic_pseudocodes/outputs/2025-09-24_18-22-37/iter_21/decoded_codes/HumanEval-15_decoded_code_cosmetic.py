from typing import List


def string_sequence(parameter_m: int) -> str:
    temporary_list: List[str] = []
    current_value: int = 0
    while True:
        temporary_list.append(str(current_value))
        current_value += 1
        if current_value > parameter_m:
            break

    result_string: str = ""
    index_counter: int = 0
    length: int = len(temporary_list)
    while index_counter < length:
        if index_counter == length - 1:
            result_string += temporary_list[index_counter]
        else:
            result_string += temporary_list[index_counter] + " "
        index_counter += 1

    return result_string