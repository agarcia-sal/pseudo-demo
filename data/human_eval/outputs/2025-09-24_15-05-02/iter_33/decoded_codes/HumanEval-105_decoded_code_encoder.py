from typing import List

def by_length(array_of_integers: List[int]) -> List[str]:
    dictionary_of_number_names: dict[int, str] = {
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
    sorted_array: List[int] = sorted(array_of_integers, reverse=True)
    new_array: List[str] = []
    for element in sorted_array:
        try:
            new_array.append(dictionary_of_number_names[element])
        except KeyError:
            pass
    return new_array