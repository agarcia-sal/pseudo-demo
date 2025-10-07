from typing import List

def string_sequence(integer_n: int) -> str:
    index: int = 0
    result_list: List[str] = []
    while index <= integer_n:
        result_list.append(str(index))
        index += 1
    return " ".join(result_list)