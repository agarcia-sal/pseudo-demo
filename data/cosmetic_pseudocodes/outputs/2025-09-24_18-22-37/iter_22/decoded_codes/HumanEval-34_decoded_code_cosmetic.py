from typing import Iterable, List, TypeVar

T = TypeVar('T')

def unique(collection_of_items: Iterable[T]) -> List[T]:
    interim_set = set()
    index_counter = 0
    # Convert collection_of_items to a sequence to support indexing
    items = list(collection_of_items)
    list_length = len(items)
    while index_counter < list_length:
        interim_set.add(items[index_counter])
        index_counter += 1
    interim_list: List[T] = []
    for element in interim_set:
        interim_list.append(element)
    sorted_list = interim_list
    swap_flag = True
    while swap_flag:
        swap_flag = False
        position = 0
        while position < len(sorted_list) - 1:
            if sorted_list[position] > sorted_list[position + 1]:
                temp_value = sorted_list[position]
                sorted_list[position] = sorted_list[position + 1]
                sorted_list[position + 1] = temp_value
                swap_flag = True
            position += 1
    return sorted_list