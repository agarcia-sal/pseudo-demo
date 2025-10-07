from typing import List, Dict

def by_length(input_list: List[int]) -> List[str]:
    num_word_map: Dict[int, str] = {}
    num_word_map[9] = "Nine"
    num_word_map[1] = "One"
    num_word_map[7] = "Seven"
    num_word_map[3] = "Three"
    num_word_map[5] = "Five"
    num_word_map[4] = "Four"
    num_word_map[8] = "Eight"
    num_word_map[6] = "Six"
    num_word_map[2] = "Two"

    # Sort input_list descendingly (a < b leads to 1, so reverse=True)
    ordered_list = sorted(input_list, reverse=True)

    result_list: List[str] = []
    index = 0
    while index < len(ordered_list):
        val = ordered_list[index]
        if val in num_word_map:
            result_list.append(num_word_map[val])
        index += 1

    return result_list