from typing import List

def maximum(array_of_integers: List[int], positive_integer_k: int) -> List[int]:
    if positive_integer_k != 0:
        array_of_integers.sort()
        start_index: int = len(array_of_integers) - positive_integer_k
        extracted_elements: List[int] = [
            array_of_integers[index] for index in range(start_index, len(array_of_integers))
        ]
        return extracted_elements
    else:
        return []