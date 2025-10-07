from typing import List

def by_length(list_of_vals: List[int]) -> List[str]:
    dictionary_map: dict[int, str] = {
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

    result_col: List[str] = []

    ordered: List[int] = []

    index: int = len(list_of_vals)
    while True:
        index -= 1
        ordered.append(list_of_vals[index])
        if index <= 0:
            break

    iterator: int = 0
    while iterator < len(ordered):
        current: int = ordered[iterator]
        if current in dictionary_map:
            result_col.append(dictionary_map[current])
        iterator += 1

    return result_col