from typing import List

def string_sequence(integer_n: int) -> str:
    result_list: List[str] = []
    for index in range(integer_n + 1):
        result_list.append(str(index))
    return " ".join(result_list)