from typing import List

def by_length(list_param: List[int]) -> List[str]:
    dictionary_map: dict[int, str] = {
        9: "Nine",
        8: "Eight",
        7: "Seven",
        6: "Six",
        5: "Five",
        4: "Four",
        3: "Three",
        2: "Two",
        1: "One"
    }

    def helper(index: int, accumulator: List[str]) -> List[str]:
        if index < 0:
            return accumulator
        if list_param[index] in dictionary_map:
            return helper(index - 1, accumulator + [dictionary_map[list_param[index]]])
        else:
            return helper(index - 1, accumulator)

    return helper(len(list_param) - 1, [])