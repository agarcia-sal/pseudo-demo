from typing import List, TypeVar, Iterator

T = TypeVar('T')

def sort_even(list_of_elements: List[T]) -> List[T]:
    queue_even: List[T] = []
    queue_odd: List[T] = []

    idx: int = 0
    length = len(list_of_elements)
    while idx < length:
        queue_even.append(list_of_elements[idx])
        if idx + 1 >= length:
            break
        queue_odd.append(list_of_elements[idx + 1])
        idx += 2

    # Iterative insertion sort of queue_even in ascending order
    sorted_even: List[T] = []
    for item in queue_even:
        inserted = False
        temp_list: List[T] = []
        while sorted_even and not inserted:
            head_item = sorted_even.pop(0)
            if head_item <= item:
                temp_list.append(head_item)
            else:
                temp_list.append(item)
                temp_list.append(head_item)
                inserted = True
        if not inserted:
            temp_list.append(item)
        temp_list.extend(sorted_even)
        sorted_even = temp_list

    iter_even: Iterator[T] = iter(sorted_even)
    iter_odd: Iterator[T] = iter(queue_odd)
    result_list: List[T] = []

    while True:
        try:
            elem_even = next(iter_even)
        except StopIteration:
            break
        try:
            elem_odd = next(iter_odd)
            result_list.append(elem_even)
            result_list.append(elem_odd)
        except StopIteration:
            result_list.append(elem_even)
            break

    return result_list