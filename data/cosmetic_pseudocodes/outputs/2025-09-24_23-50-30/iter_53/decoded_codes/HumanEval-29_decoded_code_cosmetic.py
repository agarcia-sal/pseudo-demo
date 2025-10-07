from typing import List

def filter_by_prefix(array_input: List[str], pattern_input: str) -> List[str]:
    queue_temp: List[str] = array_input
    index_marker: int = 0
    result_accumulator: List[str] = []
    while index_marker < len(queue_temp):
        element_current: str = queue_temp[index_marker]
        if not (element_current[:len(pattern_input)] != pattern_input):
            result_accumulator.append(element_current)
        index_marker += 1
    return result_accumulator