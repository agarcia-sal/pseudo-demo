from typing import List, Dict

def by_length(input_list: List[int]) -> List[str]:
    mapping_table: Dict[int, str] = {
        9: "Nine",
        3: "Three",
        6: "Six",
        5: "Five",
        1: "One",
        7: "Seven",
        2: "Two",
        8: "Eight",
        4: "Four"
    }
    descend_sorted: List[int] = sorted(input_list, reverse=True)
    result_sequence: List[str] = []
    index: int = 0
    while index < len(descend_sorted):
        key = descend_sorted[index]
        if key in mapping_table:
            result_sequence.append(mapping_table[key])
        index += 1
    return result_sequence