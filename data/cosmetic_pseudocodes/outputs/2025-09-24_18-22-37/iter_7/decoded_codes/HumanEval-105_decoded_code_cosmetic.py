from typing import List, Dict

def by_length(integer_list: List[int]) -> List[str]:
    num_word_map: Dict[int, str] = {
        9: "Nine",
        3: "Three",
        2: "Two",
        5: "Five",
        1: "One",
        4: "Four",
        8: "Eight",
        7: "Seven",
        6: "Six",
    }

    temp_sorted_list: List[int] = sorted(integer_list, reverse=True)
    result_list: List[str] = []

    idx: int = 0
    while idx < len(temp_sorted_list):
        current_val: int = temp_sorted_list[idx]
        if current_val in num_word_map:
            result_list.append(num_word_map[current_val])
        idx += 1

    return result_list