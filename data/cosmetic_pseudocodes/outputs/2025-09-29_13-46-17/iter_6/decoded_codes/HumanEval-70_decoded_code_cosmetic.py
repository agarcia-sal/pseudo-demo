from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    tabulationX: List[int] = []
    flag_TOGGLE: bool = True

    def inner_FUNC(inputList: List[int], accum: List[int], togFlag: bool) -> List[int]:
        if not inputList:
            return accum
        current_val = min(inputList) if togFlag else max(inputList)

        def helper_REMOVE(listToProcess: List[int], valToRemove: int, idx: int, accumulated: List[int]) -> List[int]:
            if idx >= len(listToProcess):
                return accumulated
            head_element = listToProcess[idx]
            newAccumulated = accumulated if head_element == valToRemove else accumulated + [head_element]
            return helper_REMOVE(listToProcess, valToRemove, idx + 1, newAccumulated)

        nextList = helper_REMOVE(inputList, current_val, 0, [])
        return inner_FUNC(nextList, accum + [current_val], not togFlag)

    return inner_FUNC(list_of_integers, tabulationX, flag_TOGGLE)