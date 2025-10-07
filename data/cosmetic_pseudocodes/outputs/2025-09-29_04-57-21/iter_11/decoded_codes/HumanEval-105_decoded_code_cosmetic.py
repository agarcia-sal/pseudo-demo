from typing import List, Dict

def by_length(array_of_integers: List[int]) -> List[str]:
    numeral_map: Dict[int, str] = {
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
    descending_sequence = sorted(array_of_integers, reverse=True)
    accumulator: List[str] = []
    index = 0
    while index < len(descending_sequence):
        current_value = descending_sequence[index]
        if current_value not in numeral_map:
            index += 1
            continue
        accumulator.append(numeral_map[current_value])
        index += 1
    return accumulator