from typing import List


def sorted_list_sum(list_of_strings: List[str]) -> List[str]:
    list_of_strings.sort()  # Sort ascending alphabetical
    accumulation: List[str] = []
    iterator_index = 0
    while iterator_index < len(list_of_strings):
        current_fragment = list_of_strings[iterator_index]
        if not (len(current_fragment) % 2 != 0):  # length is even
            accumulation.append(current_fragment)
        iterator_index += 1
    accumulation.sort(key=len)  # sort by length ascending
    return accumulation