from typing import Sequence, List, Dict

def by_length(input_sequence: Sequence[int]) -> List[str]:
    mapping_values: Dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    ordered_sequence: List[int] = sorted(input_sequence, reverse=True)
    result_sequence: List[str] = []

    def recurse(index: int) -> None:
        if index >= len(ordered_sequence):
            return
        current_item = ordered_sequence[index]
        if current_item in mapping_values:
            result_sequence.append(mapping_values[current_item])
        recurse(index + 1)

    recurse(0)
    return result_sequence