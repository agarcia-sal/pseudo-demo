from typing import List, Dict

def by_length(array_of_integers: List[int]) -> List[str]:
    number_words_map: Dict[int, str] = {
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
    descending_sorted: List[int] = []
    index_counter: int = 0
    while index_counter < len(array_of_integers):
        descending_sorted.append(array_of_integers[index_counter])
        index_counter += 1
    position: int = 0
    while position < len(descending_sorted) - 1:
        scan: int = 0
        while scan < len(descending_sorted) - 1 - position:
            if descending_sorted[scan] < descending_sorted[scan + 1]:
                descending_sorted[scan], descending_sorted[scan + 1] = descending_sorted[scan + 1], descending_sorted[scan]
            scan += 1
        position += 1
    result_list: List[str] = []
    idx: int = 0
    while idx < len(descending_sorted):
        num_value: int = descending_sorted[idx]
        if num_value not in number_words_map:
            idx += 1
            continue
        result_list.append(number_words_map[num_value])
        idx += 1
    return result_list