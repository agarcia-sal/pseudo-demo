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
        9: "Nine"
    }
    filtered_arr = [var for var in arr if 1 <= var <= 9]
    sorted_arr = sorted(filtered_arr, reverse=True)
    new_arr = [dic[var] for var in sorted_arr]
    return new_arr