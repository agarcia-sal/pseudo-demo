from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    accumulator = set()
    index_outer = 0
    while index_outer < len(list1):
        index_inner = 0
        while index_inner < len(list2):
            if list1[index_outer] == list2[index_inner]:
                temp_val = list1[index_outer]
                accumulator.add(temp_val)
            index_inner += 1
        index_outer += 1
    output_list = sorted(accumulator)
    return output_list