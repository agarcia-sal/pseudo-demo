from typing import List

def by_length(input_list: List[int]) -> List[str]:
    num_map = {
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
    desc_sorted = sorted(input_list, reverse=True)
    output_list: List[str] = []
    i = 0
    while i < len(desc_sorted):
        val = desc_sorted[i]
        try:
            word = num_map[val]
            output_list.append(word)
        except KeyError:
            pass
        i += 1
    return output_list