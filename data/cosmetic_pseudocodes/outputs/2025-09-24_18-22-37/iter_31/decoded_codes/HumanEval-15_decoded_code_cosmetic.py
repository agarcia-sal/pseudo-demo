from typing import List

def string_sequence(num_limit: int) -> str:
    result_list: List[str] = []
    current_val: int = 0

    while current_val <= num_limit:
        result_list.append(str(current_val))
        current_val += 1

    output_string: str = ""
    index: int = 0
    length: int = len(result_list)

    while index < length:
        output_string += result_list[index]

        if index < length - 1:
            output_string += " "

        index += 1

    return output_string