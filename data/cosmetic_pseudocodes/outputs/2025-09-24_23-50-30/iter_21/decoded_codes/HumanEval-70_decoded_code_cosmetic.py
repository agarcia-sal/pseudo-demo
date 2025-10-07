from typing import List, TypeVar

T = TypeVar('T')

def strange_sort_list(input_sequence: List[T]) -> List[T]:
    output_collection: List[T] = []
    toggle_switch: bool = True
    while input_sequence:
        candidate = min(input_sequence) if toggle_switch else max(input_sequence)
        remove_value_from_list(input_sequence, candidate)
        output_collection.append(candidate)
        toggle_switch = not toggle_switch
    return output_collection

def remove_value_from_list(collection: List[T], item: T) -> None:
    for index in range(len(collection)):
        if collection[index] == item:
            del collection[index]
            break