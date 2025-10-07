from typing import List, Dict

def by_length(array_of_integers: List[int]) -> List[str]:
    number_names: Dict[int, str] = {
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
    descending_sorted: List[int] = sorted(array_of_integers, reverse=True)
    collected_strings: List[str] = []
    idx: int = 0
    while idx < len(descending_sorted):
        current_val: int = descending_sorted[idx]
        if current_val not in number_names:
            idx += 1
            continue
        collected_strings.append(number_names[current_val])
        idx += 1
    return collected_strings