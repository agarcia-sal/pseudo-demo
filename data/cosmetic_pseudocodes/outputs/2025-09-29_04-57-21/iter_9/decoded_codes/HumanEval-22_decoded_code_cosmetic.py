from typing import List, Any

def filter_integers(list_of_values: List[Any]) -> List[int]:
    filtered_elements: List[int] = []
    iterator = iter(list_of_values)

    while True:
        try:
            current_item = next(iterator)
        except StopIteration:
            break
        if not isinstance(current_item, int):
            continue
        filtered_elements.append(current_item)

    return filtered_elements