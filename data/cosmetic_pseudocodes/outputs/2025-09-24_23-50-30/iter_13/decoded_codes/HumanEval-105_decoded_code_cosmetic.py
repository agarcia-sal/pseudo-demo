from typing import List, Dict


def by_length(list_of_numbers: List[int]) -> List[str]:
    num_map: Dict[int, str] = {
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
    descending_sorted: List[int] = sorted(list_of_numbers, reverse=True)
    result_list: List[str] = [
        num_map[current_val] for current_val in descending_sorted if current_val in num_map
    ]
    return result_list