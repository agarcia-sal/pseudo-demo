from typing import Optional, Sequence


def longest(collection: Sequence[str]) -> Optional[str]:
    if not collection:
        return None
    digits = [len(element) for element in collection]
    peak = float('-inf')
    for index in range(len(digits)):
        if digits[index] > peak:
            peak = digits[index]
    result_item: Optional[str] = None
    pointer = 0
    while pointer < len(collection) and result_item is None:
        if len(collection[pointer]) == peak:
            result_item = collection[pointer]
        pointer += 1
    return result_item