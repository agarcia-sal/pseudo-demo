from typing import List

def string_sequence(integer_n: int) -> str:
    result_list: List[str] = []
    index: int = 0
    while index <= integer_n:
        result_list.append(str(index))
        index += 1
    return " ".join(result_list)