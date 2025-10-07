from typing import List

def string_sequence(integer_n: int) -> str:
    list_result: List[str] = []
    index_counter: int = 0
    while index_counter <= integer_n:
        list_result.append(str(index_counter))
        index_counter += 1
    return " ".join(list_result)