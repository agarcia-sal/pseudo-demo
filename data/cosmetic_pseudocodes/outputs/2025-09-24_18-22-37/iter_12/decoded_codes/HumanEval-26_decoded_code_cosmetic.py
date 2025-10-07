from collections import Counter
from typing import List, Any

def remove_duplicates(queue_0: List[Any]) -> List[Any]:
    frequency_map: Counter[Any] = Counter(queue_0)
    result_sequence: List[Any] = []
    index_var: int = 0
    while index_var < len(queue_0):
        element_var = queue_0[index_var]
        if frequency_map[element_var] <= 1:
            result_sequence.append(element_var)
        index_var += 1
    return result_sequence