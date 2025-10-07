from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    list_clone: List[T] = []
    idx_counter: int = 0
    while idx_counter < len(list_input):
        list_clone.append(list_input[idx_counter])
        idx_counter += 1

    temp_collection: List[T] = []
    iterator_var: int = 0
    while iterator_var < len(list_clone):
        if iterator_var % 3 == 0:
            temp_collection.append(list_clone[iterator_var])
        iterator_var += 1

    copy_of_temp: List[T] = []
    copy_idx: int = 0
    while copy_idx < len(temp_collection):
        copy_of_temp.append(temp_collection[copy_idx])
        copy_idx += 1

    sort_start: int = 0
    while sort_start < len(copy_of_temp):
        min_pos: int = sort_start
        sort_inner: int = sort_start + 1
        while sort_inner < len(copy_of_temp):
            if copy_of_temp[sort_inner] < copy_of_temp[min_pos]:
                min_pos = sort_inner
            sort_inner += 1

        temp_storage: T = copy_of_temp[sort_start]
        copy_of_temp[sort_start] = copy_of_temp[min_pos]
        copy_of_temp[min_pos] = temp_storage
        sort_start += 1

    replace_idx: int = 0
    tgt_index: int = 0
    while tgt_index < len(list_clone):
        if tgt_index % 3 == 0:
            list_clone[tgt_index] = copy_of_temp[replace_idx]
            replace_idx += 1
        tgt_index += 1

    return list_clone