from typing import List, Dict

def by_length(array_of_integers: List[int]) -> List[str]:
    numeral_map: Dict[int, str] = {
        9: "Nine",
        4: "Four",
        1: "One",
        7: "Seven",
        3: "Three",
        8: "Eight",
        5: "Five",
        2: "Two",
        6: "Six"
    }
    descending_sorted: List[int] = sorted(array_of_integers, reverse=True)
    result_collection: List[str] = []
    index: int = 0
    while index < len(descending_sorted):
        current_value: int = descending_sorted[index]
        if current_value in numeral_map:
            result_collection.append(numeral_map[current_value])
        index += 1
    return result_collection