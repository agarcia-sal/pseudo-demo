from typing import Sequence, List

def by_length(input_sequence: Sequence[int]) -> List[str]:
    mapping_table: dict[int, str] = {
        1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
        6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
    }
    descending_sequence = sorted(input_sequence, reverse=True)
    accumulator: List[str] = []
    for index in range(len(descending_sequence)):
        current_element = descending_sequence[index]
        if current_element in mapping_table:
            mapped_value = mapping_table[current_element]
            accumulator.append(mapped_value)
    return accumulator