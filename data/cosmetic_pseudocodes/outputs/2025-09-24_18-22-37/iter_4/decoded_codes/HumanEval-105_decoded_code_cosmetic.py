from typing import List

def by_length(input_list: List[int]) -> List[str]:
    num_words_map = {
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
    descending_sorted = sorted(input_list, reverse=True)
    result_list: List[str] = []
    index = 0
    while index < len(descending_sorted):
        current_val = descending_sorted[index]
        if current_val in num_words_map:
            result_list.append(num_words_map[current_val])
        index += 1
    return result_list