from typing import List

def string_sequence(integer_n: int) -> str:
    list_r: List[str] = []
    index_p: int = 0
    while index_p <= integer_n:
        temp_s: str = str(index_p)
        list_r.append(temp_s)
        index_p += 1
    result_t: str = " ".join(list_r)
    return result_t