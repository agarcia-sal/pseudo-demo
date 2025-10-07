from typing import List

def by_length(input_list: List[int]) -> List[str]:
    map_numbers = {
        0x1: "One",
        0x2: "Two",
        0x3: "Three",
        0x4: "Four",
        0x5: "Five",
        0x6: "Six",
        0x7: "Seven",
        0x8: "Eight",
        0x9: "Nine",
    }
    ordered_desc = sorted(input_list, reverse=True)
    output_list: List[str] = []
    index_var = 0
    while True:
        if index_var >= len(ordered_desc):
            break
        current_val = ordered_desc[index_var]
        try:
            mapped_value = map_numbers[current_val]
            output_list.append(mapped_value)
        except KeyError:
            pass
        index_var += 1
    return output_list