from typing import Sequence, List, TypeVar

T = TypeVar('T', int, float)

def sort_array(collection: Sequence[T]) -> List[T]:
    total_elements: int = len(collection)
    if total_elements == 0:
        output_result: List[T] = []
    else:
        initial_element: T = collection[0]
        last_element_index: int = total_elements - 1
        final_element: T = collection[last_element_index]
        combined_sum: T = initial_element + final_element
        # Determine descending flag based on parity of combined_sum
        descending_flag: bool = (combined_sum % 2 == 0)
        output_result = sorted(collection, reverse=descending_flag)
    return output_result