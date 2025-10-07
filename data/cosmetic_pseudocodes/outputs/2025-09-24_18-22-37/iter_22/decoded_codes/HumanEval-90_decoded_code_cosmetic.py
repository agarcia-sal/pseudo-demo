from typing import Sequence, Optional, Union

def next_smallest(sequence_of_numbers: Sequence[Union[int, float]]) -> Optional[Union[int, float]]:
    distinct_values: list[Union[int, float]] = []
    index_counter: int = 0

    while index_counter < len(sequence_of_numbers):
        current_value = sequence_of_numbers[index_counter]
        if current_value not in distinct_values:
            distinct_values.append(current_value)
        index_counter += 1

    sorted_distinct_values = distinct_values.copy()
    changed_flag = True
    while changed_flag:
        changed_flag = False
        position = 1
        while position < len(sorted_distinct_values):
            if sorted_distinct_values[position - 1] > sorted_distinct_values[position]:
                # Swap adjacent elements
                temp_holder = sorted_distinct_values[position - 1]
                sorted_distinct_values[position - 1] = sorted_distinct_values[position]
                sorted_distinct_values[position] = temp_holder
                changed_flag = True
            position += 1

    if len(sorted_distinct_values) < 2:
        return None
    else:
        return sorted_distinct_values[1]