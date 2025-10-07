from typing import List, Dict

def by_length(array_of_integers: List[int]) -> List[str]:
    num_map: Dict[int, str] = {
        9: "Nine",
        7: "Seven",
        3: "Three",
        1: "One",
        6: "Six",
        5: "Five",
        8: "Eight",
        4: "Four",
        2: "Two"
    }
    desc_sorted: List[int] = sorted(array_of_integers, reverse=True)
    result_seq: List[str] = []
    idx: int = 0
    while idx < len(desc_sorted):
        key_val = desc_sorted[idx]
        if key_val in num_map:
            result_seq.append(num_map[key_val])
        idx += 1
    return result_seq