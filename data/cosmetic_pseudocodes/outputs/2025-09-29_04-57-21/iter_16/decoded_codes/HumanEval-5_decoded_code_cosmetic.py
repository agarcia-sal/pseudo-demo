from typing import List, Iterator

def intersperse(list_of_numbers: List[int], delimiter: int) -> List[int]:
    if not list_of_numbers:
        return []

    output_sequence: List[int] = []
    iterator: Iterator[int] = iter(list_of_numbers)
    current_element: int = next(iterator)

    for next_element in iterator:
        output_sequence.append(current_element)
        output_sequence.append(delimiter)
        current_element = next_element

    output_sequence.append(current_element)
    return output_sequence