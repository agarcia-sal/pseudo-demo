from typing import List

def string_sequence(integer_n: int) -> str:
    result_elements: List[str] = []
    alternate_index: int = 0
    while alternate_index <= integer_n:
        string_element: str = str(alternate_index)
        result_elements.append(string_element)
        alternate_index += 1

    combined_string: str = ""
    iterator_position: int = 0
    total_elements: int = len(result_elements)
    while iterator_position < total_elements:
        combined_string += result_elements[iterator_position]
        if iterator_position < total_elements - 1:
            combined_string += " "
        iterator_position += 1

    return combined_string