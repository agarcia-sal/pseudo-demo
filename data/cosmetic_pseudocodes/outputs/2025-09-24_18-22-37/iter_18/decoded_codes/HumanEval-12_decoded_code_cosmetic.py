from typing import List, Optional


def longest(array_of_texts: List[str]) -> Optional[str]:
    if not array_of_texts:
        return None

    greatest_size: int = -1
    iterator_index: int = 0

    while iterator_index < len(array_of_texts):
        current_element: str = array_of_texts[iterator_index]
        temp_length: int = len(current_element)
        if temp_length > greatest_size:
            greatest_size = temp_length
        iterator_index += 1

    iterator_index = 0
    while iterator_index < len(array_of_texts):
        current_element = array_of_texts[iterator_index]
        temp_length = len(current_element)
        if not (temp_length != greatest_size):
            return current_element
        iterator_index += 1