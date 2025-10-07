from typing import Iterable, List, Sequence

def by_length(input_collection: Iterable[int]) -> List[str]:
    num_map: dict[int, str] = {
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One",
    }
    descending_sequence: List[int] = sorted(input_collection, reverse=True)
    result: List[str] = []
    index: int = 0
    while index < len(descending_sequence):
        current = descending_sequence[index]
        if current in num_map:
            result.append(num_map[current])
        index += 1
    return result