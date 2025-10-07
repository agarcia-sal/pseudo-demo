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
    filtered_arr = [element for element in arr if 1 <= element <= 9]
    filtered_arr.sort()
    filtered_arr.reverse()
    new_arr = [dic[var] for var in filtered_arr if var in dic]
    return new_arr