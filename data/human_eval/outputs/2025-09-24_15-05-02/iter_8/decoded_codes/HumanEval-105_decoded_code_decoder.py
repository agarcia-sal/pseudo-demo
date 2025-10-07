from typing import List, Dict

def by_length(array: List[int]) -> List[str]:
    dictionary: Dict[int, str] = {
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
    sorted_array = sorted(array, reverse=True)
    new_array: List[str] = []
    for element in sorted_array:
        if element in dictionary:
            new_array.append(dictionary[element])
    return new_array