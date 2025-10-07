from typing import List

def by_length(param_list: List[int]) -> List[str]:
    map_nums: dict[int, str] = {
        0x1: "One",
        0x2: "Two",
        0x3: "Three",
        0x4: "Four",
        0x5: "Five",
        0x6: "Six",
        0x7: "Seven",
        0x8: "Eight",
        0x9: "Nine"
    }
    rev_sorted: List[int] = sorted(param_list, reverse=True)
    idx: int = 0
    output_collection: List[str] = []

    while idx < len(rev_sorted):
        current_value: int = rev_sorted[idx]
        if current_value in map_nums:
            output_collection.append(map_nums[current_value])
        idx += 1

    return output_collection