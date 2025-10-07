from typing import Sequence, Tuple


def sorted_list_sum(input_sequence: Sequence[str]) -> Tuple[str, ...]:
    def is_even_length(candidate: str) -> bool:
        return len(candidate) % 2 == 0

    sorted_input = sorted(input_sequence)
    filtered_collection: Tuple[str, ...] = ()

    iterator_index = 0
    while iterator_index < len(sorted_input):
        element_candidate = sorted_input[iterator_index]
        if is_even_length(element_candidate):
            filtered_collection += (element_candidate,)
        iterator_index += 1

    filtered_collection = tuple(sorted(filtered_collection, key=len))
    return filtered_collection