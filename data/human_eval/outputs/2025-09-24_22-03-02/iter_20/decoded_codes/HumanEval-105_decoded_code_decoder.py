from typing import List

def by_length(arr: List[int]) -> List[str]:
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
    sorted_arr = arr[::-1]
    new_arr = [dic[v] for v in sorted_arr if 1 <= v <= 9]
    return new_arr