from typing import List

def by_length(parameter_array: List[int]) -> List[str]:
    num_word_map: dict[int, str] = {
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

    descending_list: List[int] = sorted(parameter_array, reverse=True)
    reordered_list: List[str] = []

    idx: int = 0
    while idx < len(descending_list):
        current_val = descending_list[idx]
        if current_val in num_word_map:
            reordered_list.append(num_word_map[current_val])
        idx += 1

    return reordered_list