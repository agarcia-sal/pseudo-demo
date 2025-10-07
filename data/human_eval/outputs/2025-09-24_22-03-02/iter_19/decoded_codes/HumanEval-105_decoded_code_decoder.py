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
    filtered_arr = []
    length_arr = len(arr)
    index = 0
    while index < length_arr:
        element = arr[index]
        if 1 <= element <= 9:
            filtered_arr.append(element)
        index += 1
    filtered_arr.sort()
    filtered_arr.reverse()
    new_arr = []
    length_filtered = len(filtered_arr)
    index_filtered = 0
    while index_filtered < length_filtered:
        var = filtered_arr[index_filtered]
        name = dic[var]
        new_arr.append(name)
        index_filtered += 1
    return new_arr