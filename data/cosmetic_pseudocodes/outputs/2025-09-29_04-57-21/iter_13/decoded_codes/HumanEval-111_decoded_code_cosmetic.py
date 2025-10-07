from typing import Dict

def histogram(test_string: str) -> Dict[str, int]:
    freq_map: Dict[str, int] = {}
    tokens_list = test_string.split(" ")
    highest_frequency = 0

    def update_maximum(index: int) -> None:
        nonlocal highest_frequency
        if index == len(tokens_list):
            return
        element = tokens_list[index]
        if element != "":
            element_count = tokens_list.count(element)
            if element_count > highest_frequency:
                highest_frequency = element_count
        update_maximum(index + 1)

    update_maximum(0)

    if highest_frequency <= 0:
        return freq_map

    def assign_frequency(index: int) -> None:
        if index == len(tokens_list):
            return
        current_item = tokens_list[index]
        if tokens_list.count(current_item) == highest_frequency:
            freq_map[current_item] = highest_frequency
        assign_frequency(index + 1)

    assign_frequency(0)

    return freq_map