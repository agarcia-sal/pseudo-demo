from typing import List


def sorted_list_sum(list_of_strings: List[str]) -> List[str]:
    sorted_strings = sorted(list_of_strings)
    filtered_collection: List[str] = []
    cursor = 0
    while cursor < len(sorted_strings):
        current_string = sorted_strings[cursor]
        if len(current_string) % 2 == 0:
            filtered_collection.append(current_string)
        cursor += 1
    return sorted(filtered_collection, key=len)