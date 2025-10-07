from typing import List, Set

def common(list1: List[str], list2: List[str]) -> List[str]:
    def innerMatch(index1: int, index2: int, accumulator: Set[str]) -> Set[str]:
        if index1 == len(list1):
            return accumulator
        elif index2 == len(list2):
            return innerMatch(index1 + 1, 0, accumulator)
        elif list1[index1] == list2[index2]:
            accumulator = accumulator.union({list1[index1]})
            return innerMatch(index1, index2 + 1, accumulator)
        else:
            return innerMatch(index1, index2 + 1, accumulator)

    result = innerMatch(0, 0, set())
    return sorted(element for element in result)