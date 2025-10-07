from typing import List

def by_length(array_of_integers: List[int]) -> List[str]:
    dic = {
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
    sorted_arr = sorted(array_of_integers, reverse=True)
    new_arr: List[str] = []
    for element in sorted_arr:
        if element in dic:
            new_arr.append(dic[element])
    return new_arr