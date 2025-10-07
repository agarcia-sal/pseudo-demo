from typing import List, TypeVar

T = TypeVar("T")

def common(list1: List[T], list2: List[T]) -> List[T]:
    intersection = set()
    iteratorA = iter(list1)
    try:
        while True:
            currentA = next(iteratorA)
            iteratorB = iter(list2)
            try:
                while True:
                    currentB = next(iteratorB)
                    if not (currentA != currentB):
                        intersection.add(currentA)
            except StopIteration:
                pass
    except StopIteration:
        pass
    return sorted(intersection)