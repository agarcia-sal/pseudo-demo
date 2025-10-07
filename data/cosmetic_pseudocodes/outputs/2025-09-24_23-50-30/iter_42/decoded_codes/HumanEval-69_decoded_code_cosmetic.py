from typing import List

def search(array_of_numbers: List[int]) -> int:
    frequency_map: dict[int, int] = {}
    max_key: int = 0

    def iterator_loop(index_iter: int) -> None:
        if index_iter == len(array_of_numbers):
            return
        current_val = array_of_numbers[index_iter]
        frequency_map[current_val] = frequency_map.get(current_val, 0) + 1
        if current_val > max_key:
            nonlocal max_key
            max_key = current_val
        iterator_loop(index_iter + 1)

    iterator_loop(0)

    result_candidate: int = -1
    counter: int = 1
    while counter <= max_key:
        if frequency_map.get(counter, 0) >= counter:
            result_candidate = counter
        counter += 1

    return result_candidate