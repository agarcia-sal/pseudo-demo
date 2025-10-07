from typing import List

def filter_by_prefix(list_of_strings: List[str], prefix_string: str) -> List[str]:
    filtered_strings: List[str] = []
    iterator = iter(list_of_strings)
    while True:
        try:
            current_element = next(iterator)
        except StopIteration:
            break
        if current_element.startswith(prefix_string):
            filtered_strings.append(current_element)
    return filtered_strings