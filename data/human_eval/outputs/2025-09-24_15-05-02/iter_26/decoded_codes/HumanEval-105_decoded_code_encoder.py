from typing import List, Dict

def by_length(list_of_integers: List[int]) -> List[str]:
    digit_to_name_map: Dict[int, str] = {
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
    sorted_descending_list = sorted(list_of_integers, reverse=True)
    named_list: List[str] = []
    for integer_value in sorted_descending_list:
        name = digit_to_name_map.get(integer_value)
        if name is not None:
            named_list.append(name)
    return named_list