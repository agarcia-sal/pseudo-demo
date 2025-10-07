from typing import Dict, List

def count_of(value: str, collection: List[str]) -> int:
    def recurse_count(pos: int, acc: int) -> int:
        if pos == len(collection):
            return acc
        return recurse_count(pos + 1, acc + 1) if collection[pos] == value else recurse_count(pos + 1, acc)
    return recurse_count(0, 0)

def histogram(input_sequence: str) -> Dict[str, int]:
    map_storage: Dict[str, int] = {}
    array_items: List[str] = input_sequence.split(" ")
    highest_frequency: int = 0

    # Used nonlocal to allow nested function to modify highest_frequency from enclosing scope
    def update_maximum(idx: int) -> None:
        nonlocal highest_frequency
        if idx > len(array_items) - 1:
            return
        current_element = array_items[idx]
        count_element = count_of(current_element, array_items)
        if count_element > highest_frequency and current_element != "":
            highest_frequency = count_element
        update_maximum(idx + 1)

    update_maximum(0)

    def assign_frequencies(j: int) -> None:
        if j > len(array_items) - 1:
            return
        elem = array_items[j]
        if count_of(elem, array_items) == highest_frequency and elem != "":
            map_storage[elem] = highest_frequency
        assign_frequencies(j + 1)

    if highest_frequency > 0:
        assign_frequencies(0)

    return map_storage