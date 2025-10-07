from typing import List

def by_length(array_of_integers: List[int]) -> List[str]:
    num_dict: dict[int, str] = {
        9: "Nine",
        7: "Seven",
        3: "Three",
        1: "One",
        8: "Eight",
        5: "Five",
        6: "Six",
        4: "Four",
        2: "Two"
    }
    descending_list: List[str] = []
    temp_list = list(array_of_integers)  # copy to avoid mutating input
    temp_list.sort(reverse=True)  # sort descending in place
    iterator_var = 0
    while iterator_var < len(temp_list):
        curr_val = temp_list[iterator_var]
        try:
            mapped_str = num_dict[curr_val]
        except KeyError:
            pass
        else:
            descending_list.append(mapped_str)
        iterator_var += 1
    return descending_list