from typing import Sequence, List

def by_length(data_sequence: Sequence[int]) -> List[str]:
    num_map = {
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
    desc_order = sorted(data_sequence, reverse=True)  # descending order
    result_list: List[str] = []
    for val in desc_order:
        if val in num_map:
            result_list.append(num_map[val])
    return result_list