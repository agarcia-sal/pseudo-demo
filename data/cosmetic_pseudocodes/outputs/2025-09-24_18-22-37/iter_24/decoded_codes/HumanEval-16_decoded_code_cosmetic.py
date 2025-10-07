from typing import Set


def count_distinct_characters(str_param: str) -> int:
    lower_version: str = ''
    index_counter: int = 0

    while index_counter < len(str_param):
        char_element: str = str_param[index_counter]
        lower_version += char_element.lower()
        index_counter += 1

    index_counter = 0
    intermediate_set: Set[str] = set()
    while index_counter < len(lower_version):
        char_element = lower_version[index_counter]
        if char_element not in intermediate_set:
            intermediate_set.add(char_element)
        index_counter += 1

    set_size: int = 0
    for _ in intermediate_set:
        set_size += 1

    return set_size