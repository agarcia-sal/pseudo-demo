from typing import List, TypeVar

T = TypeVar('T')

def unique(array_input: List[T]) -> List[T]:
    temp_storage: List[T] = []
    for element in array_input:
        if element not in temp_storage:
            temp_storage.append(element)
    counter: int = len(temp_storage) - 1
    while counter > 0:
        index: int = 0
        while index < counter:
            if temp_storage[index] > temp_storage[index + 1]:
                # Swap elements
                holder = temp_storage[index]
                temp_storage[index] = temp_storage[index + 1]
                temp_storage[index + 1] = holder
            index += 1
        counter -= 1
    return temp_storage