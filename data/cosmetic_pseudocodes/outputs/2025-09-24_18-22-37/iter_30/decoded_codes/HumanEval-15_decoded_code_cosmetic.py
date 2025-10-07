from typing import List

def string_sequence(integer_n: int) -> str:
    result_list: List[str] = []
    current_value: int = 0
    while current_value <= integer_n:
        result_list.append(str(current_value))
        current_value += 1

    joined_string: str = ""
    index_counter: int = 0
    length: int = len(result_list)
    while index_counter < length:
        joined_string += result_list[index_counter]
        if index_counter != length - 1:
            joined_string += " "
        index_counter += 1

    return joined_string