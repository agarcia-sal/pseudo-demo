from typing import List, TypeVar

T = TypeVar('T')


def sort_third(list_input: List[T]) -> List[T]:
    mutable_list: List[T] = list(list_input)
    selected_elements: List[T] = [mutable_list[idx] for idx in range(len(mutable_list)) if idx % 3 == 0]

    ordered_elements: List[T] = sorted(selected_elements)

    insert_pos: int = 0
    for idx in range(len(mutable_list)):
        if idx % 3 == 0:
            mutable_list[idx] = ordered_elements[insert_pos]
            insert_pos += 1

    return mutable_list