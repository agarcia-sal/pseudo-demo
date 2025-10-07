from typing import List, TypeVar

T = TypeVar('T')

def sort_third(array_data: List[T]) -> List[T]:
    temp_array: List[T] = list(array_data)
    indices_for_sorting: List[int] = [idx for idx in range(len(temp_array)) if idx % 3 == 0]

    extraction_list: List[T] = [temp_array[i] for i in indices_for_sorting]
    sorted_extracted: List[T] = sorted(extraction_list)

    for pos, idx in enumerate(indices_for_sorting):
        temp_array[idx] = sorted_extracted[pos]

    return temp_array