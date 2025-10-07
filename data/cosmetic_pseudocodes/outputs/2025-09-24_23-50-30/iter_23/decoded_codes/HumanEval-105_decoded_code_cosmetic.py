from typing import List

def by_length(list_of_values: List[int]) -> List[str]:
    mapping = {
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
    descending_values = sorted(list_of_values, reverse=True)
    result_collection: List[str] = []
    index = 0
    while index < len(descending_values):
        current_value = descending_values[index]
        if current_value in mapping:
            result_collection.append(mapping[current_value])
        index += 1
    return result_collection