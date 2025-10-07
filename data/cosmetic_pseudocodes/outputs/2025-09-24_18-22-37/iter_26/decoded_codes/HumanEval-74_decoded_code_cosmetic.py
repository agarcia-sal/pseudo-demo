from typing import List, Union

def total_match(list_one: List[str], list_two: List[str]) -> List[str]:
    alpha_counter: int = 0
    idx_one: int = 0
    while idx_one < len(list_one):
        current_str: str = list_one[idx_one]
        str_len: int = len(current_str)
        alpha_counter += str_len
        idx_one += 1

    beta_counter: int = 0
    pos_two: int = 0
    while pos_two < len(list_two):
        segment: str = list_two[pos_two]
        segment_length: int = len(segment)
        beta_counter += segment_length
        pos_two += 1

    if alpha_counter <= beta_counter:
        return list_one
    else:
        return list_two