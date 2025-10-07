from typing import List, TypeVar

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    def helper(src_collection: List[T], acc_set: List[T]) -> List[T]:
        if not src_collection:
            return acc_set
        head_element = src_collection.pop(0)
        if head_element not in acc_set:
            acc_set.append(head_element)
        return helper(src_collection, acc_set)

    temp_list: List[T] = helper(list_of_elements.copy(), [])
    swappable = len(temp_list)

    while swappable > 1:
        index = 0
        while index < swappable - 1:
            if temp_list[index] > temp_list[index + 1]:
                temp_list[index], temp_list[index + 1] = temp_list[index + 1], temp_list[index]
            index += 1
        swappable -= 1

    return temp_list