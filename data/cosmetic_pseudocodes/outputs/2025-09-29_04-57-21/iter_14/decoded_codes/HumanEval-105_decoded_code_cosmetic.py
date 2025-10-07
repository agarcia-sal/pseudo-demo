from typing import List

def by_length(array_of_integers: List[int]) -> List[str]:
    numeric_names: dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    descending_list: List[str] = []
    ordered_input = sorted(array_of_integers, reverse=True)
    index = 0
    while index < len(ordered_input):
        current_value = ordered_input[index]
        if current_value not in numeric_names:
            index += 1
            continue
        descending_list.append(numeric_names[current_value])
        index += 1
    return descending_list