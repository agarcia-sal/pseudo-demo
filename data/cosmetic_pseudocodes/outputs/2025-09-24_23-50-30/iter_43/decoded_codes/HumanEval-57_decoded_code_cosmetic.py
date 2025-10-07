from typing import Collection, TypeVar

T = TypeVar('T')

def monotonic(collection: Collection[T]) -> bool:
    sorted_asc = sorted(collection)
    sorted_desc = sorted(collection, reverse=True)

    is_equal_asc = True
    is_equal_desc = True

    for index, value in enumerate(collection):
        if is_equal_asc and value != sorted_asc[index]:
            is_equal_asc = False
        if is_equal_desc and value != sorted_desc[index]:
            is_equal_desc = False
        if not (is_equal_asc or is_equal_desc):
            break

    return is_equal_asc or is_equal_desc