from typing import Sequence, TypeVar

T = TypeVar('T')

def monotonic(collection: Sequence[T]) -> bool:
    def check_non_decreasing(sequence: Sequence[T], index: int, limit: int, result_flag: bool) -> bool:
        if index >= limit:
            return result_flag
        if sequence[index] > sequence[index + 1]:
            return False
        return check_non_decreasing(sequence, index + 1, limit, result_flag)

    def check_non_increasing(sequence: Sequence[T], position: int, boundary: int, status: bool) -> bool:
        if position >= boundary:
            return status
        if sequence[position] < sequence[position + 1]:
            return False
        return check_non_increasing(sequence, position + 1, boundary, status)

    n = len(collection)
    if n < 2:
        return True  # A collection with fewer than 2 elements is trivially monotonic

    ascending_result = check_non_decreasing(collection, 0, n - 1, True)
    descending_result = check_non_increasing(collection, 0, n - 1, True)

    if ascending_result:
        return True
    if descending_result:
        return True
    return False