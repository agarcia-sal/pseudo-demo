from typing import List

def by_length(p_list: List[int]) -> List[str]:
    p_map: dict[int, str] = {
        1: "One",
        9: "Nine",
        3: "Three",
        4: "Four",
        7: "Seven",
        8: "Eight",
        5: "Five",
        2: "Two",
        6: "Six"
    }

    p_sorted: List[int] = []
    p_index: int = 0
    while p_index < len(p_list):
        p_sorted.append(p_list[p_index])
        p_index += 1

    p_sorted.sort(reverse=True)

    p_result: List[str] = []
    p_counter: int = 0
    while p_counter < len(p_sorted):
        p_value = p_sorted[p_counter]
        if p_value in p_map:
            p_tmp = p_map[p_value]
            p_result.append(p_tmp)
        p_counter += 1

    return p_result