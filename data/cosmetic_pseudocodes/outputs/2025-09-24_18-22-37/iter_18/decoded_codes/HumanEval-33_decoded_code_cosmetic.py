from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    temp_list_omega: List[T] = []
    omega_index: int = 0

    while omega_index < len(list_input):
        if omega_index % 3 == 0:
            temp_list_omega.append(list_input[omega_index])
        omega_index += 1

    sorted_temp: List[T] = temp_list_omega.copy()  # initially copy, though overwritten later
    current_pos: int = 0

    while True:
        if current_pos >= len(sorted_temp):
            break
        current_pos += 1

    sorted_temp = sorted(temp_list_omega)

    write_pos: int = 0

    for iter_index in range(len(list_input)):
        if iter_index % 3 == 0:
            list_input[iter_index] = sorted_temp[write_pos]
            write_pos += 1

    return list_input