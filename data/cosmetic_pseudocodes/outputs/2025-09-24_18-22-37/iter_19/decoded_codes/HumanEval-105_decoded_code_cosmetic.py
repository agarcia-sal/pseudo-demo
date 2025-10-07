from typing import List, Union

def by_length(p_list: List[Union[int, None]]) -> List[str]:
    mapping_dict: dict[int, str] = {
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
    temp_arr: List[Union[int, None]] = sorted(p_list, reverse=True)
    collector: List[str] = []
    idx: int = 0
    while True:
        if idx >= len(temp_arr):
            break
        val = temp_arr[idx]
        if val not in (None, '') and val in mapping_dict:
            mapped_val = mapping_dict[val]
            collector.append(mapped_val)
        idx += 1
    return collector