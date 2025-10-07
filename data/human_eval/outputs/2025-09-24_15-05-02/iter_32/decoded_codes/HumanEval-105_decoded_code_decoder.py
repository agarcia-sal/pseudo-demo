from typing import List, Dict

def by_length(array_of_integers: List[int]) -> List[str]:
    dictionary_of_number_names: Dict[int, str] = {
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
    sorted_array = sorted(array_of_integers, reverse=True)
    resulting_array: List[str] = []
    for element in sorted_array:
        try:
            resulting_array.append(dictionary_of_number_names[element])
        except KeyError:
            pass
    return resulting_array