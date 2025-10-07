from typing import List

def string_sequence(integer_n: int) -> str:
    result_list: List[str] = [str(index) for index in range(integer_n + 1)]
    output_string: str = ""
    if result_list:
        output_string = result_list[0]
    for position in range(1, len(result_list)):
        output_string += " " + result_list[position]
    return output_string