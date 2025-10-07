from typing import List, TypeVar

T = TypeVar("T")

def sort_third(list_input: List[T]) -> List[T]:
    temp_list = list_input.copy()
    indices_multiple_of_3: List[int] = []
    extracted_vals: List[T] = []

    counter = 0
    while counter < len(temp_list):
        if counter % 3 == 0:
            extracted_vals.append(temp_list[counter])
            indices_multiple_of_3.append(counter)
        counter += 1

    extracted_vals.sort()

    i = 0
    while i < len(indices_multiple_of_3):
        idx = indices_multiple_of_3[i]
        temp_list[idx] = extracted_vals[i]
        i += 1

    return temp_list