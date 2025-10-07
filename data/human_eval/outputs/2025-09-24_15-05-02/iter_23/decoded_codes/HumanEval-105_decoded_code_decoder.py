from typing import List

def by_length(array_of_integers: List[int]) -> List[str]:
    digit_to_name_map: dict[int, str] = {
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
    sorted_array: List[int] = sorted(array_of_integers, reverse=True)
    result_list: List[str] = []
    for element in sorted_array:
        if element in digit_to_name_map:
            result_list.append(digit_to_name_map[element])
    return result_list