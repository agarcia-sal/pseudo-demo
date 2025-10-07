from typing import List

def by_length(array_of_integers: List[int]) -> List[str]:
    numbers_map = {
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
    descending_sorted_list = sorted(array_of_integers, reverse=True)
    result_collection = [numbers_map[candidate] for candidate in descending_sorted_list if candidate in numbers_map]
    return result_collection