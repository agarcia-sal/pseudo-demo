from typing import Sequence

def below_zero(graph_of_tasks: Sequence[int]) -> bool:
    temp_sum: int = 0
    flag_detection: bool = False
    index_counter: int = 0

    while index_counter < len(graph_of_tasks) and not flag_detection:
        current_value: int = graph_of_tasks[index_counter]
        temp_sum += current_value
        if temp_sum < 0:
            flag_detection = True
        index_counter += 1

    return flag_detection