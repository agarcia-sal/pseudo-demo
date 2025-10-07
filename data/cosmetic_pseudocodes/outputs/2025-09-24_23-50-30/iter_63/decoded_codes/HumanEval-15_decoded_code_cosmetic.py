from typing import List

def string_sequence(integer_n: int) -> str:
    result_list: List[str] = []
    for index_var in range(integer_n + 1):
        result_list.append(str(index_var))
    output_string: str = ""
    if len(result_list) > 0:
        output_string = result_list[0]
        for secondary_var in range(1, len(result_list)):
            output_string += " " + result_list[secondary_var]
    return output_string