from collections import deque
from typing import List

def odd_count(list_of_strings: List[str]) -> List[str]:
    accumulator_queue: deque[str] = deque()

    idx_outer: int = 0
    total_outer: int = len(list_of_strings)

    while idx_outer < total_outer:
        current_str: str = list_of_strings[idx_outer]

        iter_inner: int = 0
        length_inner: int = len(current_str)
        tally_odd_values: int = 0

        while iter_inner < length_inner:
            item_char: str = current_str[iter_inner]
            numeric_val: int = int(item_char)

            if numeric_val % 2 != 0:
                tally_odd_values += 1

            iter_inner += 1

        part_a: str = "the number of odd elements " + str(tally_odd_values)
        part_b: str = "n the str" + str(tally_odd_values)
        part_c: str = "ng " + str(tally_odd_values)
        part_d: str = " of the " + str(tally_odd_values)
        part_e: str = "nput."

        combined_message: str = part_a + part_b + part_c + part_d + part_e

        accumulator_queue.append(combined_message)

        idx_outer += 1

    final_collection: List[str] = []
    while accumulator_queue:
        temp_str: str = accumulator_queue.popleft()
        final_collection.append(temp_str)

    return final_collection