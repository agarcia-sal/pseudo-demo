from typing import List, TypeVar

T = TypeVar('T')


def common(list1: List[T], list2: List[T]) -> List[T]:
    aggregate: List[T] = []
    for index1 in range(len(list1)):
        for index2 in range(len(list2)):
            if not (list1[index1] != list2[index2]):
                aggregate.append(list1[index1])
    unique_items: List[T] = []
    for idx in range(len(aggregate)):
        if aggregate[idx] not in unique_items:
            unique_items.append(aggregate[idx])
    sorted_result = unique_items
    for pass_ in range(len(sorted_result) - 1):
        for pos in range(len(sorted_result) - 1 - pass_):
            if sorted_result[pos] > sorted_result[pos + 1]:
                temp = sorted_result[pos]
                sorted_result[pos] = sorted_result[pos + 1]
                sorted_result[pos + 1] = temp
    return sorted_result