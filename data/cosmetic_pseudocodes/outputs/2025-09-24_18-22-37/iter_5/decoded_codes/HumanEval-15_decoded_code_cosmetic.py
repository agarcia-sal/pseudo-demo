from typing import List


def string_sequence(input_num: int) -> str:
    result_list: List[str] = []
    index_var: int = 0
    while index_var <= input_num:
        result_list.append(str(index_var))
        index_var += 1
    output_string: str = ""
    position: int = 0
    while position < len(result_list):
        output_string += result_list[position]
        if position < len(result_list) - 1:
            output_string += " "
        position += 1
    return output_string