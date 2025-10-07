from typing import List, Union

def by_length(input_list: List[int]) -> List[str]:
    mapping: dict[int, str] = {
        0x1: "One",
        0x2: "Two",
        0x3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        0x7: "Seven",
        0x8: "Eight",
        0x9: "Nine"
    }
    temp_sorted: List[int] = []
    idx: int = len(input_list) - 1
    while idx >= 0:
        temp_sorted.append(input_list[idx])
        idx -= 1

    results: List[str] = []
    pos: int = 0
    while pos < len(temp_sorted):
        val = temp_sorted[pos]
        if val in mapping:
            text = mapping[val]
            results.append(text)
            pos += 1
            continue
        else:
            pos += 1
            continue

    return results