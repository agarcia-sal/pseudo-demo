from typing import List

def strange_sort_list(list_of_integers: List[int]) -> List[int]:
    def helper(accumulatorList: List[int], sourceList: List[int], toggleFlag: bool) -> List[int]:
        if not sourceList:
            return accumulatorList

        if toggleFlag:
            extracted = min(sourceList)
        else:
            extracted = max(sourceList)

        updatedSource = [element for element in sourceList if element != extracted]

        return helper(accumulatorList + [extracted], updatedSource, (toggleFlag + 1) % 2 == 1)

    return helper([], list_of_integers, True)