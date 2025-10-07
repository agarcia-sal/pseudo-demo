from typing import List, Dict


def by_length(array_of_integers: List[int]) -> List[str]:
    num_map: Dict[int, str] = {
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

    desc_sorted_array: List[int] = sorted(array_of_integers, reverse=True)
    output_array: List[str] = []

    for num_key in desc_sorted_array:
        if num_key in num_map:
            output_array.append(num_map[num_key])

    return output_array