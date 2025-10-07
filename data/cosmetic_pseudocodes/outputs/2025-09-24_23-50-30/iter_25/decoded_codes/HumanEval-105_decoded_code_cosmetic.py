from typing import Iterable, List

def by_length(sequence_of_numbers: Iterable[int]) -> List[str]:
    mapping_numbers: dict[int, str] = {
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One"
    }
    ordered_sequence = sorted(sequence_of_numbers, reverse=True)
    buffer_list: List[str] = []
    index_counter = 0
    while index_counter < len(ordered_sequence):
        current_item = ordered_sequence[index_counter]
        if current_item in mapping_numbers:
            buffer_list.append(mapping_numbers[current_item])
        index_counter += 1
    return buffer_list