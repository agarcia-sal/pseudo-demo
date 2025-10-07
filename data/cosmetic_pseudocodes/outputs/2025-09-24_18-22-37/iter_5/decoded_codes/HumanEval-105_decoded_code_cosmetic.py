from typing import List

def by_length(input_list: List[int]) -> List[str]:
    num_words_map: dict[int, str] = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
    }
    temp_list: List[int] = sorted(input_list, reverse=True)
    result_container: List[str] = []

    idx: int = 0
    while idx < len(temp_list):
        curr_val: int = temp_list[idx]
        if curr_val in num_words_map:
            word_str: str = num_words_map[curr_val]
            result_container.append(word_str)
        idx += 1

    return result_container