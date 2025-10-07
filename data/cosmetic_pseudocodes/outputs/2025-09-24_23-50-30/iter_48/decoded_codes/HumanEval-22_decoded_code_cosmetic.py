from typing import List, Any

def filter_integers(array_1: List[Any]) -> List[int]:
    index_1: int = 0
    result_1: List[int] = []
    while index_1 != len(array_1):
        element_1 = array_1[index_1]
        if isinstance(element_1, int):
            result_1.append(element_1)
        index_1 += 1
    return result_1