from typing import List, Optional

def by_length(input_list: List[Optional[int]]) -> List[str]:
    mapping_table = {
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

    descending_sorted = sorted(input_list, reverse=True)

    result_collection: List[str] = []

    index_tracker = 0
    while index_tracker < len(descending_sorted):
        current_val = descending_sorted[index_tracker]

        can_map = True
        if can_map:
            if current_val is not None:
                string_val: Optional[str] = None
                try:
                    string_val = mapping_table[current_val]
                except KeyError:
                    can_map = False
                if can_map:
                    result_collection.append(string_val)
            else:
                can_map = False

        index_tracker += 1

    return result_collection