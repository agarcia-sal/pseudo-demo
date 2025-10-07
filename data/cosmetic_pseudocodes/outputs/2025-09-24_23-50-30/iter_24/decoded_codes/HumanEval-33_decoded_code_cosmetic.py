from typing import List, TypeVar

T = TypeVar('T')


def sort_third(array_alpha: List[T]) -> List[T]:
    temp_beta: List[T] = array_alpha[:]  # clone array_alpha
    gamma_indices: List[int] = []
    delta_values: List[T] = []

    epsilon_index: int = 0
    while epsilon_index < len(temp_beta):
        if epsilon_index % 3 == 0:
            gamma_indices.append(epsilon_index)
            delta_values.append(temp_beta[epsilon_index])
        epsilon_index += 1

    def bubble_sort(arr_charlie: List[T], size_delta: int) -> None:
        if size_delta <= 1:
            return
        index_foxtrot: int = 0
        while index_foxtrot < size_delta - 1:
            if arr_charlie[index_foxtrot] > arr_charlie[index_foxtrot + 1]:
                arr_charlie[index_foxtrot], arr_charlie[index_foxtrot + 1] = (
                    arr_charlie[index_foxtrot + 1],
                    arr_charlie[index_foxtrot],
                )
            index_foxtrot += 1
        bubble_sort(arr_charlie, size_delta - 1)

    bubble_sort(delta_values, len(delta_values))

    index_golf: int = 0
    while index_golf < len(gamma_indices):
        temp_beta[gamma_indices[index_golf]] = delta_values[index_golf]
        index_golf += 1

    return temp_beta