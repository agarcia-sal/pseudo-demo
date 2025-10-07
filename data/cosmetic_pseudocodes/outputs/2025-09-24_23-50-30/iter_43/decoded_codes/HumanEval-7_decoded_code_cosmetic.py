from typing import Sequence, List

def filter_by_substring(container_x: Sequence[str], pattern_y: str) -> List[str]:
    result_z: List[str] = []
    for index_a in range(len(container_x)):
        element_b = container_x[index_a]
        if pattern_y in element_b:
            result_z.append(element_b)
    return result_z