from typing import List

def by_length(array: List[int]) -> List[str]:
    dic: dict[int, str] = {
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
    sorted_arr: List[int] = sorted(array, reverse=True)
    new_arr: List[str] = []
    for element in sorted_arr:
        if element in dic:
            new_arr.append(dic[element])
    return new_arr