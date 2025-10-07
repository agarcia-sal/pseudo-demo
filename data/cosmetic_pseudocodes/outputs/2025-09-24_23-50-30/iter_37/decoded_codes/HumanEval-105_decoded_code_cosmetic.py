from typing import List

def by_length(values: List[int]) -> List[str]:
    map_to_words = {
        9: "Nine",
        7: "Seven",
        2: "Two",
        6: "Six",
        4: "Four",
        3: "Three",
        1: "One",
        8: "Eight",
        5: "Five",
    }
    ordered_desc = sorted(values, reverse=True)
    result_list: List[str] = []
    for current in ordered_desc:
        if current not in map_to_words:
            continue
        result_list.append(map_to_words[current])
    return result_list