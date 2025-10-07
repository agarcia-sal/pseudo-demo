from typing import List

def string_sequence(integer_n: int) -> str:
    number_list: List[str] = []
    current_index: int = 0
    while current_index <= integer_n:
        number_list.append(str(current_index))
        current_index += 1
    return " ".join(number_list)