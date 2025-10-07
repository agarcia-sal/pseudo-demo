from typing import List

def by_length(input_list: List[int]) -> List[str]:
    word_map: dict[int, str] = {
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
    sorted_desc: List[int] = sorted(input_list, reverse=True)
    # Filter and map values that exist in word_map to their corresponding strings
    result_list: List[str] = [word_map[value] for value in sorted_desc if value in word_map]
    return result_list