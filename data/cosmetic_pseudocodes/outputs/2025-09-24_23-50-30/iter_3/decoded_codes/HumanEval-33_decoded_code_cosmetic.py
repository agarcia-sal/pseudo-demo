from typing import List, TypeVar

T = TypeVar('T')

def sort_third(list_input: List[T]) -> List[T]:
    temp_list: List[T] = [x for x in list_input]
    temp_storage: List[T] = []
    for index in range(0, len(temp_list), 3):
        temp_storage.append(temp_list[index])
    temp_storage.sort()
    counter = 0
    for i in range(0, len(temp_list), 3):
        temp_list[i] = temp_storage[counter]
        counter += 1
    return temp_list