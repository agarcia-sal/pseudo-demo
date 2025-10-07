from typing import List

def string_sequence(integer_n: int) -> str:
    result_list: List[str] = []
    counter: int = integer_n
    while counter >= 0:
        result_list.insert(0, str(counter))
        counter -= 1
    return " ".join(result_list)