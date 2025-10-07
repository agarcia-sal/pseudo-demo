from typing import List

def string_sequence(integer_p: int) -> str:
    list_y: List[str] = []
    index_k: int = 0
    while index_k <= integer_p:
        temp_i: int = index_k
        temp_s: str = str(temp_i)
        list_y.append(temp_s)
        index_k += 1
    delimiter_str: str = " "
    result_str: str = delimiter_str.join(list_y)
    return result_str