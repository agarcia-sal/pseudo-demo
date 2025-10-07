from typing import List, TypeVar

T = TypeVar('T', bound=object)

def sort_third(list_input: List[T]) -> List[T]:
    temp_list = list(list_input)  # Create a copy to avoid mutating the input
    indices = [i for i in range(len(temp_list)) if i % 3 == 0]
    extracted_elements = [temp_list[i] for i in indices]
    ordered_elements = sorted(extracted_elements)
    for i, idx in enumerate(indices):
        temp_list[idx] = ordered_elements[i]
    return temp_list