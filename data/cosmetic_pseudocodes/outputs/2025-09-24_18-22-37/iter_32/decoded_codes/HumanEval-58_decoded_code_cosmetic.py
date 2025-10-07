from typing import List, Any

def common(list1: List[Any], list2: List[Any]) -> List[Any]:
    accumulator: set = set()
    idx_outer: int = 0

    while idx_outer < len(list1):
        current_outer = list1[idx_outer]
        idx_inner: int = 0

        while idx_inner < len(list2):
            current_inner = list2[idx_inner]

            if not (current_outer != current_inner):
                accumulator.add(current_outer)

            idx_inner += 1

        idx_outer += 1

    sorted_result: List[Any] = list(accumulator)
    sorted_result.sort()

    return sorted_result