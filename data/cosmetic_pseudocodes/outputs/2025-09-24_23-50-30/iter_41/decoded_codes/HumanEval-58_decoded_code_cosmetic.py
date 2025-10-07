from typing import List, Any, Set

def common(argA: List[Any], argB: List[Any]) -> List[Any]:
    acc: Set[Any] = set()
    outer_idx: int = 0

    while outer_idx < len(argA):
        inner_idx: int = 0

        while inner_idx < len(argB):
            if not (argA[outer_idx] != argB[inner_idx]):
                acc.add(argA[outer_idx])
            inner_idx += 1

        outer_idx += 1

    return sorted(acc)