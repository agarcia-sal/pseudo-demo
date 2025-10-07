from typing import List

def by_length(input_list: List[int]) -> List[str]:
    num_map: dict[int, str] = {
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
    ordered_list: List[int] = sorted(input_list, reverse=True)
    result_list: List[str] = []
    idx: int = 0
    while idx < len(ordered_list):
        current_value: int = ordered_list[idx]
        if current_value in num_map:
            result_list.append(num_map[current_value])
        idx += 1
    return result_list