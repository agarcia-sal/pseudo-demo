from typing import List

def sorted_list_sum(list_of_strings: List[str]) -> List[str]:
    list_of_strings_sorted = sorted(list_of_strings)  # sort ascending alphabetically
    container = [item for item in list_of_strings_sorted if len(item) % 2 == 0]
    return sorted(container, key=len)