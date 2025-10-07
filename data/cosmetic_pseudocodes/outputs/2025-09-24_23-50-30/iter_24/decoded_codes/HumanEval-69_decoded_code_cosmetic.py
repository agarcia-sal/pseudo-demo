from typing import List

def search(array_of_numbers: List[int]) -> int:
    bag: List[int] = []
    apex: int = 0
    while apex < len(array_of_numbers):
        bag.append(0)
        apex += 1
    node: int = 0
    while node < len(array_of_numbers):
        element: int = array_of_numbers[node]
        existing_value: int = bag[element]
        bag[element] = existing_value + 1
        node += 1
    result: int = -1
    pointer: int = 1
    while pointer <= len(bag) - 1:
        if not (bag[pointer] < pointer):
            result = pointer
        pointer += 1
    return result