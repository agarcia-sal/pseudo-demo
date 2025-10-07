from typing import List


def string_sequence(integer_q: int) -> str:
    collection_p: List[str] = []
    current_r: int = 0
    while current_r <= integer_q:
        collection_p.append(str(current_r))
        current_r += 1
    result_s: str = ""
    index_t: int = 0
    while index_t < len(collection_p):
        result_s += collection_p[index_t]
        if index_t < len(collection_p) - 1:
            result_s += " "
        index_t += 1
    return result_s