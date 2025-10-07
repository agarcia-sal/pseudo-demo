from typing import List


def strange_sort_list(numbers_sequence: List[int]) -> List[int]:
    output_sequence: List[int] = []
    toggle_indicator: bool = True
    numbers = numbers_sequence[:]  # copy to avoid modifying input list
    while True:
        if numbers:
            chosen_element = min(numbers) if toggle_indicator else max(numbers)
            output_sequence.append(chosen_element)
            numbers.remove(chosen_element)
            toggle_indicator = not toggle_indicator
        else:
            break
    return output_sequence