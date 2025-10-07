from typing import List

def string_sequence(integer_n: int) -> str:
    result_list: List[str] = []
    index: int = 0
    while index <= integer_n:
        result_list.append(str(index))
        index += 1
    output_string: str = ""
    for position in range(len(result_list) - 1):
        output_string += result_list[position] + " "
    output_string += result_list[-1]
    return output_string