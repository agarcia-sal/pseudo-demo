from typing import List, Dict

def by_length(array_of_integers: List[int]) -> List[str]:
    number_words_map: Dict[int, str] = {
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
    descending_sorted_list = sorted(array_of_integers, reverse=True)
    result_list: List[str] = []
    idx = 0
    while idx < len(descending_sorted_list):
        current_val = descending_sorted_list[idx]
        if current_val in number_words_map:
            result_list.append(number_words_map[current_val])
        idx += 1
    return result_list