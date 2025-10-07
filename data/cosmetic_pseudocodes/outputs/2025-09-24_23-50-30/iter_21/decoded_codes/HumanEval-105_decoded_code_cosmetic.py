from collections import deque
from typing import List, Dict

def by_length(parameter_list: List[int]) -> List[str]:
    mapping: Dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }

    result_queue: deque[str] = deque()

    sorted_collection = sorted(parameter_list, reverse=True)

    def recursive_process(index_counter: int) -> None:
        if index_counter > len(parameter_list):
            return
        current_value = sorted_collection[index_counter - 1]  # index adjusted for 0-based
        if current_value in mapping:
            result_queue.append(mapping[current_value])
        recursive_process(index_counter + 1)

    recursive_process(1)

    final_result: List[str] = []
    while result_queue:
        element_var = result_queue.popleft()
        final_result.append(element_var)

    return final_result