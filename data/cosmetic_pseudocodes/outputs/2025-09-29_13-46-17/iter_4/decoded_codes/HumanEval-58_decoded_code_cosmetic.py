from typing import List, Set

def common(list1: List[str], list2: List[str]) -> List[str]:
    def helper(idxA: int, acc: Set[str]) -> Set[str]:
        if idxA >= len(list1):
            return acc
        else:
            element_a = list1[idxA]
            def inner_loop(idxB: int) -> Set[str]:
                if idxB >= len(list2):
                    return acc
                else:
                    current_b = list2[idxB]
                    acc_updated = acc | ({element_a} if element_a == current_b else set())
                    return inner_loop(idxB + 1)
            return helper(idxA + 1, inner_loop(0))

    final_set = helper(0, set())
    return sorted(final_set)