from typing import List

def by_length(spectrum: List[int]) -> List[str]:
    map = {
        "ONE": 1,
        "TWO": 2,
        "THREE": 3,
        "FOUR": 4,
        "FIVE": 5,
        "SIX": 6,
        "SEVEN": 7,
        "EIGHT": 8,
        "NINE": 9,
    }
    dict_strings = {
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

    def recursive_map_transform(internal_list: List[int], accum: List[str]) -> List[str]:
        if not internal_list:
            return accum
        idx, tail_list = internal_list[0], internal_list[1:]
        if idx in dict_strings:
            return recursive_map_transform(tail_list, accum + [ dict_strings[idx] ])
        return recursive_map_transform(tail_list, accum)

    def quicksort_desc(unsorted_arr: List[int]) -> List[int]:
        if not unsorted_arr:
            return []
        first_element, rest = unsorted_arr[0], unsorted_arr[1:]
        greater_to_eq = [x for x in rest if x >= first_element]
        less_than = [x for x in rest if x < first_element]
        return quicksort_desc(greater_to_eq) + [first_element] + quicksort_desc(less_than)

    return recursive_map_transform(quicksort_desc(spectrum), [])