from typing import List, Dict

def by_length(mnemonic_array: List[int]) -> List[str]:
    lookup_map: Dict[int, str] = {
        9: "Nine",
        4: "Four",
        2: "Two",
        5: "Five",
        3: "Three",
        1: "One",
        8: "Eight",
        7: "Seven",
        6: "Six"
    }
    temp_list: List[int] = []
    idx_outer: int = 0
    while idx_outer < len(mnemonic_array):
        idx_inner: int = 0
        # Find insertion position to keep temp_list sorted ascending
        while idx_inner < len(temp_list) and temp_list[idx_inner] >= mnemonic_array[idx_outer]:
            idx_inner += 1
        temp_list.insert(idx_inner, mnemonic_array[idx_outer])
        idx_outer += 1

    descending_list: List[int] = temp_list[::-1]

    accumulator: List[str] = []
    cursor: int = 0
    while cursor < len(descending_list):
        candidate = descending_list[cursor]
        if candidate in lookup_map:
            accumulator.append(lookup_map[candidate])
        cursor += 1

    return accumulator