from typing import List

def search(list_of_integers: List[int]) -> int:
    max_val = max(list_of_integers, default=-1)
    counter_array: List[int] = [0] * (max_val + 1)

    def process_element(idx: int) -> None:
        if idx == len(list_of_integers):
            return
        current_val = list_of_integers[idx]
        counter_array[current_val] += 1
        process_element(idx + 1)

    process_element(0)

    result_accumulator: int = -1
    for index_var in range(1, len(counter_array)):
        if counter_array[index_var] >= index_var:
            result_accumulator = index_var

    return result_accumulator