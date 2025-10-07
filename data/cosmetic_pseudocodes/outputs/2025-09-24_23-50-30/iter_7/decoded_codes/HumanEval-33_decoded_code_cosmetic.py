from typing import List, TypeVar

T = TypeVar('T')


def sort_third(list_input: List[T]) -> List[T]:
    temp_list: List[T] = [list_input[index] for index in range(len(list_input)) if index % 3 == 0]

    n: int = len(temp_list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if temp_list[j] > temp_list[j + 1]:
                temp_list[j], temp_list[j + 1] = temp_list[j + 1], temp_list[j]

    p: int = 0
    while p < len(list_input):
        if p % 3 == 0:
            list_input[p] = temp_list.pop(0)
        p += 1

    return list_input