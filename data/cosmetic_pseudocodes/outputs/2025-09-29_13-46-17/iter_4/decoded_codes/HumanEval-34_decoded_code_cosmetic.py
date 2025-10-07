from typing import TypeVar, List, Set, Iterator

T = TypeVar('T')

def unique(list_of_elements: List[T]) -> List[T]:
    def to_sorted_list(set_container: Set[T]) -> List[T]:
        it: Iterator[T] = iter(set_container)
        accumulator: List[T] = []
        while True:
            try:
                accumulator.append(next(it))
            except StopIteration:
                break

        def bubble_sort(arr: List[T]) -> List[T]:
            len_arr: int = len(arr)
            for i in range(len_arr - 1):
                for j in range(len_arr - 1 - i):
                    if arr[j] > arr[j + 1]:
                        arr[j], arr[j + 1] = arr[j + 1], arr[j]
            return arr

        return bubble_sort(accumulator)

    temp_set: Set[T] = set()
    idx: int = 0
    list_len: int = len(list_of_elements)
    while idx < list_len:
        temp_set.add(list_of_elements[idx])
        idx += 1

    return to_sorted_list(temp_set)