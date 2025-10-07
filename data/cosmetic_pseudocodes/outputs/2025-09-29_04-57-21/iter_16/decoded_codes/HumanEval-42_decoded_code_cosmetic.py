from typing import List, Iterable

def incr_list(list_of_elements: Iterable[int]) -> List[int]:
    output_collection: List[int] = []
    iterator = iter(list_of_elements)
    while True:
        try:
            current_value = next(iterator)
        except StopIteration:
            break
        output_collection.append(1 + current_value)
    return output_collection