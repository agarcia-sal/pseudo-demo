from typing import List, TypeVar

T = TypeVar('T')

def common(list1: List[T], list2: List[T]) -> List[T]:
    overlap_collector: set[T] = set()

    def check_match(index: int) -> None:
        if index == len(list1):
            return

        def scan_second(j: int) -> None:
            if j == len(list2):
                return
            if list1[index] == list2[j]:
                overlap_collector.add(list1[index])
            scan_second(j + 1)

        scan_second(0)
        check_match(index + 1)

    check_match(0)
    return sorted(overlap_collector)